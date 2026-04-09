const ButtonLight = ({ content, onClick }) => {
  return (
    <button
      onClick={onClick}
      className="mt-6 px-4 py-2 bg-col_con text-col_bas_mai
            rounded-lg hover:bg-col_con/85 transition-colors flip-btn
            cursor-pointer"
    >
      {content}
    </button>
  );
};
export default ButtonLight;
