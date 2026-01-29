import menu from "@/assets/menu";
import LinkIcon from "@/components/link/LinkIcon";

const Menu = () => {
  return (
    <main>
      <div className="hidden flex-row items-center sm:flex sm:ml-4 lg:ml-12 xl:mx-46">
        {menu.map((item, index) => (
          <LinkIcon
            key={index}
            to={item.url_name}
            name={item.name}
            icon={item.img_name}
          />
        ))}
      </div>
    </main>
  );
};

export default Menu;
