// GoogleAuth.jsx или Login.jsx
import { GoogleLogin, googleLogout } from "@react-oauth/google";
import axios from "axios";

const GoogleAuth = () => {
    const handleSuccess = async (credentialResponse) => {
        console.log("ID Token:", credentialResponse.credential); // ← сначала просто выведи в консоль

        try {
            const res = await axios.post(
                "http://localhost:8000/api/auth/social/login/",
                {
                    provider: "google",
                    id_token: credentialResponse.credential,
                },
                {
                    withCredentials: true,
                }
            );
            console.log("Backend response:", res.data);
        } catch (err) {
            console.error("Backend error:", err.response?.data || err);
        }
    };

    return (
        <GoogleLogin
            onSuccess={handleSuccess}
            onError={() => console.log("Login Failed")}
            useOneTap={false}                  // отключаем One Tap, если мешает
            ux_mode="popup"                     // явно popup (по умолчанию и так, но иногда помогает)
            // login_uri="http://localhost:5173" // ← иногда нужно, но редко
            // nonce="random-string-here"       // можно попробовать рандомный nonce
            // prompt="select_account"          // или "consent"
            auto_select={false}
            // theme="filled_blue"               // или outline / filled_black
            // size="large"
            // shape="rectangular"
            // text="signin_with"
        />
    );
};

export default GoogleAuth;
