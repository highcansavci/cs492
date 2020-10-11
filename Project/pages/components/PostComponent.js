import React, { Component } from "react";
import { StyleSheet, View, Image, Text,TouchableHighlight } from "react-native";
import EntypoIcon from "react-native-vector-icons/Entypo";
import EvilIconsIcon from "react-native-vector-icons/EvilIcons";

function PostComponent(props) {
  return (
    <View style={[styles.container, props.style]}>
      <View style={styles.imageRow}>
        <Image
          source={require("../assets/IEEE.jpg")}
          resizeMode="contain"
          style={styles.image}
        ></Image>
        <View style={styles.ieeeStackColumn}>
          <View style={styles.ieeeStack}>
            <Text style={styles.ieee}>IEEE</Text>
            <Text style={styles.loremIpsum5}></Text>
          </View>
          <View style={styles.loremIpsumRow}>
            <Text style={styles.loremIpsum}>09.10.2020</Text>
            <Text style={styles.loremIpsum4}>• 14h</Text>
          </View>
        </View>
      </View>
      <View style={styles.eventStack}>
        <Text style={styles.event}></Text>
        <Text style={styles.event8}>Event :</Text>
      </View>
      <Text style={styles.time}>Time :</Text>
      <Text style={styles.place}>Place :</Text>
      <Text style={styles.capacity}>Capacity :</Text>
      <Text style={styles.ge250251Points}>GE 250/251 Points :</Text>
      <View style={styles.iconRow}>
        <TouchableHighlight onPress={()=>console.log("Join")}>
            <View>
              <EntypoIcon name="add-user" style={styles.icon}></EntypoIcon>
            </View>
        </TouchableHighlight>
        <TouchableHighlight onPress={()=>console.log("Leave")}>
          <View>
            <EntypoIcon name="remove-user" style={styles.icon2}></EntypoIcon>
          </View>
        </TouchableHighlight>
        <TouchableHighlight onPress={()=>console.log("Share")}>
          <View>
            <EvilIconsIcon name="share-google" style={styles.icon3}></EvilIconsIcon>
          </View>
        </TouchableHighlight>
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
    height: 24
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
    color: "rgba(255,255,255,1)",
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

export default PostComponent;
