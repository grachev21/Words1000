const CheckBoxSimple = ({ label, description, value, onDataSend }) => {
  return (
    <label className="flex items-center gap-3 cursor-pointer group">
      <input
        type="checkbox"
        className="hidden peer"
        checked={value}
        onChange={onDataSend} // убрал лишнюю обёртку (e) => onDataSend(e)
      />
      {/* peer-checked работает — div идёт сразу после input */}
      <div
        className="w-5 h-5 rounded-md border border-zinc-700 bg-zinc-900 
        flex items-center justify-center
        peer-checked:bg-col_bright_1 peer-checked:border-col_bright_1 
        group-hover:border-zinc-500 transition-all duration-150 shrink-0"
      >
        {/* svg показываем через value, не через peer — он внутри div */}
        {value && (
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path
              d="M2 6L5 9L10 3"
              stroke="white"
              strokeWidth="1.8"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        )}
      </div>
      <div className="flex flex-col">
        <span className="text-sm text-col_con">{label}</span>
        {description && <span className="text-xs text-col_suc_ave">{description}</span>}
      </div>
    </label>
  );
};

export default CheckBoxSimple;
