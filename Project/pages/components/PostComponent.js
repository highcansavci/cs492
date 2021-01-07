import React from "react";
import { StyleSheet, View, Image,Dimensions, Text,TouchableHighlight } from "react-native";
import EntypoIcon from "react-native-vector-icons/Entypo";
import EvilIconsIcon from "react-native-vector-icons/EvilIcons";
import { Rating, AirbnbRating } from 'react-native-ratings';
const { width, height } = Dimensions.get('window');

function checkingGEPoints(point){
  if(point ==0)
    return "No Points Will Be Given"
  else
    return point
}
function checkingCapacity(point){
  if(point ==0)
    return "No Limit"
  else
    return point
}
async function joinEvent(bilkent_id,eventName) { 
  const url = "https://bileventsapp.herokuapp.com/viewset/participants/"+bilkent_id+"/selected_events";
  const response = await fetch(url, { 
    method: "PUT", 
    headers: { 
      'Accept': 'application/json', 
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify({ 
      event_name: eventName
    }) 
  });
  if(response.status == "400")
  {
    alert("Unsuccessful");
  }
  else if(response.status == "409"){
    alert("You have already added that event." );
  }
  else{
    alert("Added Successfully" );
  }
}

async function leaveEvent(bilkent_id,eventName){
  const url = "https://bileventsapp.herokuapp.com/viewset/participants/"+bilkent_id+"/selected_events";
  const response = await fetch(url, { 
    method: "DELETE", 
    headers: { 
      'Accept': 'application/json', 
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify({ 
      event_name: eventName
    }) 
  });
  if(response.status == "400")
  {
    alert("Unsuccessful");
  }
  if(response.status == "404")
  {
    return;
  }
  else{
    alert("Deleted Successfully" );
  }
}
function addZoomButton(eventPage)
{
  if(eventPage != "pastEvents")
  return <TouchableHighlight onPress={()=>console.log("share")}>
          <View>
            <EvilIconsIcon name="share-google" style={styles.icon3}></EvilIconsIcon>
          </View>
        </TouchableHighlight>
}


function calculateDay(day) {
  if(day == -1)
    return "Yesterday";
  if(day == 0)
    return "Today";
  else if(day<-1)
    if(parseInt((-1*day)/30) > 0)
      return parseInt((-1*day)/30)+"M "+(-1*day)%30+"d Ago";
    else
      return (-1*day)+"d Ago";
  else
    if(day>0 &&day<=29)
      return day+"d Left";
    else
      if(day%30 ==0)
      return day%30+"M Left";
      else if(day%30 > 1 && day%30 <= 29)
        return parseInt(day/30)+"M "+day%30+"d Left";
}

function PostComponent(props){

  function ratingCompleted(rating) {
    
  }

  function checkEventPage(eventPage,eventName,bilkent_id){
    if(eventPage == "selectedEvents")
      return <View style={styles.iconRow2}>                
                <TouchableHighlight onPress={()=>leaveEvent(bilkent_id,eventName)}>
                  <View>
                    <EntypoIcon name="remove-user" style={styles.icon2}></EntypoIcon>
                  </View>
                </TouchableHighlight>
                {addZoomButton(props.eventPage)}
             </View>
    else if(eventPage == "upcomingEvents" || eventPage == "recommendedEvents" )
      return <View style={styles.iconRow2}>
              <TouchableHighlight onPress={()=>joinEvent(bilkent_id,eventName)}>
                <View>
                  <EntypoIcon name="add-user" style={styles.icon}></EntypoIcon>
                </View>
              </TouchableHighlight>
              
              {addZoomButton(props.eventPage)}
            </View>
      
    else if(eventPage == "pastEvents")
      return  <View style={styles.iconRow}>
                <AirbnbRating
                  count={5}
                  reviews={["Terrible", "Bad", "Neutral", "Good", "Very Good"]}
                  defaultRating={5}
                  onFinishRating = {ratingCompleted}
                  size={20}
                  />
              </View>
  }
    return (
    <View style={[styles.container, props.style]}>
      <View style={styles.imageRow}>
        <Image
          source={{ uri:props.logo}}
          resizeMode="contain"
          style={styles.image}
        ></Image>
        <View style={styles.ieeeStackColumn}>
          <View style={styles.ieeeStack}>
            <Text style={styles.ieee}>{props.clubName}</Text>
          </View>
          <View style={styles.loremIpsumRow}>
         
            <Text style={styles.loremIpsum}>{props.dateTime} </Text>
            <Text style={styles.loremIpsum4}>• {calculateDay(props.postAgo)}</Text>
          </View>
        </View>
      </View>
      <View style={styles.eventStack}>
        <Text style={styles.event}></Text>
        <Text style={styles.event8}>Event : {props.eventName}</Text>
      </View>
      <Text style={styles.time}>Time : {props.time}</Text>
      <Text style={styles.place}>Place : {props.place}</Text>
      <Text style={styles.capacity}>Capacity : {checkingCapacity(props.capacity)}</Text>
      <Text style={styles.ge250251Points}>GE 250/251 Points : {checkingGEPoints(props.gePoints)}</Text>
        {checkEventPage(props.eventPage,props.eventName,props.participantID)}
        
    </View>
  );

}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "rgba(70,88,129,1)",
    alignItems: "center",
    justifyContent: "space-around",
    shadowColor: "rgba(0,0,0,1)",
    shadowOffset: {
      height: 0,
      width: 0
    },
    elevation: 5,
    shadowOpacity: 0.01,
    shadowRadius: 0,
    borderWidth: 1,
    borderColor: "rgba(255,255,255,1)"
  },
  image: {
    width: 43,
    height: 49
  },
  ieee: {
    top: 0,
    left: 0,
    position: "absolute",
    color: "rgba(255,255,255,1)",
    fontSize: 19,
    width: 209,
    height: "100%"
  },
  loremIpsum5: {
    top: 12,
    left: 117,
    position: "absolute",
    color: "#121212"
  },
  ieeeStack: {
    width: 209,
    height: 24
  },
  loremIpsum: {
    color: "rgba(255,255,255,1)",
    width: 74,
    height: 24
  },
  loremIpsum4: {
    color: "rgba(255,255,255,1)",
    height: 18,
    width: 100,
    marginLeft: 4
  },
  loremIpsumRow: {
    height: 24,
    flexDirection: "row",
    marginTop: 5,
    marginRight: 92
  },
  ieeeStackColumn: {
    width: width *0.6,
    marginLeft: 17
  },
  imageRow: {
    height: 53,
    flexDirection: "row",
    marginTop: 5,
    marginLeft: width *0.14,
    marginRight: 49
  },
  event: {
    top: 9,
    left: 15,
    position: "absolute",
    color: "#121212"
  },
  event8: {
    top: 0,
    position: "absolute",
    color: "rgba(255,255,255,1)",
    height: 19,
    width: 302,
    left: 0
  },
  eventStack: {
    width: 302,
    height: 19,
    marginTop: 9,
    marginLeft: 8
  },
  time: {
    color: "rgba(255,255,255,1)",
    height: 19,
    width: 302,
    marginTop: 5,
    marginLeft: 8
  },
  place: {
    color: "rgba(255,255,255,1)",
    height: 19,
    width: 302,
    marginTop: 5,
    marginLeft: 8
  },
  capacity: {
    color: "rgba(255,255,255,1)",
    height: 19,
    width: 302,
    marginTop: 6,
    marginLeft: 8
  },
  ge250251Points: {
    color: "rgba(255,255,255,1)",
    height: 19,
    width: 302,
    marginTop: 8,
    marginLeft: 8
  },
  icon: {
    color: "rgba(255,255,255,1)",
    fontSize: 27,
    marginTop: 7
  },
  icon2: {
    color: "red",
    fontSize: 27,
    marginLeft: 16,
    marginTop: 7
  },
  icon3: {
    color: "rgba(255,255,255,1)",
    fontSize: 40,
    marginLeft: 192
  },
  iconRow: {
    height: height*0.13,
    flexDirection: "row",
    marginLeft: 8,
    marginRight: 16,
    marginBottom:10
  },
  iconRow2: {
    flexDirection: "row",
    marginLeft: 8,
    marginRight: 16,
    
    marginBottom:10
  }
});

export default PostComponent;
