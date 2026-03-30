const TabButton = ({ name, tab, isActiveTab, setActiveTab }) => {
  return (
    <button
      onClick={() => setActiveTab(tab)}
      className={`
        px-4 py-2 text-col_con rounded-lg font-semibold shadow-lg
        hover:bg-col_bright_3 hover:shadow-col_bright_3/50 cursor-pointer
        ${isActiveTab == tab ? "bg-col_bright_1 shadow-col_bright_1/50" : "bg-col_bright_4/20"}
      `}
    >
      {name}
    </button>
  );
};
export default TabButton;
