import React from 'react';
import {
  BrowserRouter,
  Route,
  Routes
} from 'react-router-dom';
// import logo from './logo.svg';
// import './App.css';
// import axios, { AxiosResponse } from 'axios';
import {
  Box,
  ChakraProvider,
  Flex,
  Show,
  theme,
  useDisclosure
} from '@chakra-ui/react';
import TopHeader from './components/TopHeader';
import DrawerMenu from './components/DrawerMenu';
import SideMenu from './components/SideMenu';
import Dashboard from './routes/Dashboard';
import ToyokoInn from './routes/ToyokoInn';
import BottomFotter from './components/BottomFotter';

const App: React.FC = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();

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
    <ChakraProvider theme={theme}>
      <Box h={{ base: "80px", lg: "100px" }}>
        <TopHeader onOpen={onOpen} />
      </Box>
      <Box w="100vw" h={{ base: "calc(100vh - 80px - 40px)", lg: "calc(100vh - 100px - 40px)" }}>
        <Flex w="100%" h="100%">
          <BrowserRouter>
            <DrawerMenu isOpen={isOpen} onClose={onClose} />
            <Show above="lg">
              <SideMenu width="20vw" />
            </Show>
            <Box w={{ base: "100vw", lg: "80vw" }}>
              <Routes>
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/toyoko-inn" element={<ToyokoInn />} />
              </Routes>
            </Box>
          </BrowserRouter>
        </Flex>
      </Box>
      <Box h={{ base: "40px", lg: "40px" }}>
        <BottomFotter />
      </Box>
    </ChakraProvider>
  );
};

export default App;
