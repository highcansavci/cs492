import { StatusBar } from 'expo-status-bar';
import React,{Component} from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { SafeAreaView,StyleSheet, Text, View, Image, TextInput,Button,KeyboardAvoidingView  } from 'react-native';
import { render } from 'react-dom';

class Signup extends Component{
    render() {
        return (
        <KeyboardAvoidingView style={styles.container} behavior="padding">
            <SafeAreaView  style={styles.container}>
                <Image source={require('./assets/logo.png')} style={styles.logo} /> 
                <Text style={styles.title} >Bil-Events</Text>
                <TextInput style={styles.idPass} placeholder={'ID'} />
                <TextInput style={styles.idPass} placeholder={'name'} />
                <TextInput style={styles.idPass} placeholder={'surname'} />
                <TextInput style={styles.idPass} placeholder={'Password'} secureTextEntry={true}/>
            </SafeAreaView >

            <SafeAreaView  style={styles.container2}>
                <Button title = "   Save   " style={styles.button} onPress = {() =>console.log("login tabbed")}/>
            </SafeAreaView>        
        </KeyboardAvoidingView>
        );
    }
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
  
});

export default Signup;