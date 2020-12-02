import React from 'react';
import { StyleSheet,Image, Text, View, TextInput, TouchableOpacity, Dimensions } from 'react-native';

const { width, height } = Dimensions.get('window');
export default class App extends React.Component {
  state={
    IDNo:0,
    email:"",
    password:"",
    name:"",
    surname:"",

  }
  render(){
    return (
      <View style={styles.container}>
        <View  style={styles.logo} >
          <Image source={require('./assets/logo.png')} style={styles.logo} />
        </View>  
        <View style={styles.inputView} >
          <TextInput  
            style={styles.inputText}
            placeholder="ID number" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({IDNo:text})}/>
        </View>
        <View style={styles.inputView} >
          <TextInput  
            style={styles.inputText}
            placeholder="E-Mail Address" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({email:text})}/>
        </View>
        <View style={styles.inputView} >
          <TextInput              
            style={styles.inputText}
            placeholder="Name" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({name:text})}/>
        </View>
        <View style={styles.inputView} >
          <TextInput  
            style={styles.inputText}
            placeholder="Surname" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({surname:text})}/>
        </View>
        <View style={styles.inputView} >
          <TextInput  
            secureTextEntry
            style={styles.inputText}
            placeholder="Password" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({password:text})}/>
        </View>
        <TouchableOpacity>
          <Text style={styles.forgot}>Forgot Password?</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.loginBtn} onPress = {() =>this.props.navigation.navigate('Login')}>
          <Text style={styles.loginText}>REGISTER</Text>
        </TouchableOpacity>
  
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },

  logo: {
    width: width * 0.67,
    height: height * 0.48,
  },

  inputView:{
    width:"80%",
    backgroundColor:"#465881",
    borderRadius:25,
    height:'5%',
    marginBottom:'2.5%',
    justifyContent:"center",
    padding:20
  },
  inputText:{
    height:40,
    color:"white"
  },
  forgot:{
    color:"black",
    fontSize:11
  },
  loginBtn:{
    width:"50%",
    backgroundColor:"#fb5b5a",
    borderRadius:25,
    height:'7%',
    alignItems:"center",
    justifyContent:"center",
    marginTop:'2%',
    marginBottom: '10%'
  },
});