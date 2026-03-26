import { useState } from "react";

const ThemeToggle = () => {
  const [isLight, setIsLight] = useState(false);

  const toggle = () => {
    setIsLight((prev) => !prev);
  };

  return (
    <label htmlFor="theme-toggle" className="flex items-center cursor-pointer">
      <div className="relative">
        <input
          type="checkbox"
          id="theme-toggle"
          className="sr-only"
          checked={isLight}
          onChange={toggle}
        />

        {/* Фон */}
        <div
          className={`
            block w-10 h-6 rounded-full transition-all duration-300 ease-in-out
            ${isLight ? "bg-col_bright_5" : "bg-col_bright_2"}
          `}
        />

        {/* Бегунок */}
        <div
          className={`
            absolute top-1 w-4 h-4 bg-col_con rounded-full
            transition-all duration-300 ease-in-out
            ${isLight ? "left-1" : "right-1"}
          `}
        />
      </div>
    </label>
  );
};

export default ThemeToggle;
