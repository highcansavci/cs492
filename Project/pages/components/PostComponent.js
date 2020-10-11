import React, { Component } from "react";
import { StyleSheet, View, Image, Text, TouchableOpacity } from "react-native";
import Icon from "react-native-vector-icons/Entypo";

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
        <Icon name="dots-three-vertical" style={styles.icon}></Icon>
      </View>
      <View style={styles.eventStack}>
        <Text style={styles.event}></Text>
        <Text style={styles.event8}>Event :</Text>
      </View>
      <Text style={styles.time}>Time :</Text>
      <Text style={styles.place}>Place :</Text>
      <Text style={styles.capacity}>Capacity :</Text>
      <Text style={styles.ge250251Points}>GE 250/251 Points :</Text>
      <View style={styles.buttonRow}>
        <TouchableOpacity style={styles.button}></TouchableOpacity>
        <Text style={styles.loremIpsum6}>3.5 k</Text>
        <TouchableOpacity style={styles.button2}></TouchableOpacity>
        <Text style={styles.text}>3.5 k</Text>
        <TouchableOpacity style={styles.button3}></TouchableOpacity>
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
  icon: {
    color: "rgba(255,255,255,1)",
    fontSize: 23,
    marginLeft: 24,
    marginTop: 4
  },
  imageRow: {
    height: 53,
    flexDirection: "row",
    marginTop: 5,
    marginLeft: 8,
    marginRight: 2
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
    height: 18,
    width: 302,
    marginTop: 8,
    marginLeft: 8
  },
  button: {
    width: 28,
    height: 28,
    backgroundColor: "#E6E6E6"
  },
  loremIpsum6: {
    color: "rgba(255,255,255,1)",
    width: 43,
    height: 14,
    marginLeft: 8,
    marginTop: 6
  },
  button2: {
    width: 29,
    height: 26,
    backgroundColor: "#E6E6E6",
    marginLeft: 5
  },
  text: {
    color: "rgba(255,255,255,1)",
    width: 47,
    height: 12,
    marginLeft: 5,
    marginTop: 6
  },
  button3: {
    width: 70,
    height: 27,
    backgroundColor: "#E6E6E6",
    marginLeft: 45
  },
  buttonRow: {
    height: 28,
    flexDirection: "row",
    marginTop: 14,
    marginLeft: 15,
    marginRight: 31
  }
});

export default PostComponent;
