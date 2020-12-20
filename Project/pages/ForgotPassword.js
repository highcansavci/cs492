import React from 'react';
import { StyleSheet,Image, Text, View, TextInput, TouchableOpacity, Dimensions } from 'react-native';
const { width, height } = Dimensions.get('window');



export default class ForgotPassword extends React.Component {
  state={
    email:""
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
            placeholder="Email Adress" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({email:text})}/>
        </View>      
        <TouchableOpacity style={styles.loginBtn} onPress = {() =>alert('New Password is sent to '+ this.state.email)}>
          <Text style={styles.loginText} >Send Email</Text>
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
    width:"70%",
    backgroundColor:"#465881",
    borderRadius:25,
    height:'6%',
    marginBottom:'2.5%',
    justifyContent:"center",
    padding:10
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
    marginTop:'2.5%',
    marginBottom:'2.5%',
  },
  signupBtn:{
    width:"50%",
    backgroundColor:"#fb5b5a",
    borderRadius:25,
    height:'7%',
    alignItems:"center",
    justifyContent:"center",
    marginTop:'2.5%',
    marginBottom:'2.5%',
  }
});