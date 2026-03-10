import { NavLink } from "react-router-dom";

const LinkSimple = ({ name, link }) => {
  return;
  <NavLink
    to={link}
    className={({ isActive }) => {
      isActive
        ? "text-col_bright_1 border-b-2 border-col_bright_1"
        : "text-col_con hover:text-col_bright_6";
    }}
  >
    {name}
  </NavLink>;
};

export default LinkSimple;
