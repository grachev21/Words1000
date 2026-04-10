import { useState } from "react";

const SelectSimple = ({ status, currentStatus, content, onDataSend }) => {
  const [selectedValue, setSelectedValue] = useState(currentStatus);

  const currentItemStatus = status.find((item) => item.key === currentStatus);

  const handleChange = (e) => {
    setSelectedValue(e.target.value);
    if (onDataSend) onDataSend(e.target.value);
  };

  return (
    <label
      htmlFor="select-headliner"
      className="
          block
          text-sm font-medium text-col_con
      "
    >
      {content}

      <div
        className="
          relative
        "
      >
        <select
          id="select-headliner"
          value={selectedValue}
          onChange={handleChange}
          className="
            w-full mt-1
            px-3.5 py-2.5 pr-10
            text-sm text-col_bright_2
            bg-col_bas_mai
            border border-col_con/15 rounded-lg
            cursor-pointer transition-colors
            appearance-none outline-none duration-150 hover:border-col_con/15 focus:border-col_bright_4 focus:ring-2 focus:ring-col_bright_1
          "
        >
          <option value={currentItemStatus.key}>{currentItemStatus.display}</option>
          {status.map((value, index) =>
            value.key != currentStatus ? (
              <option key={index} value={value.key}>
                {value.display}
              </option>
            ) : null,
          )}
        </select>

        <div
          className="
            flex
            text-col_suc_ave
            pointer-events-none
            absolute inset-y-0 right-3 items-center
          "
        >
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path
              d="M3 5L7 9L11 5"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </div>
      </div>
    </label>
  );
};

export default SelectSimple;
