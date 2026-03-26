import { NavLink } from "react-router-dom";

const LinkSimple = ({ name, link, onClick }) => {
  return (
    <NavLink
        onClick={onClick}
      to={link}
      className={({ isActive }) =>
        `mx-0.5 my-2
        ${isActive
          ? "text-col_bright_1 border-b-2"
          : "text-col_con hover:text-col_bright_6"}
          `}
    >
      {name}
    </NavLink>
  );
};

export default LinkSimple;
