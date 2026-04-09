import { useState, useEffect } from "react";
import useRegister from "@/hooks/useRegister";
import { useNavigate } from "react-router-dom";
import { Input, Error } from "@/components";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const { register, loading, error, success } = useRegister();

  const handleSubmit = async (e) => {
    e.preventDefault();

    await register({
      email,
      password,
      confirmPassword,
    });
  };

  useEffect(() => {
    if (success) {
      navigate("/login", { replace: true }); // replace — чтобы не было кнопки "назад" на форму
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
      <Input
        onDataSend={(e) => setConfirmPassword(e.target.value)}
        content={"Пароль еще раз"}
        type={"password"}
        id={"password"}
        placeholder={"Пароль"}
        value={confirmPassword}
      />

      <button
        className="block w-full rounded-lg border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white transition-colors hover:bg-transparent hover:text-indigo-600 dark:hover:bg-indigo-700 dark:hover:text-white"
        type="submit"
      >
        {loading ? "РЕГИСТРАЦИЯ" : "РЕГИСТРИРУЕМСЯ"}
      </button>
    </form>
  );
};
export default Register;
