import { useState, useRef, useEffect } from "react";
import useAuthCheck from "@/hooks/useAuthCheck";
import useLogout from "@/hooks/useLogout";
import LinkSimple from "@/components/links/LinkSimple";
import { FaUser } from "react-icons/fa";

const DropDownMenu = ({ name }) => {
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef(null);
    const { logout } = useLogout();

    const { isAuthenticated, loading, error } = useAuthCheck();

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (
                dropdownRef.current &&
                !dropdownRef.current.contains(event.target)
            ) {
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
        if (action) action();
        setIsOpen(false);
    };

    return (
        <menu
            ref={dropdownRef}
            className="hidden mx-auto items-center justify-center sm:flex relative"
        >
            <div className="py-2 cursor-pointer relative">
                <button
                    onClick={toggleDropdown}
                    className="flex flex-row lg:px-4 rounded-full lg:border lg:border-col_con_inv/15 lg:rounded-lg md:h-10 cursor-pointer items-center hover:opacity-80"
                >
                    <span className="hidden h-10 space-x-5 items-center justify-between lg:flex text-col_con font-bold">
                        {name}
                    </span>
                    <FaUser
                        className={`ml-2 ${isOpen ? "text-col_bright_2" : "text-col_bright_3"}`}
                    />
                </button>

                {isOpen && (
                    <div
                        className="z-50 mt-3.5 lg:mt-5 text-md lg:text-md pl-5
                                flex flex-col w-full lg:shadow-xl lg:border lg:border-col_con_inv/15 rounded-lg absolute"
                    >
                        {isAuthenticated ? (
                            <div
                                onClick={logout}
                                className="mx-0.5 my-2 text-col_con"
                            >
                                Выйти
                            </div>
                        ) : (
                            <>
                                <LinkSimple
                                    name={"Войти"}
                                    link={"/login"}
                                    onClick={() => handleItemClick()}
                                />
                                <LinkSimple
                                    name={"Регистрация"}
                                    link={"/registration"}
                                    onClick={() => handleItemClick()}
                                />
                            </>
                        )}
                    </div>
                )}
            </div>
        </menu>
    );
};
export default DropDownMenu;
