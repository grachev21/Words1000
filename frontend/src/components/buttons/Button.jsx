const Button = ({ content, onClick }) => {
  return (
    <button
      onClick={onClick}
      className="mt-12 px-4 py-2 bg-col_suc_mai text-col_con font-bold
    rounded-lg hover:bg-col_bright_2 transition-colors 
    cursor-pointer w-full"
    >
      {content}
    </button>
  );
};

export default Button;
