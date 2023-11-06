import { Box } from "@chakra-ui/react";
import CommonMenuButton from "./CommonMenuButton"
import { useNavigate } from "react-router-dom";
import MenuItems from "../MenuItems";

type Props = {
  width: string
}

const SideMenu = (props: Props) => {
  const navigate = useNavigate();

  return (
    <Box
      w={props.width}
      py={3}
      bg="gray.100"
    >
      {MenuItems.map((item) => (
        <Box key={item.name}>
          <CommonMenuButton
            iconType={item.icon}
            title={item.name}
            onClick={() => navigate(item.path)}
          />
        </Box>
      ))}
    </Box>
  );
};

export default SideMenu;
