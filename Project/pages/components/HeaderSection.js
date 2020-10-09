import React, { Component } from "react";
import { StyleSheet, View, TextInput,TouchableHighlight } from "react-native";
import Icon from "react-native-vector-icons/EvilIcons";

function HeaderSection(props) {
  return (
    <View style={[styles.container, props.style]}>
      <View style={styles.searchHeader}>
        <TouchableHighlight onPress={()=>console.log("Search")}>
          <View>
            <Icon name="search" style={styles.searchIcon}></Icon>
          </View>
        </TouchableHighlight>
        <TextInput placeholder="Search" style={styles.searchInput}></TextInput>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {},
  searchHeader: {
    height: 40,
    backgroundColor: "#1a1a1c",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "flex-start",
    borderRadius: 10,
    marginTop: 1,
    marginLeft: 9,
    marginRight: 4
  },
  searchIcon: {
    color: "white",
    fontSize: 35,
    marginLeft: 5,
    marginRight: 1
  },
  searchInput: {
    width: 239,
    height: 40,
    color: "rgba(255,255,255,1)",
    marginRight: 1,
    marginLeft: 5,
    fontSize: 14,
  }
});

export default HeaderSection;
