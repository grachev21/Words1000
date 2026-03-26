import { useState } from "react";
import axios from "axios";

const useRegister = () => {
  const [loading, setLoading] = useState(false); // Состояние для отслеживания загрузки
  const [error, setError] = useState(null); // Состояние для хранения ошибок
  const [success, setSuccess] = useState(false); // Состояние для отслеживания успешной регистрации

  const register = async (userData) => {
    setLoading(true); // Начинаем загрузку
    setError(null); // Сбрасываем ошибки
    setSuccess(false); // Сбрасываем состояние успеха

    try {
      // Отправляем POST-запрос на эндпоинт регистрации Djoser
      const response = await axios.post("http://127.0.0.1:8000/auth/users/", userData);

      // Если запрос успешен
      setSuccess(true);
      return response.data; // Возвращаем данные ответа (если нужно)
    } catch (err) {
      // Обрабатываем ошибку
      setError(err.response ? err.response.data : "An error occurred");
    } finally {
      setLoading(false); // Завершаем загрузку
    }
  };

  return { register, loading, error, success };
};

export default useRegister;
