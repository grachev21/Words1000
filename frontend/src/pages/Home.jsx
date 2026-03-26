import useGetRequestToken from "@/hooks/useGetRequestToken";
import TitleAndDescription from "@/components/text/Typography";
import AllWords from "@/components/organism/AllWords";
import CardInfo from "@/components/cards/CardInfo";
import Chart from "@/components/organism/Chart";

import { FaDatabase, FaBookReader } from "react-icons/fa";
import { MdEventRepeat } from "react-icons/md";
import { TbWriting } from "react-icons/tb";
import { MdTranslate } from "react-icons/md";

import Load from "@/components/other/Load";
import { GrStatusUnknown } from "react-icons/gr";

const Home = () => {
  const dataWoordsSettings = useGetRequestToken("core/api/CardInfoSettings/");
  const dataWordsUser = useGetRequestToken("users/api/RemainderCardInfo/");

  if (dataWoordsSettings.loading) return <Load />;
  if (dataWordsUser.loading) return <Load />;
  console.log(dataWordsUser.data);

  return (
    <main>
      <TitleAndDescription
        start={"Все слова,"}
        center={"|_Тут"}
        finish={"!"}
        description={"Пробегает вся 1000 слов, те которые вы уже выучили имеют странный вид..."}
      />

      <AllWords />

      <TitleAndDescription
        start={"Ваши настройки"}
        center={"|_Тут"}
        finish={"!"}
        description={"Все ваши установки и достижения"}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-8">
        <CardInfo
          name={"Количество слов за день"}
          icon={FaDatabase}
          description={"Это то количество слов которые вы должны выучить за один день"}
          className="text-col_bright_1 w-7 h-7"
          data={dataWoordsSettings.data[0].number_words}
        />

        <CardInfo
          name={"Количество повторов"}
          icon={MdEventRepeat}
          description={"Это количество повторов при заучивании"}
          className="text-col_bright_2 w-7 h-7"
          data={dataWoordsSettings.data[0].number_repetitions}
        />

        <CardInfo
          name={"Набор слова"}
          icon={TbWriting}
          description={"Сколько раз набрать слово при заучивании"}
          className="text-col_bright_3 w-7 h-7"
          data={dataWoordsSettings.data[0].number_write}
        />

        <CardInfo
          name={"Количество предложений"}
          icon={FaBookReader}
          description={"Это количество предложений которое вы будите читать с заучиваемым словом"}
          className="text-col_bright_4 w-7 h-7"
          data={dataWoordsSettings.data[0].max_number_read}
        />

        <CardInfo
          name={"Перевод слов в списке"}
          icon={MdTranslate}
          description={"Это то количество слов которые вы должны выучить за один день"}
          className="text-col_bright_5 w-7 h-7"
          data={dataWoordsSettings.data[0].translation_list ? "Да" : "Нет"}
        />
      </div>

      <TitleAndDescription
        start={"Ваши достижения на сегодня"}
        center={"|_Тут"}
        finish={"!"}
        description={"Все ваши установки и достижения"}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-8">
        <CardInfo
          name={"Оставлось выучить за сегодня"}
          icon={FaBookReader}
          description={"Это то количество слов которые вы должны выучить за один день"}
          className="text-col_bright_1 w-7 h-7"
          data={dataWordsUser.data.remainder_day}
        />

        <CardInfo
          name={"Все"}
          icon={FaDatabase}
          description={"Общее количество слов"}
          className="text-col_bright_2 w-7 h-7"
          data={dataWordsUser.data.remainder_all}
        />

        <CardInfo
          name={"Неизвестно"}
          icon={GrStatusUnknown}
          description={"Общее количество слов которые вы еще не заучили"}
          className="text-col_bright_3 w-7 h-7"
          data={dataWordsUser.data.unknown}
        />

        <CardInfo
          name={"Изучаю"}
          icon={FaBookReader}
          description={"Количество слов которые вы изучаете"}
          className="text-col_bright_4 w-7 h-7"
          data={dataWordsUser.data.unknown}
        />

        <CardInfo
          name={"Повторяю"}
          icon={MdEventRepeat}
          description={"Количество слов которые вы повторяете"}
          className="text-col_bright_5 w-7 h-7"
          data={dataWordsUser.data.repetition}
        />

        <CardInfo
          name={"Изучил"}
          icon={FaBookReader}
          description={"Количество слов которые вы уже выучили"}
          className="text-col_bright_6 w-7 h-7"
          data={dataWordsUser.data.repetition}
        />
      </div>

      <Chart />
    </main>
  );
};
export default Home;
