import React, { useState } from "react";
import { StyleSheet, View, StatusBar,TouchableOpacity,TextInput,Button,Dimensions,Platform, Image, Text} from "react-native";
import Footer from "./components/Footer";
import DatePicker from 'react-native-datepicker';

const { width, height } = Dimensions.get('window');

class AddEventPage extends React.Component {
  state={
    name:"",
    place:"",   
    date:"",
    time:"",     
    GEPoint:0, 
    maxCapacity:0,
    tags:"",
    zoomLink:"",
    club: this.props.route.params.club,
    eventTags:  this.props.route.params.clubTag,   
    select:"",
    logoUrl: this.props.route.params.logo        
  }

  async postEvent(state){
    const url = await "https://bileventsapp.herokuapp.com/viewset/events";
    console.log(new Date(state.date+"T"+state.time+":00"));
    const response = await fetch(url, { 
      method: "POST", 
      headers: { 
        'Accept': 'application/json', 
        'Content-Type': 'application/json' 
      },
      body: JSON.stringify({ 
        "event_name": state.name,
        "event_place":state.place,
        "event_time":new Date(state.date+"T"+state.time+":00"),
        "event_points":state.GEPoint,
        "event_max_capacity":state.maxCapacity,
        "event_tags": state.eventTags,
        "event_description":" ",
        "club": state.club,
        "event_zoom_link":state.zoomLink,
      }) 
    });
    if(response.status == 200)
      console.log("eklendi");
    else
      console.log(response.status);
  }

  render(){  
    let Image_Http_URL ={ uri: this.state.logoUrl}; 
    var now = new Date().toJSON().toString().substring(0,10);
    return (
      
      <View style={styles.container}>
        <StatusBar
          animated
          barStyle="dark-content"
          backgroundColor="rgba(255,255,255,1)"
        />
      
        <View style={styles.container1} >
          <View >            
            <Image source={Image_Http_URL} style={styles.logo} />
            <View style={styles.inputView} >
                <TextInput style={styles.inputText} placeholder="Event Name" placeholderTextColor="white" onChangeText={text => this.setState({name:text})}/>
            </View>
            <DatePicker
              style={{width: 250,marginBottom: 10,}}
              date={this.state.date}
              mode="date"
              format="YYYY-MM-DD"
              minDate={now}
              maxDate="2021-06-01"
              placeholder="Select date"
              confirmBtnText="Confirm"
              cancelBtnText="Cancel"              
              customStyles={{
                dateIcon: {
                  position: 'absolute',
                  left: 0,
                  top: 4,
                  marginLeft: 0,
                },
                dateInput: {
                  marginLeft: 40,
                }
              }}
              onDateChange={(date) => {this.setState({date: date})}}              
            />
            
            <View style={styles.inputView} >
                <TextInput style={styles.inputText} placeholder="Event Time(00:00)" placeholderTextColor="white" onChangeText={text => this.setState({time:text})}/>
            </View>
            <View style={styles.inputView} >
                <TextInput style={styles.inputText} placeholder="Event Place" placeholderTextColor="white" onChangeText={text => this.setState({place:text})}/>
            </View>
            <View style={styles.inputView} >
                <TextInput style={styles.inputText}
                keyboardType= "number-pad"
                maxLength={3}                 
                placeholder="Event Capacity" 
                placeholderTextColor="white" 
                onChangeText={text => this.setState({maxCapacity:text})}/>
            </View>
            <View style={styles.inputView} >
                <TextInput style={styles.inputText} 
                keyboardType= "number-pad"
                maxLength={2}
                placeholder="GE 250/251 Points" 
                placeholderTextColor="white" 
                onChangeText={text => this.setState({GEPoint:text})}/>
            </View>
            <TouchableOpacity style={styles.loginBtn} onPress = {() =>{this.postEvent(this.state)}}>
                <Text style={{color:'white'}} >Add Event</Text>
            </TouchableOpacity>
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
    backgroundColor: "rgba(234,226,226,1)",
  },
  container1: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
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
  loginBtn:{
    width:150,
    backgroundColor:"#fb5b5a",
    borderRadius:25,
    height:'20%',
    alignItems:'center',
    justifyContent:'center',
    marginTop:'2%',
    marginBottom: '10%',
    marginLeft:'10%'
  },
  inputView:{
    width:250,
    backgroundColor:"#465881",
    height:'5%',
    marginBottom:'2.5%',
    justifyContent:"center",
    padding:20
  },
  inputText:{
    height:40,
    color:"white"
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
    marginBottom: 1,
    alignItems:"center",
  },
  footer: {
    height: 50
  },
  logo: {
    width: width * 0.4,
    height: height * 0.2,
    marginLeft:'8%'
  },
});

export default AddEventPage;
