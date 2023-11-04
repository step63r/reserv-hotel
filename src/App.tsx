import React from 'react';
// import logo from './logo.svg';
// import './App.css';
// import axios, { AxiosResponse } from 'axios';
import { ChakraProvider, VStack } from '@chakra-ui/react';
import Header from './components/Header';
import Footer from './components/Footer';

const App: React.FC = () => {
  // useEffect(() => {
  //   axios.get('/api/HttpTrigger1')
  //     .then(response => {
  //       // handle success
  //       setResponse(response);
  //       console.log(response);
  //     })
  //     .catch(error => {
  //       // handle error
  //       console.log(error);
  //     })
  //     .then(() => {
  //       // always executed
  //     });
  // }, []);

  return (
    <ChakraProvider>
      <VStack spacing={4} align="stretch">
        <Header />
        <Footer />
      </VStack>
    </ChakraProvider>
    
  );
};

export default App;
