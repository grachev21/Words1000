import { useNavigate } from "react-router-dom";
import axios from "axios";

const useLogout = () => {
    const navigate = useNavigate();

    const logout = async () => {
        try {
            await axios.post("http://127.0.0.1:8000/auth/token/logout/", null, {
                headers: {
                    Authorization: `Token ${localStorage.getItem("token")}`,
                },
            });
        } catch (err) {
            console.error(
                "Logout error:",
                err.response ? err.response.data : err,
            );
        } finally {
            localStorage.removeItem("token");

            navigate("/login");
            navigate(0);
        }
    };

    return { logout };
};

export default useLogout;
