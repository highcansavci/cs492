import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Login from './pages/Login';
import Signup from './pages/Signup';
import Homepage from './pages/Homepage';
import SelectedEvents from './pages/SelectedEvents';
import RecommendedEvents from './pages/RecommendedEvents';
import ClubList from './pages/ClubList';
import ForgotPassword from './pages/ForgotPassword';
import PastEventsPage from './pages/PastEventsPage';
import AddEventPage from './pages/AddEventPage';

const Stack = createStackNavigator();

function NavStack() {
  return (
    
     <Stack.Navigator
     
        initialRouteName="Login"
        screenOptions={{
          headerTitleAlign: 'center',
          headerStyle: {
            backgroundColor: '#465881',
          },
          headerTintColor: '#fff',
          headerTitleStyle :{
            fontWeight: 'bold',
          },
        }}
      >
      <Stack.Screen 
        name="Login" 
        component={Login} 
        options={{ title: 'Login' }}
      />
      <Stack.Screen 
        name="Signup" 
        component={Signup} 
        options={{ title: 'Signup' }}

      />
      <Stack.Screen 
        name="ForgotPassword" 
        component={ForgotPassword} 
        options={{ title: 'Forgot Password' }}
      />
       <Stack.Screen 
        name="Homepage" 
        component={Homepage} 
        options={{ title: 'Upcoming Events' }}      
      />
      <Stack.Screen 
        name="SelectedEvents" 
        component={SelectedEvents} 
        options={{ title: 'Selected Events' }}      
      />
      <Stack.Screen 
        name="RecommendedEvents" 
        component={RecommendedEvents} 
        options={{ title: 'Recommended Events' }}   
      />
      <Stack.Screen 
        name="PastEventsPage" 
        component={PastEventsPage} 
        options={{ title: 'Past Events' }}

      />
      <Stack.Screen 
        name="ClubList" 
        component={ClubList} 
        options={{ title: 'Club List' }}     
      />
      
      <Stack.Screen 
        name="AddEventPage" 
        component={AddEventPage} 
        options={{ title: 'Add Event' }}

      />
    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <NavStack />
    </NavigationContainer>
  );
}
