import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useLogin } from "@/hooks";

import { Input } from "@/components";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const { login, loading, error, success } = useLogin();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const credentials = { email, password };
    await login(credentials); // Вызываем хук для авторизации
  };
  useEffect(() => {
    if (success) {
      navigate("/home", { replace: true }); // replace — чтобы не было кнопки "назад" на форму
    }
  }, [success, navigate]);
  return (
    <form
      className="mx-auto max-w-md space-y-4 rounded-lg border border-col_con/15 bg-col_bas_hig p-6"
      onSubmit={handleSubmit}
    >
      {error && <Error content={"email: " + error.email} />}
      <Input
        onDataSend={(e) => setEmail(e.target.value)}
        content={"Email"}
        type={"email"}
        id={"email"}
        placeholder={"Email"}
        value={email}
      />

      {error && <Error content={"password: " + error.password} />}
      <Input
        onDataSend={(e) => setPassword(e.target.value)}
        content={"Пароль"}
        type={"password"}
        id={"password"}
        placeholder={"Пароль"}
        value={password}
      />

      <button
        className="block w-full rounded-lg border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white transition-colors hover:bg-transparent hover:text-indigo-600 dark:hover:bg-indigo-700 dark:hover:text-white"
        type="submit"
      >
        {loading ? "ВХОДИМ" : "ВОЙТИ"}
      </button>
    </form>
  );
};
export default Login;
