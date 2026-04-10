import LinkIcon from "@/components/links/LinkIcon";
import { FaHome, FaList, FaBook, FaTools } from "react-icons/fa";

const menu = [
  {
    name: "Главная",
    link: "home",
    icon: FaHome,
  },
  {
    name: "Слова",
    link: "words",
    icon: FaList,
  },
  {
    name: "Учить",
    link: "game",
    icon: FaBook,
  },
  {
    name: "Настройки",
    link: "settings",
    icon: FaTools,
  },
];
const Menu = () => {
  return (
    <div className="hidden flex-row items-center sm:flex sm:ml-4 lg:ml-12 xl:mx-46">
      {menu.map((value, index) => {
        return (
          <LinkIcon
            key={index} // ← почти всегда нужен key!
            icon={value.icon}
            link={value.link}
            name={value.name}
          />
        );
      })}
    </div>
  );
};
export default Menu;
