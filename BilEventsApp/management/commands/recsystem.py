import pandas as pd
import numpy as np  
import xgboost as xgb
from surprise import SVD, Dataset, accuracy, BaselineOnly, Reader
from surprise.model_selection import train_test_split, cross_validate
from django.core.management.base import BaseCommand
from BilEventsApp.models import Event


class Command(BaseCommand):

    help = 'Execute the recommender engine.'  

    def content_based(self):
        pass 

    def collaborative_filtering(self):
        # Load the movielens-100k dataset (download it if needed),
        ratings_dict = {'itemID': [],
                        'userID': [],
                        'rating': []}
        events = Event.objects.all().values_list('event_name', flat=True)
        print(events)
        df = pd.DataFrame(ratings_dict)

        # A reader is still needed but only the rating_scale param is requiered.
        reader = Reader(rating_scale=(1, 5))

        # The columns must correspond to user id, item id and ratings (in that order).
        data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)

        # sample random trainset and testset
        # test set is made of 25% of the ratings.
        trainset, testset = train_test_split(data, test_size=.05)

        # We'll use the famous SVD algorithm.
        algo = SVD()

        # Train the algorithm on the trainset, and predict ratings for the testset
        algo.fit(trainset)
        predictions = algo.test(testset)

        # Then compute RMSE
        accuracy.rmse(predictions)
        return predictions

    def handle(self, *args, **options):
        print(self.collaborative_filtering())

