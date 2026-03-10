import { BrowserRouter, Routes, Route } from "react-router-dom";
import "@/styles/styles.css";

import Home from "@/pages/Home";
import Settings from "@/pages/Settings";
import Test from "@/pages/Test";
import Words from "@/pages/Words";
import Header from "@/components/navigations/Header";
import Footer from "@/components/other/footer/Footer";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Header />
        <div className="mt-56 p-8">
          <Routes>
            <Route path="/home" element={<Home />} />
            <Route path="/words" element={<Words />} />
            <Route path="/test" element={<Test />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  );
};

export default App;
