import React, { Component } from "react";
import { StyleSheet, View, StatusBar, Image, Text,ScrollView} from "react-native";
import HeaderSection from "./components/HeaderSection";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";
import IoniconsIcon from "react-native-vector-icons/Ionicons";
import Divider from "./components/Divider";
import PostComponent from "./components/PostComponent";
import Footer from "./components/Footer";
import DropDownPicker from 'react-native-dropdown-picker';

function myFunction(datetime) {
  var date = new Date(datetime);
  var now = new Date();
  var ms = now - date;
  var days = -1 * Math.floor(ms / (24 * 60 * 60 * 1000));
  var daysms=ms % (24 * 60 * 60 * 1000);
  var hours = -1 * Math.floor((daysms)/(60 * 60 * 1000));
  return days;
}

function fixData(date){
  date = date.substring(8,10)+ "."+date.substring(5,7)+"."+date.substring(0,4)
  return date;
}
const setPostComponents = (id,stateData) => {
  if(null == stateData || undefined == stateData)
    return;

  if(stateData.isLoading)
    return (<Text>Loaging.....</Text>)

  else if(stateData.isError)
    return (<Text>An error has occured!</Text>)

  else if (null != stateData.data && undefined != stateData.data && stateData.data.length > 0)
    return stateData.data.map(i => (           
        <PostComponent
          key = {i.id}
          clubName={i.club.club_name}
          dateTime={fixData(i.event_time.substring(0,10))}
          postAgo={myFunction(i.event_time)}
          eventName={i.event_name}
          time={i.event_time.substring(11,16)}
          place={i.event_place}
          capacity={i.event_max_capacity}
          gePoints={i.event_points}
          logo = {i.club.logo}
          eventPage = "recommendedEvents"
          participantID = {id}
        />  
    ));    
}
class RecommendedEvents extends React.Component {
  state={
    isLoading : false,
    data:[],
    isError: false,
    select:'',
  }
  
  async componentDidMount () {    
    try{
      let response = await fetch('https://bileventsapp.herokuapp.com/viewset/participants/'+this.props.route.params.userID+'/recommended_events');

      if(null === response || undefined === response){
        this.setState({
          isLoading : false,
          data:[],
          isError: false
        })
        return;
      }

      let jsonData = await response.json();

      if(null === jsonData || undefined === jsonData ){
        this.setState({
          isLoading : false,
          data:[],
          isError: true
        })
      }
      this.setState({
        isLoading : false,
        data:jsonData,
        isError: false
      })
    }catch(err){
      this.state={
        isLoading : false,
        data:[],
        isError: false
      }
      console.error(error);
    }
  }

  render(){
    return ( 
        
      <View style={styles.container}>
        <StatusBar
          animated
          barStyle="dark-content"
          backgroundColor="rgba(255,255,255,1)"
        />
        <View style={styles.headerTabsColumn}>
          <View style={styles.headerSectionRow}>
            <HeaderSection style={styles.headerSection}></HeaderSection>
            <View style={styles.layoutOptions}>
              <View style={styles.rect}></View>
              <View style={styles.rect2}></View>
                   
              <DropDownPicker 
                  items={[         
                    {label: 'IN A WEEK', value: 'week', selected: true},
                    {label: 'IN A MONTH', value: 'month'},                    
                    {label: 'IN A SEMESTER', value: 'semester'},
                  ]}
                  containerStyle={{height: '100%', width: '90%'}}
                  style={{backgroundColor: '#fafafa', marginBottom: 10}}
                  itemStyle={{justifyContent: 'flex-start'}}
                  dropDownStyle={{backgroundColor: '#fafafa'}}
                  onChangeItem={item => this.setState({select: item.value })} 
                >
              </DropDownPicker>
            </View>
          </View>
        </View>
        <View style={styles.dividerStack}>
          <Divider style={styles.divider}></Divider>
          <View style={styles.scrollArea}>
            <ScrollView horizontal={false} contentContainerStyle={styles.scrollArea_contentContainerStyle}> 
            {setPostComponents(this.props.route.params.userID,this.state)}
            </ScrollView>
          </View>
        </View>
        <Footer bilkent_id={this.props.route.params.userID} club={this.props.route.params.club} clubTag = {this.props.route.params.clubTag} logo={this.props.route.params.logo}></Footer>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "rgba(234,226,226,1)"
  },
  headerTabs: {
    height: 76,
    backgroundColor: "rgba(70,88,129,1)",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center"
  },
  image: {
    top: 6,
    left: 10,
    width: 97,
    height: 66,
    position: "absolute"
  },
  homeTab: {
    width: 144,
    height: 46,
    borderColor: "#026bbd",
    borderWidth: 0
  },
  upcomingEvents: {
    color: "rgba(255,255,255,1)",
    fontSize: 16,
    lineHeight: 0,
    letterSpacing: 0,
    marginTop: 21,
    marginLeft: 15
  },
  headerSection: {
    height: 46,
    flex: 1,
    marginTop: 3
  },
  layoutOptions: {
    height: 52,
    flexDirection: "row",
    flex: 1
  },
  rect: {},
  rect2: {},
  bestPostIcon: {
    left: 15,
    position: "absolute",
    color: "rgba(0,0,0,1)",
    fontSize: 20,
    top: 13
  },
  inAWeek: {
    left: 40,
    color: "rgba(0,0,0,1)",
    position: "absolute",
    fontSize: 14,
    letterSpacing: 1,
    top: 15
  },
  dropdownIcon: {
    left: 128,
    position: "absolute",
    color: "rgba(0,0,0,1)",
    fontSize: 36,
    top: 6
  },
  headerSectionRow: {
    height: 52,
    flexDirection: "row"
  },
  headerTabsColumn: {
    marginTop: 24
  },
  divider: {
    top: 0,
    left: 0,
    width: 360,
    height: 2,
    position: "absolute"
  },
  scrollArea: {
    top: 0,
    left: 0,
    backgroundColor: "rgba(255,255,255,1)",
    position: "absolute",
    right: 0,
    bottom: 0
  },
  scrollArea_contentContainerStyle: {
    height :"auto",
    justifyContent: "flex-start",
    overflow: "hidden"
  },
  postComponent: {
    height: "100%",
    alignSelf:"stretch",
  },
  dividerStack: {
    flex: 1,
    marginBottom: 1
  },
  footer: {
    height: 50
  }
});

export default RecommendedEvents;
