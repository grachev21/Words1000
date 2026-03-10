import DropDownMenu from "@/components/navigations/DropDownMenu";
import Logo from "@/components/logo/Logo";
import Menu from "@/components/navigations/Menu";
import ThemeToggle from "@/components/buttons/ThemeToggle";

const menu = [
  { name: "Выйти", link: "logout" },
  { name: "Войти", link: "login" },
  { name: "Регистрация", link: "signup" },
];

const Header = () => {
  return (
    <header
      className="fixed flex items-center border-b border-col_con/15 top-0 left-0
      w-full z-50 min-h-16 bg-col_bas_mai/80 backdrop-blur-2xl"
    >
      <main className="w-full mx-4 flex flex-row justify-between items-center">
        <div className="flex flex-row justify-between items-center">
          <Logo />
          <nav className="flex flex-row">
            <Menu />
            <DropDownMenu name={"Пользователь"} icon={"user"} menu={menu} />
          </nav>
        </div>

        <div className="hidden sm:block ml-2">
          <ThemeToggle />
        </div>
        <div className="sm:hidden">{/* <c-organism.mobile-menu /> */}</div>
      </main>
    </header>
  );
};
export default Header;
