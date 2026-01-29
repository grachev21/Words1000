import { NavLink } from "react-router-dom";

const LinkIcon = ({ to, name, icon: Icon }) => {
  return (
    <div className="flex flex-row items-center md:mx-4">
      <NavLink
        to={to}
        className={({ isActive }) => {
          const baseClasses = "flex items-center mx-2 pb-1 cursor-pointer";

          if (isActive) {
            return `${baseClasses} text-col_bright_1 border-b-2 border-col_bright_1`;
          } else {
            return `${baseClasses} text-col_con hover:text-col_bright_6`;
          }
        }}
      >
        {({ isActive }) => (
          <>
            {/* Иконка */}
            <div
              className={`p-2 rounded-full ${
                isActive ? "bg-col_bright_2/25" : "bg-col_bright_1/25"
              }`}
            >
              <Icon
                className={`w-4 h-4 ${
                  isActive ? "text-col_bright_2" : "text-col_bright_1"
                }`}
              />
            </div>

            {/* Текст */}
            <span className="ml-2">{name}</span>
          </>
        )}
      </NavLink>
    </div>
  );
};

export default LinkIcon;
