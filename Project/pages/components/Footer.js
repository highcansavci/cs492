import React, { Component } from "react";
import { StyleSheet, View, TouchableOpacity } from "react-native";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";
import FontAwesomeIcon from "react-native-vector-icons/FontAwesome";
import IoniconsIcon from "react-native-vector-icons/Ionicons";

function Footer(props) {
  return (
    <View style={[styles.container, props.style]}>
      <TouchableOpacity style={styles.button3} onPress={() => console.log("Navigate to Upcoming Events")}>
        <MaterialCommunityIconsIcon name="home" style={styles.icon3}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => console.log("Navigate to Selected Events")} >
        <MaterialCommunityIconsIcon name="heart" style={styles.icon6}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button2} onPress={() => console.log("Navigate to Recommended Events")} >
        <MaterialCommunityIconsIcon name="checkbox-multiple-marked-outline" style={styles.icon7}></MaterialCommunityIconsIcon>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button4} onPress={() => console.log("Navigate to Clup List")}>
        <IoniconsIcon name="logo-github" style={styles.icon4}></IoniconsIcon>
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
    color: "grey",
    fontSize: 28
  },
  icon6: {
    color: "grey",
    fontSize: 28
  },
  button2: {
    width: 28,
    height: 28
  },
  icon7: {
    color: "grey",
    fontSize: 28
  },
  button4: {
    width: 28,
    height: 28,
    justifyContent: "center"
  },
  icon4: {
    color: "rgba(128,128,128,1)",
    fontSize: 28,
    alignSelf: "center"
  }
});

export default Footer;
