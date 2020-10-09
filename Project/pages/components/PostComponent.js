import React, { Component } from "react";
import { StyleSheet, View, Image, Text, TouchableOpacity } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

function PostComponent(props) {
  return (
    <View style={[styles.container, props.style]}>
      <View style={styles.postWrapper}>
        <View style={styles.postHeader}>
          <Image
            source={require("../assets/IEEE.jpg")}
            resizeMode="cover"
            style={styles.image}
          ></Image>
          <View style={styles.headerGroup}>
            <View style={styles.ieeeStack}>
              <Text style={styles.ieee}>{props.Subreddit || "IEEE"}</Text>
              <Text style={styles.postDetails}>{props.text5 || "09.10.2020• 14h"}</Text>
            </View>
          </View>
          <Icon name="dots-vertical" style={styles.moreIcon}></Icon>
          <Text style={styles.event}>
            Event :{"\n"}Time :{"\n"}Place :{"\n"}Capacity:{"\n"}GE 250/251
            Points :
          </Text>
        </View>
        <View style={styles.actionBar}>
          <View style={styles.likeRow}>
            <TouchableOpacity style={styles.like}></TouchableOpacity>
            <TouchableOpacity style={styles.dislike}></TouchableOpacity>
            <Text style={styles.loremIpsum}>3.5k</Text>
            <TouchableOpacity style={styles.share}></TouchableOpacity>
          </View>
        </View>
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
  postWrapper: {
    height: 217,
    alignItems: "flex-start",
    alignSelf: "stretch",
    justifyContent: "space-around",
    marginTop: 0,
    margin: 0,
    shadowColor: "rgba(0,0,0,1)",
    shadowOffset: {
      height: 0,
      width: 3
    },
    elevation: 5,
    shadowOpacity: 0.01,
    shadowRadius: 0
  },
  postHeader: {
    width: 318,
    height: 131,
    flexDirection: "row",
    alignSelf: "center",
    justifyContent: "space-between",
    marginRight: 0,
    marginLeft: 0,
    left: 25,
    top: -5,
    backgroundColor: "rgba(15,15, 15,0)"
  },
  image: {
    width: 30,
    height: 30,
    borderRadius: 100
  },
  headerGroup: {
    width: 250,
    height: 27,
    left: 44,
    top: 0
  },
  ieee: {
    top: 0,
    left: 0,
    color: "rgba(255,255,255,1)",
    position: "absolute",
    fontSize: 14,
    letterSpacing: 1
  },
  postDetails: {
    top: 15,
    left: 0,
    color: "rgba(255,255,255,1)",
    position: "absolute",
    fontSize: 12,
    letterSpacing: 1
  },
  ieeeStack: {
    width: 34,
    height: 30
  },
  moreIcon: {
    color: "grey",
    fontSize: 18,
    left: 283,
    width: 18,
    top: 0,
    height: 19
  },
  event: {
    top: 37,
    left: 9,
    position: "absolute",
    color: "rgba(255,255,255,1)",
    height: 105,
    width: 260
  },
  actionBar: {
    width: 314,
    height: 53,
    flexDirection: "row",
    alignItems: "center",
    alignSelf: "center",
    justifyContent: "space-between",
    marginRight: 0,
    marginLeft: 0,
    left: 0,
    top: 128
  },
  like: {
    width: 34,
    height: 32,
    backgroundColor: "#E6E6E6"
  },
  dislike: {
    width: 35,
    height: 32,
    backgroundColor: "#E6E6E6",
    marginLeft: 14
  },
  loremIpsum: {
    color: "rgba(255,255,255,1)",
    height: 22,
    width: 73,
    fontSize: 16,
    marginLeft: 13,
    marginTop: 5
  },
  share: {
    width: 59,
    height: 32,
    backgroundColor: "#E6E6E6",
    marginLeft: 57
  },
  likeRow: {
    height: 32,
    flexDirection: "row",
    flex: 1,
    marginRight: 17,
    marginLeft: 12,
    marginTop: 10
  }
});

export default PostComponent;
