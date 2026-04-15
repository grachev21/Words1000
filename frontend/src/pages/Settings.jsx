import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Load, Error, CheckBoxSimple, InputQuantity, SelectSimple } from "@/components";
import { useGetRequestToken, usePutRequestToken } from "@/hooks";

const Login = () => {
  const [isNumberWords, setNumberWords] = useState("");
  const [isNumberRepetitions, setNumberRepetitions] = useState("");
  const [isNumberWrite, setNumberWrite] = useState("");
  const [isMaxNumberRead, setMaxNumberRead] = useState("");
  const [isTranslationList, setTranslationList] = useState(false);

  const navigate = useNavigate();

  const dataGet = useGetRequestToken("api/settings/SettingsWords/");
  const dataPut = usePutRequestToken();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const credentials = {
      number_words: isNumberWords,
      number_repetitions: isNumberRepetitions,
      number_write: isNumberWrite,
      max_number_read: isMaxNumberRead,
      translation_list: isTranslationList,
    };
    console.log(credentials);

    const result = await dataPut.putData(
      `api/settings/SettingsWords/${dataGet.data[0].id}/`,
      credentials,
    );
    if (result.success) {
      console.log("Сохранено:", result.data);
      navigate("/home");
    } else {
      // result.error — объект ошибок от DRF
      // { username: ["Это поле обязательно"], non_field_errors: ["..."] }
      console.log("Ошибки:", result.error);
    }
  };

  useEffect(() => {
    if (dataGet.data[0]) {
      setNumberWords(dataGet.data[0].number_words);
      setNumberRepetitions(dataGet.data[0].number_repetitions);
      setNumberWrite(dataGet.data[0].number_write);
      setMaxNumberRead(dataGet.data[0].max_number_read);
      setTranslationList(dataGet.data[0].translation_list);
    }
  }, [dataGet.data]);

  if (dataGet.loading) return <Load />;
  console.log(isNumberWords)

  return (
    <form
      onSubmit={handleSubmit}
      method="put"
      className="
        max-w-md
        mx-auto space-y-4 p-6
        bg-col_bas_hig
        rounded-lg border border-col_con/15
      "
    >
      <h1
        className="
          mt-8 mb-4
          text-col_con font-bold text-2xl text-center
        "
      >
        Настройки
      </h1>
      <Error error={dataPut.error} item={"number_words"} content={"Количество слов: "} />
      <InputQuantity
        content={"Количество слов за день"}
        id={"number_words"}
        onDataSend={(value) => setNumberWords(value)}
        value={isNumberWords}
        min={5}
        max={100}
      />

      {/* Доделать */}
      <Error
        error={dataPut.error}
        item={"number_repetitions"}
        content={"Количество повторений: "}
      />
      <SelectSimple
        onDataSend={(value) => setNumberRepetitions(value)}
        status={dataGet.data[0].number_repetitions_display}
        currentStatus={dataGet.data[0].number_repetitions}
        content={"Количество повторений"}
      />

      <Error
        error={dataPut.error}
        item={"number_write"}
        content={"Количество написанных предложений: "}
      />
      <InputQuantity
        onDataSend={(value) => setNumberWrite(value)}
        content={"Максимальное количество раз при наборе"}
        id={"number_write"}
        value={isNumberWrite}
        min={2}
        max={100}
      />

      <Error
        error={dataPut.error}
        item={"max_number_read"}
        content={"Максимальное количество предложений при чтении: "}
      />
      <InputQuantity
        onDataSend={(value) => setMaxNumberRead(value)}
        content={"Максимальное количество предложений при чтении"}
        id={"max_number_read"}
        value={isMaxNumberRead}
        min={3}
        max={30}
      />

      <Error
        error={dataPut.error}
        item={"translation_list"}
        content={"Отображать перевод в списке слов: "}
      />
      <CheckBoxSimple
        onDataSend={(e) => setTranslationList(e.target.checked)}
        label={"Отображать перевод в списке слов"}
        description={"Этот список находится на странице Слова"}
        value={isTranslationList}
      />

      <button
        type="submit"
        className="
          block
          w-full
          px-12 py-3
          text-sm font-medium text-col_con
          bg-col_bright_4
          rounded-lg
          transition-colors cursor-pointer
          hover:bg-col_bright_2
        "
      >
        {dataPut.loading ? "СОХРАНЯЕМ" : "СОХРАНИТЬ"}
      </button>
    </form>
  );
};
export default Login;
