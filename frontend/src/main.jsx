import { GoogleOAuthProvider } from "@react-oauth/google";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <GoogleOAuthProvider clientId="391077185859-6ngkoqj670vqlfcik0bi5o3u6ge5tdbb.apps.googleusercontent.com">
            <App />
        </GoogleOAuthProvider>
    </StrictMode>,
);
