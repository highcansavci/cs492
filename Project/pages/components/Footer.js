import React, { Component } from "react";
import { StyleSheet, View, TouchableOpacity } from "react-native";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";
import FontAwesomeIcon from "react-native-vector-icons/FontAwesome";
import IoniconsIcon from "react-native-vector-icons/Ionicons";
import { useNavigation } from '@react-navigation/native';
import EntypoIcon from "react-native-vector-icons/Entypo";

function checkLeader(leader){
  if (leader) {
    <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('AddEventPage',{userID: props.bilkent_id})}  >
        <MaterialCommunityIconsIcon name="plus" style={styles.icon7}></MaterialCommunityIconsIcon>
    </TouchableOpacity>
  }
}
function Footer(props) {
  const navigation = useNavigation();
  return (
    <View style={[styles.container, styles.property]}>
      <TouchableOpacity style={styles.button3} onPress={() => { navigation.navigate('Homepage',{userID: props.bilkent_id})}}>
        <MaterialCommunityIconsIcon name="home" style={styles.icon3}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => { navigation.navigate('SelectedEvents',{userID: props.bilkent_id})}} >
        <MaterialCommunityIconsIcon name="heart" style={styles.icon6}></MaterialCommunityIconsIcon>
      </TouchableOpacity>
      
      <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('RecommendedEvents',{userID: props.bilkent_id})}  >
        <MaterialCommunityIconsIcon name="checkbox-multiple-marked-outline" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('PastEvents',{userID: props.bilkent_id})}  >
        <MaterialCommunityIconsIcon name="content-save" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button4} onPress={() => navigation.navigate('ClubList',{userID: props.bilkent_id})}>
        <IoniconsIcon name="logo-github" style={styles.icon4}></IoniconsIcon>
      </TouchableOpacity>

      {checkLeader(props.leader)}

      <TouchableOpacity style={styles.button4} onPress={() => navigation.navigate('Login')}>
        <EntypoIcon name="log-out" style={styles.icon8}></EntypoIcon>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "rgba(0,0,0,1)",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-around"
  },
  button3: {
    width: 28,
    height: 28,
    justifyContent: "center"
  },
  icon3: {
    color: "white",
    fontSize: 28
  },
  icon6: {
    color: "white",
    fontSize: 28
  },
  button2: {
    width: 28,
    height: 28
  },
  icon7: {
    color: "white",
    fontSize: 28
  }, 
  icon8: {
    color: "white",
    fontSize: 28
  },
  button4: {
    width: 28,
    height: 28,
    justifyContent: "center"
  },
  icon4: {
    color: "white",
    fontSize: 28,
    alignSelf: "center"
  },
  property: {
    height: 50
  },
});

export default Footer;
