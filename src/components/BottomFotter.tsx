import { Box, Flex, Text } from "@chakra-ui/react";

const BottomFotter = () => {
  return (
    <Flex
      as="footer"
      width="100%"
      height="100%"
      bg="gray.100"
      shadow="sm"
      align="center"
      px={{ base: 2, lg: 4 }}
    >
      <Box ml={{ base: 2, lg: 4 }}>
        <Text>© 2023 minato project. All rights reserved</Text>
      </Box>
    </Flex>
  );
};

export default BottomFotter;
