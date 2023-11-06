import {
  Box,
  Button,
  Flex,
  Hide,
  Spacer,
  Text
} from "@chakra-ui/react";
import { HamburgerIcon } from '@chakra-ui/icons'
import { AuthenticatedTemplate, UnauthenticatedTemplate, useMsal } from "@azure/msal-react";
import { loginRequest } from '../authConfig';

type Props = {
  onOpen: () => void;
}

const TopHeader = (props: Props) => {
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
      top={0}
      width="100%"
      height="100%"
      bg="azure"
      shadow="sm"
      align="center"
      px={{ base: 2, lg: 4 }}
    >
      <Hide above="lg">
        <Button
          variant="ghost"
          fontSize={{ base: "xl", lg: "3xl" }}
          boxSize={{ base: 8, lg: 16 }}
          onClick={() => props.onOpen()}
        >
          <HamburgerIcon />
        </Button>
      </Hide>
      <Box
        ml={{ base: 2, lg: 4 }}
        fontSize={{ base: "xl", lg: "3xl" }}
        fontWeight="bold"
      >
        ホテル自動予約サービス
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
  );
};

export default TopHeader;
