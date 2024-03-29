import React, { Component } from "react";
import { StyleSheet, View, Image,Alert , Text,TouchableHighlight } from "react-native";
import EntypoIcon from "react-native-vector-icons/Entypo";
import EvilIconsIcon from "react-native-vector-icons/EvilIcons";
const createAlert = (title,msg) =>
    Alert.alert(
      title,
      msg,
      [
        { text: "OK" }
      ]
    );

function propsDescription(input){
  return <Text style={ styles.descript }> {input} </Text>;
}

function ClubComponent(props) {
  return (
    <View style={[styles.container, props.style]}>
      <View style={styles.imageRow}>
        <Image source={{ uri:props.logo}} resizeMode="contain" style={styles.image}></Image>
        <View style={styles.ieeeStackColumn}>
          <View style={styles.ieeeStack}>
            <Text style={styles.ieee}>{props.club_name}</Text>
          </View>          
        </View>
      </View>
      <View style={styles.eventStack}>
        <Text style={styles.event}></Text>
        <Text style={styles.event8}>Club Leader : {props.leader}</Text>
      </View>
      <View>
        <Text style={styles.time} onPress={()=> createAlert("Description",props.description)}>Description :{ propsDescription(props.description)}</Text>
      </View>
      <Text style={styles.capacity} >Tags :  {props.tag}</Text>
      <View style={styles.iconRow}>
        
      </View>
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
    width: 39,
    marginLeft: 4
  },
  loremIpsumRow: {
    height: 24,
    flexDirection: "row",
    marginTop: 5,
    marginRight: 92
  },
  ieeeStackColumn: {
    width: 209,
    marginLeft: 17
  },
  imageRow: {
    height: 53,
    flexDirection: "row",
    marginTop: 5,
    marginLeft: 8,
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
    color: "#ebde34",
    height: 19,
    width: 302,
    marginTop: 5,
    marginLeft: 8,
  },
  descript:
  {
    color:"white"
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
    color: "grey",
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
    height: 44,
    flexDirection: "row",
    marginLeft: 8,
    marginRight: 16
  }
});

export default ClubComponent;
