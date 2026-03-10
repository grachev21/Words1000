import { useState, useRef, useEffect } from "react";
import LinkSimple from "@/components/links/LinkSimple";
import { FaUser } from "react-icons/fa";

const DropDownMenu = ({ name, icon, menu }) => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef(null);

  // Закрываем при клике вне компонента
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const toggleDropdown = () => {
    setIsOpen((prev) => !prev);
  };

  const handleItemClick = (action) => {
    if (action) action(); // если у пункта есть действие
    setIsOpen(false); // закрываем после выбора
  };

  return (
    <menu ref={dropdownRef} className="hidden mx-auto items-center justify-center sm:flex relative">
      <div className="py-2 cursor-pointer relative">
        <button onClick={toggleDropdown} className="flex flex-row lg:px-4 rounded-full lg:border lg:border-col_con_inv/15 lg:rounded-lg md:h-10 cursor-pointer items-center hover:opacity-80">
          <span className="hidden h-10 space-x-5 items-center justify-between lg:flex text-col_con font-bold">
            {name}
          </span>
          <FaUser className="text-col_bright_3 ml-2" />
        </button>

        <div
          className="z-50 mt-3.5 lg:mt-5 text-md lg:text-md pl-5 
          flex flex-col w-full lg:shadow-xl lg:border lg:border-col_con_inv/15 rounded-lg absolute"
        >
          <LinkSimple name={"Выйти"} link={"/logout"} />
          <LinkSimple name={"Войти"} link={"/logout"} />
          <LinkSimple name={"Регистрация"} link={"/logout"} />
        </div>
      </div>
    </menu>
  );
};
export default DropDownMenu;
