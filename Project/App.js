import { StatusBar } from 'expo-status-bar';
import React,{Component} from 'react';
import { SafeAreaView,StyleSheet, Text, View, Image, TextInput,Button } from 'react-native';
import { render } from 'react-dom';

export default function App() {
  
    return (
      <SafeAreaView style={styles.container}>
        <SafeAreaView  style={styles.container}>
          <Image source={require('./assets/logo.png')} style={styles.logo} /> 
          <Text style={styles.title} >Bil-Events</Text>
          <TextInput style={styles.idPass} placeholder={'ID'} />
          <TextInput style={styles.idPass} placeholder={'Password'} secureTextEntry={true}/>
        </SafeAreaView >
        
        <SafeAreaView  style={styles.container2}>
          <Button title = "   Log In   " style={styles.button} onPress = {() =>console.log("login tabbed")}/>
          <Button title = "   Sign In  " style={styles.button} onPress = {() =>console.log("signin tabbed")}/>
        </SafeAreaView>
        
      </SafeAreaView>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  container2: {
    flex: 0.28,
    width: 250,
    overflow: 'hidden',
    backgroundColor: '#fff',
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    alignItems: 'baseline',
  },
  logo: {
    width: 300,
    height: 300,
    marginTop: 20,
  },
  title: {
    fontSize: 40,
    fontWeight: "bold",
    marginTop: 20,
  },
  idPass:{
    color:'white',
    width: 230,
    height: 40,
    backgroundColor: '#737373',
    marginTop: 15,
  },
  button: {
    width: 80,
   
  },
  space:{
    
    
  }
  
});
