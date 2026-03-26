const Input = ({ content, type, id, placeholder, onDataSend }) => {
    return (
        <div>
            <label className="block text-sm font-medium text-col_con" htmlFor={id}>
                {content}
            </label>

            <input
                className="mt-1 w-full rounded-lg border border-col_con/15 focus:border-col_bright_1 focus:outline-none bg-col_bas_mai text-col_con p-1"
                onChange={(e) => onDataSend(e)}
                id={id}
                type={type}
                placeholder={placeholder}
            />
        </div>
    );
};
export default Input;
