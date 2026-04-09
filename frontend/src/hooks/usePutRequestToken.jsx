import { useState } from "react";
import axios from "axios";

const usePutRequestToken = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const putData = async (url, body) => {
    setLoading(true);
    setError(null);

    try {
      const token = localStorage.getItem("token");
      const response = await axios.put("http://localhost:8000/" + url, body, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      });
      setData(response.data);
      return { success: true, data: response.data };
    } catch (err) {
      const errorData = err.response?.data || { detail: "Ошибка сети" };
      setError(errorData);
      return { success: false, error: errorData };
    } finally {
      setLoading(false);
    }
  };

  return { putData, data, loading, error };
};

export default usePutRequestToken;
