import React from 'react';
import { StyleSheet,Image, Text, View, TextInput, TouchableOpacity, Dimensions } from 'react-native';

const { width, height } = Dimensions.get('window');
export default class Signup extends React.Component {
  state={
    bilkent_id:"",
    first_name:"",
    last_name:"",
    email:"",
    password:"",
  }
  async userSignup() { 
    const response = await fetch("https://bileventsapp.herokuapp.com/auth/register", { 
      method: "POST", 
      headers: { 
        'Accept': 'application/json', 
        'Content-Type': 'application/json' 
      },
      body: JSON.stringify({ 
        bilkent_id:this.state.bilkent_id,
        first_name:this.state.first_name,
        last_name:this.state.last_name,
        email: this.state.email, 
        password: this.state.password, 
      }) 
    });
    const data = await response.json();
    if(response.status == "400")
    {
      alert("Unsuccessful Register\nInvalid Inputs");
    }
    else{
      alert("Signed Up Successfully" );
      this.props.navigation.navigate('Login');
    }
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
            onChangeText={text => this.setState({bilkent_id:text})}/>
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
            onChangeText={text => this.setState({first_name:text})}/>
        </View>
        <View style={styles.inputView} >
          <TextInput  
            style={styles.inputText}
            placeholder="Surname" 
            placeholderTextColor="white"
            onChangeText={text => this.setState({last_name:text})}/>
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
        <TouchableOpacity style={styles.loginBtn} onPress = {() =>this.userSignup(this.state)}>
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