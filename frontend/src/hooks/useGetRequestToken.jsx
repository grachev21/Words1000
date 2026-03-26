import { useEffect, useState } from "react";
import axios from "axios";

const useGetRequestToken = (url) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            setLoading(false);
            return;
        }
        const fetchBasket = async () => {
            try {
                const response = await axios.get(
                    "http://localhost:8000/" + url,
                    {
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Token ${token}`,
                        },
                    },
                );
                setData(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchBasket();
    }, [url]);

    return { data, loading, error };
};

export default useGetRequestToken;
