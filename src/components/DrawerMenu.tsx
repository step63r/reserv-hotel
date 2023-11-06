import { Box, Drawer, DrawerBody, DrawerContent, DrawerOverlay, Flex } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import MenuItems from "../MenuItems";
import CommonMenuButton from "./CommonMenuButton";

type Props = {
  isOpen: boolean,
  onClose: () => void;
}

const DrawerMenu = (props: Props) => {
  const navigate = useNavigate();

  const onClickMenu = (path: string) => {
    navigate(path);
    props.onClose();
  };

  return (
    <Drawer
      placement="left"
      isOpen={props.isOpen}
      onClose={props.onClose}
    >
      <DrawerOverlay />
      <DrawerContent bg="gray.100">
        <DrawerBody px={0} py={6}>
          <Flex direction="column">
            {MenuItems.map((item) => (
              <Box key={item.name}>
                <CommonMenuButton
                  iconType={item.icon}
                  title={item.name}
                  onClick={() => onClickMenu(item.path)}
                />
              </Box>
            ))}
          </Flex>
        </DrawerBody>
      </DrawerContent>
    </Drawer>
  );
}

export default DrawerMenu;
