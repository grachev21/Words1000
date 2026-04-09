import { useState, useEffect } from "react";

const Error = ({ error, item, content }) => {
  const [isError, setError] = useState(false);

  useEffect(() => {
    if (error) {
      const keys = Object.keys(error);
      if (item == keys) {
        console.log(item, "<<<");
        console.log(keys, "<<<");
        setError(error[keys]);
      }
    }
  });

  return isError ? (
    <main
      className="text-col_attn w-full bg-col_con_inv/15 p-2 rounded-lg 
                       border border-col_att_base"
    >
      {content}
      {isError}
    </main>
  ) : null;
};
export default Error;
