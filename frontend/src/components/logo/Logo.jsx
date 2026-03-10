const Logo = () => {
  return (
    <a href="" className="cursor-pointer flex flex-row items-center hover:opacity-80 duration-300">
      <div className="bg-col_bright_1 p-2 rounded-lg text-white mr-2 shadow-lg shadow-col_bright_1/50">
        w1
      </div>
      <p className="bg-linear-to-r from-col_bright_1 to-col_bright_2 bg-clip-text text-md lg:text-xl font-extrabold text-transparent hidden md:block">
        Words 1000
      </p>
    </a>
  );
};

export default Logo;
