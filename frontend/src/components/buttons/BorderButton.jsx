const BorderButton = ({ onClick, active, value, content }) => {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors cursor-pointer
              ${
                active === value
                  ? "border border-col_bright_2 text-col_con"
                  : "border border-col_bright_1 hover:bg-col_bright_2/25 text-col_con"
              }`}
    >
      {content}
    </button>
  );
};
export default BorderButton;
