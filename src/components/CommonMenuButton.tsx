import { Button, Icon, Spacer } from "@chakra-ui/react";
import { IconType } from "react-icons";

type Props = {
  iconType: IconType
  title: string;
  onClick: () => void;
}

const CommonMenuButton = (props: Props) => (
  <Button
    w="100%"
    h="auto"
    px={6}
    py={3}
    variant="ghost"
    onClick={props.onClick}
  >
    <Spacer />
    <Icon
      as={props.iconType}
      w={7}
      h={7}
      mr={2}
    />
    {props.title}
    <Spacer />
  </Button>
);

export default CommonMenuButton;
