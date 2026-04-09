import { useState, useEffect } from "react";

const InputQuantity = ({ content, id, onDataSend, value }) => {
  const [isQuantity, setQuantity] = useState(value ?? 0);

  useEffect(() => {
    if (value !== undefined) {
      setQuantity(value);
    }
  }, [value]);

  const changeQuantityPlus = () => {
    const newValue = isQuantity + 1;
    setQuantity(newValue);
    if (onDataSend) onDataSend(newValue); // Передаем число, а не событие
  };

  const changeQuantityMinus = () => {
    const newValue = isQuantity - 1;
    setQuantity(newValue);
    if (onDataSend) onDataSend(newValue); // Передаем число, а не событие
  };

  const handleInputChange = (e) => {
    const newValue = parseInt(e.target.value) || 0;
    setQuantity(newValue);
    if (onDataSend) onDataSend(newValue); // Передаем число, а не событие
  };

  return (
    <div>
      <label
        htmlFor={id}
        className="
          block
          text-sm font-medium text-col_con
        "
      >
        {content}
      </label>

      <div
        className="
          flex
          rounded-sm border border-gray-200
          items-center dark:border-gray-800
        "
      >
        <button
          onClick={changeQuantityMinus}
          type="button"
          className="
            leading-10 text-col_bright_2 text-2xl
            cursor-pointer mr-2
            size-10 transition hover:opacity-75
            bg-col_bright_2/15 rounded-full 
          "
        >
          −
        </button>

        <input
          type="number"
          id={id}
          value={isQuantity}
          onChange={handleInputChange}
          className="
            h-10 w-16
            mt-1
            text-center
            rounded-lg border border-col_con/15
            [-moz-appearance:textfield] dark:bg-col_bas_mai dark:text-col_con 
            [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none 
            [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none
            sm:text-sm
          "
        />

        <button
          onClick={changeQuantityPlus}
          type="button"
          className="
            leading-10 text-col_bright_2 text-2xl
            cursor-pointer ml-2
            size-10 transition hover:opacity-75
            bg-col_bright_2/15 rounded-full 
          "
        >
          +
        </button>
      </div>
    </div>
  );
};
export default InputQuantity;
