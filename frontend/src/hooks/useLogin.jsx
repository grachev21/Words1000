import { useState } from "react";
import axios from "axios";

const useLogin = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [token, setToken] = useState(null);

  const login = async (credentials) => {
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/auth/token/login/",
        credentials,
      );

      const authToken = response.data.auth_token;
      setToken(authToken);
      localStorage.setItem("token", authToken);
      setSuccess(true);
      return response.data;
    } catch (err) {
      setError(err.response ? err.response.data : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  return { login, loading, error, success, token };
};

export default useLogin;
