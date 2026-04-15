import { useState, useEffect } from "react";

const InputQuantity = ({ content, id, onDataSend, value, min = 0, max = 99 }) => {
  const [isQuantity, setQuantity] = useState(value || 0);

  // Синхронизация с пропсом value (если родитель меняет значение извне)
  useEffect(() => {
    if (value !== undefined) {
      setQuantity(value);
    }
  }, [value]);

  // Плюс
  const changeQuantityPlus = () => {
    setQuantity((prev) => {
      const newValue = Math.min(prev + 1, max); // не выходим за пределы

      if (newValue !== prev && onDataSend) {
        onDataSend(newValue); // отправляем новое значение
      }

      return newValue;
    });
  };

  // Минус
  const changeQuantityMinus = () => {
    setQuantity((prev) => {
      const newValue = Math.max(prev - 1, min);

      if (newValue !== prev && onDataSend) {
        onDataSend(newValue);
      }

      return newValue;
    });
  };

  // Изменение через input
  const handleInputChange = (e) => {
    let newValue = parseInt(e.target.value) || 0;

    // Ограничиваем значение
    newValue = Math.max(min, Math.min(max, newValue));

    setQuantity(newValue);
    if (onDataSend) onDataSend(newValue);
  };

  return (
    <div>
      <label htmlFor={id} className="block text-sm font-medium text-col_con">
        {content}
      </label>

      <div className="flex rounded-sm border border-gray-200 items-center dark:border-gray-800">
        <button
          onClick={changeQuantityMinus}
          type="button"
          className="leading-10 text-col_bright_2 text-2xl cursor-pointer mr-2 size-10 transition hover:opacity-75 bg-col_bright_2/15 rounded-full"
        >
          −
        </button>

        <input
          type="number"
          id={id}
          value={isQuantity}
          onChange={handleInputChange}
          min={min}
          max={max}
          className="h-10 w-16 mt-1 text-center rounded-lg border border-col_con/15 
                     [-moz-appearance:textfield] dark:bg-col_bas_mai dark:text-col_con
                     [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none
                     [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none sm:text-sm"
        />

        <button
          onClick={changeQuantityPlus}
          type="button"
          className="leading-10 text-col_bright_2 text-2xl cursor-pointer ml-2 size-10 transition hover:opacity-75 bg-col_bright_2/15 rounded-full"
        >
          +
        </button>
      </div>
    </div>
  );
};

export default InputQuantity;
