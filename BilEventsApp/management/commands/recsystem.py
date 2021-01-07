import pandas as pd
import numpy as np  
import xgboost as xgb
from surprise import SVD, Dataset, accuracy, BaselineOnly, Reader
from surprise.model_selection import train_test_split, cross_validate
from django.core.management.base import BaseCommand
from BilEventsApp.models import Club, Event, RecommendedEvent, Participant, Rate
from surprise.model_selection import KFold
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer
from django.utils import timezone


class Command(BaseCommand):

    help = 'Execute the recommender engine.'  

    def one_hot_encoding(self, description):
        tags = description.split()
        categories_dict = {"FUN":0.0, "EDU":1.0, "SCI":2.0, "ART":3.0, "IKT":4.0, "HUM":5.0, "BUSS":6.0, "LAW":7.0, "ENGR":8.0, "MUS":9.0, "APS":10.0}
        one_hot_vector = 11.0
        if description in categories_dict.keys():
            one_hot_vector = categories_dict[description.upper()]
        return one_hot_vector

    def create_cb_dataset(self):
        content_train_x = {
                        'userID': [],
                        'enter_year': [],
                        'club_tags': [],
                        'event_points': [],
                        'event_current_capacity': [],
                        'event_max_capacity': [],
                        'event_avg_score':[],
                        'event_tags': [],
                        }
        content_test_x = {
                        'userID': [],
                        'enter_year': [],
                        'club_tags': [],
                        'event_points': [],
                        'event_current_capacity': [],
                        'event_max_capacity': [],
                        'event_avg_score':[],
                        'event_tags': [],
                        }
        
        content_train_y = {'rating': []}
        content_test_y = {'rating': []}
        content_test_items = {'itemID': []}

        events = list(Event.objects.all())
        for event in events:
            participants = event.participants.all()
            for participant in participants:
                rate = Rate.objects.get(event=event, participant=participant)
                if rate.event_score != 0:
                    content_train_x['userID'].append(participant.bilkent_id)
                    content_train_x['enter_year'].append(int(str(participant.bilkent_id)[:3]))
                    content_train_x['club_tags'].append(self.one_hot_encoding(event.club.club_tags))
                    content_train_x['event_tags'].append(self.one_hot_encoding(event.event_tags))
                    content_train_x['event_points'].append(event.event_points)
                    content_train_x['event_current_capacity'].append(event.event_current_capacity)
                    content_train_x['event_max_capacity'].append(event.event_max_capacity)
                    content_train_y['rating'].append(int(rate.event_score))
                    content_train_x['event_avg_score'].append(event.event_avg_score)
                else:
                    content_test_x['userID'].append(participant.bilkent_id)
                    content_test_items['itemID'].append(event.event_name)
                    content_test_x['enter_year'].append(int(str(participant.bilkent_id)[:3]))
                    content_test_x['club_tags'].append(self.one_hot_encoding(event.club.club_tags))
                    content_test_x['event_tags'].append(self.one_hot_encoding(event.event_tags))
                    content_test_x['event_points'].append(event.event_points)
                    content_test_x['event_current_capacity'].append(event.event_current_capacity)
                    content_test_x['event_max_capacity'].append(event.event_max_capacity)
                    content_test_y['rating'].append(int(rate.event_score))
                    content_test_x['event_avg_score'].append(event.event_avg_score)

        df_train_x = pd.DataFrame(content_train_x)
        df_test_x = pd.DataFrame(content_test_x)
        df_train_y = pd.DataFrame(content_train_y)
        df_test_y = pd.DataFrame(content_test_y)
        df_test_items = pd.DataFrame(content_test_items)
        return df_train_x, df_train_y, df_test_x, df_test_y, df_test_items

    def content_based(self):
        df_train_x, df_train_y, df_test_x, df_test_y, df_test_items = self.create_cb_dataset()
        dtrain = xgb.DMatrix(df_train_x, label=df_train_y, enable_categorical=True) 
        dtest = xgb.DMatrix(df_test_x, enable_categorical=True) 
        xg_cls = xgb.XGBClassifier(max_depth=9, objective='multi:softmax', n_estimators=1000, eval_metric="mlogloss", use_label_encoder=True)
        xg_cls.fit(df_train_x, df_train_y['rating'])
        ypred = xg_cls.predict(df_test_x)
        content_test_y = {'rating': ypred}
        df_pred_y = pd.DataFrame(content_test_y)
        df_test_x['rating'] = ypred
        df_test_x['itemID'] = df_test_items
        return df_test_x
    
    def get_top_n(self, predictions, n=10):
        # First map the predictions to each user.
        top_n = defaultdict(list)
        for uid, iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est))
        # Then sort the predictions for each user and retrieve the k highest ones.
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key=lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]
        return top_n

    def collaborative_filtering(self, df_test_x):
        ratings_train = {'itemID': [],
                        'userID': [],
                        'rating': []}
        ratings_test = {'itemID': [],
                        'userID': [],
                        'rating': []}

        events = list(Event.objects.all())
        for event in events:
            participants = event.participants.all()
            for participant in participants:
                rate = Rate.objects.get(event=event, participant=participant)
                if rate.event_score != 0:
                    ratings_train['itemID'].append(event.event_name)
                    ratings_train['userID'].append(participant.bilkent_id)
                    ratings_train['rating'].append(rate.event_score)
                else:
                    ratings_train['itemID'].append(event.event_name)
                    ratings_train['userID'].append(participant.bilkent_id)
                    ratings_train['rating'].append(df_test_x[(df_test_x['userID'] == participant.bilkent_id) & (df_test_x['itemID'] == event.event_name)]['rating'].values[0])
        
        df_train = pd.DataFrame(ratings_train)
        reader = Reader(rating_scale=(1, 5))

        data_train = Dataset.load_from_df(df_train[['userID', 'itemID', 'rating']], reader)
        kf = KFold(n_splits=3)
        algo = SVD()

        for trainset, validset in kf.split(data_train):
            algo.fit(trainset)
            predictions = algo.test(validset)
        
        top_n = self.get_top_n(predictions, n=10)
        return top_n

    def handle(self, *args, **options):
        df_test_x = self.content_based()
        top_n = self.collaborative_filtering(df_test_x)
        recommended_list = ""
        for uid, user_ratings in top_n.items():
            for iid, _ in user_ratings:
                recommended_list += str(uid) + "," + str(iid) + ","
        return recommended_list


