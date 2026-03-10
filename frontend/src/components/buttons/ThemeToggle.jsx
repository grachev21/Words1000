const ThemeToggle = ({ light }) => {
  return (
    <div>
      <label htmlFor="toggle" className="flex items-center cursor-pointer">
        <div className="relative">
          <input type="checkbox" id="toggle" className="sr-only" />
          <div
            className={
              light
                ? "bg-col_bright_5"
                : "bg-col_bright_2" +
                  "block w-10 h-6 rounded-full transition-all duration-300 ease-in-out"
            }
          ></div>
          <div className="absolute top-1 bg-col_con w-4 h-4 rounded-full transition-all duration-300 ease-in-out"></div>
        </div>
      </label>
    </div>
  );
};

export default ThemeToggle;
