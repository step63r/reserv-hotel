import React from 'react';
import {
  AuthenticatedTemplate,
  UnauthenticatedTemplate,
  useMsal,
} from '@azure/msal-react'
import {
  Button,
  Box,
  Flex,
  Heading,
  Spacer,
  Text
} from '@chakra-ui/react';
import { loginRequest } from '../authConfig';

const Header: React.FC = () => {
  const { instance } = useMsal();
  const activeAccount = instance.getActiveAccount();

  const handleRedirect = () => {
    instance
      .loginRedirect({
        ...loginRequest,
        prompt: 'create',
      })
      .catch((error) => console.log(error));
  }

  return (
    <Flex
      as="header"
      position="fixed"
      bg="gray.100"
      top={0}
      width="full"
      shadow="sm"
      py={4}
      px={8}
    >
      <Box bg="transparent">
        <Heading>ホテル自動予約サービス</Heading>
      </Box>
      <Spacer />
      <Box bg="transparent">
        <AuthenticatedTemplate>
          <Text>{activeAccount?.name} さんでログイン中</Text>
          <Button colorScheme="teal" variant="outline" onClick={() => instance.logout()}>ログアウト</Button>
        </AuthenticatedTemplate>
        <UnauthenticatedTemplate>
          <Button colorScheme="teal" onClick={handleRedirect}>ログイン/新規登録</Button>
        </UnauthenticatedTemplate>
      </Box>
    </Flex>
  )
};

export default Header;
