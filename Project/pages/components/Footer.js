import React from "react";
import { StyleSheet, View, TouchableOpacity } from "react-native";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";
import IoniconsIcon from "react-native-vector-icons/Ionicons";
import { useNavigation } from '@react-navigation/native';
import EntypoIcon from "react-native-vector-icons/Entypo";

function Footer(props) {
  const navigation = useNavigation();
  return (
    <View style={[styles.container, styles.property]}>
      <TouchableOpacity style={styles.button3} onPress={() => { navigation.navigate('Homepage',{userID: props.bilkent_id,club : props.club,clubTag :props.clubTag,logo:props.logo})}}>
        <MaterialCommunityIconsIcon name="home" style={styles.icon3}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => { navigation.navigate('SelectedEvents',{userID: props.bilkent_id,club : props.club,clubTag :props.clubTag,logo:props.logo})}} >
        <MaterialCommunityIconsIcon name="heart" style={styles.icon6}></MaterialCommunityIconsIcon>
      </TouchableOpacity>
      
      <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('RecommendedEvents',{userID: props.bilkent_id,club : props.club,clubTag :props.clubTag,logo:props.logo})}  >
        <MaterialCommunityIconsIcon name="checkbox-multiple-marked-outline" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('PastEventsPage',{userID: props.bilkent_id,club : props.club,clubTag :props.clubTag,logo:props.logo})}  >
        <MaterialCommunityIconsIcon name="content-save" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button4} onPress={() => navigation.navigate('ClubList',{userID: props.bilkent_id,club : props.club,clubTag :props.clubTag,logo:props.logo})}>
        <IoniconsIcon name="logo-github" style={styles.icon4}></IoniconsIcon>
      </TouchableOpacity>

      {props.club != "" ?
      <TouchableOpacity style={styles.button2} onPress={() => navigation.navigate('AddEventPage',{userID: props.bilkent_id, club : props.club,clubTag :props.clubTag,logo:props.logo})}  >
        <MaterialCommunityIconsIcon name="plus" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>
      :null}

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
