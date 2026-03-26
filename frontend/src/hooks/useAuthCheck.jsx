import { useState, useEffect } from "react";
import axios from "axios";

const useAuthCheck = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const token = localStorage.getItem("token");
                if (!token) {
                    setIsAuthenticated(false);
                    setError("Токен не найден");
                    return;
                }

                const response = await axios.get(
                    "http://127.0.0.1:8000/auth/users/me/",
                    {
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Token ${token}`,
                        },
                    },
                );
                if (response.status === 200) {
                    setIsAuthenticated(true);
                    setError(null);
                }
            } catch (err) {
                const axiosError = err;
                const errorMessage = axiosError.response
                    ? axiosError.response.data
                    : "Произошла ошибка при проверке аутентификации";

                setError(errorMessage);
                setIsAuthenticated(false);
            } finally {
                setLoading(false);
            }
        };

        checkAuth();
    }, []);

    return {
        isAuthenticated,
        loading,
        error,
    };
};

export default useAuthCheck;
