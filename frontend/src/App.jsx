import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "@/components/navigation/Header";
import Home from "@/page/Home";
import Words from "@/page/Words";
import Learn from "@/page/Learn";
import Settings from "@/page/Settings";
import GoogleAuth from "@/page/Login";

import "./styles.css";

function App() {
    return (
        <>
            <BrowserRouter>
                <Header />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/words" element={<Words />} />
                    <Route path="/learn" element={<Learn />} />
                    <Route path="/settings" element={<Settings />} />
                    <Route path="/googleauth" element={<GoogleAuth/>} />
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;
