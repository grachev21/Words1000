import { clsx } from "clsx";
import useGetRequestToken from "@/hooks/useGetRequestToken";
import Load from "@/components/other/Load";
import InfoMarker from "@/components/other/InfoMarker";

const AllWords = () => {
  const url = "/api/core/AllWords/";
  const dataWordsUser = useGetRequestToken(url);

  if (dataWordsUser.loading) return <Load />;

  return (
    <main
      className="w-full border border-col_con/15 rounded-lg flex flex-row
                        flex-wrap p-12 bg-liner-to-br from-col_bas_hig to-col_bas_mai shadow-lg"
    >
      <header className="w-full flex flex-row mb-8 m-1">
        <InfoMarker styleClass={"bg-col_bright_1"} content={"Неизвестно"} />
        <InfoMarker styleClass={"bg-col_bright_2"} content={"Изучаю"} />
        <InfoMarker styleClass={"bg-col_bright_3"} content={"Повторяю"} />
        <InfoMarker styleClass={"bg-col_bright_4"} content={"Изучил"} />
      </header>

      {dataWordsUser.data.map((item, index) => (
        <div key={index} className="w-6 h-6 flex justify-center items-center group">
          <div
            className={clsx(
              "rounded-full m-1 p-2 relative",
              item.status === 1 && "bg-col_bright_1 group-hover:bg-col_bright_5/70",
              item.status === 2 && "bg-col_bright_2 group-hover:bg-col_bright_5/70",
              item.status === 3 && "bg-col_bright_3 group-hover:bg-col_bright_5/70",
              item.status === 4 && "bg-col_bright_4 group-hover:bg-col_bright_5/70",
            )}
          >
            <p
              className="text-col_con font-bold absolute bg-col_bright_4
                            z-50 p-2 rounded-lg border border-col_con/15 cursor-none
                            shadow-md -top-14 left-9 invisible group-hover:visible"
            >
              {item.word} {item.id}
            </p>
          </div>
        </div>
      ))}
    </main>
  );
};

export default AllWords;
