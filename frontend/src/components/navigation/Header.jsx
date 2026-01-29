import Logo from "@/components/logo/Logo";
import Menu from "@/components/navigation/Menu"

const Header = () => {
    return (
    <header
        className="fixed flex items-center border-b border-col_con/15 top-0 left-0 w-full z-50 min-h-16 bg-col_bas_mai/80 backdrop-blur-2xl">
        <main className="w-full mx-4 md:mx-12 flex flex-row justify-between items-center">
            <div className="flex flex-row justify-between items-center">
                <Logo />
                <nav className="flex flex-row">
                    <Menu />
                    {/* {% include 'components/header/dropdown_menu.html' %} */}
                </nav>
            </div>

            {/* {% include 'components/header/theme_toggle.html' %} */}

            <img className="sm:hidden w-6 h-6" id="burger" src="{% static 'icons/menu.png' %}" alt="" />
        </main>
    </header>)

};
export default Header;
