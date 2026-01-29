import { FaHome, FaList, FaBookOpen, FaTools } from "react-icons/fa";

const menu = [
  {
    name: "Главная",
    url_name: "/",
    img_name: FaHome,
  },
  {
    name: "Слова",
    url_name: "/words",
    img_name: FaList,
  },
  {
    name: "Учить",
    url_name: "/learn",
    img_name: FaBookOpen,
  },
  {
    name: "Настройки",
    url_name: "/settings",
    img_name: FaTools,
  },
];

export default menu;
