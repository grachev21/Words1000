import { useState } from "react";
import { ListWord, TabButton } from "@/components";


const Words = () => {
  const [isActiveTab, setActiveTab] = useState("tab1");

  return (
    <main>
      <div className="w-full border border-col_con/15 rounded-lg p-6">
        <div className="flex justify-center space-x-4">
          <TabButton
            name={"Список слов"}
            tab={"tab1"}
            isActiveTab={isActiveTab}
            setActiveTab={setActiveTab}
          />
          <TabButton
            name={"Карточки слов"}
            tab={"tab2"}
            isActiveTab={isActiveTab}
            setActiveTab={setActiveTab}
          />
        </div>
        <div className="p-4 rounded-lg">
          <ListWord isActiveTab={isActiveTab} />
        </div>
      </div>
    </main>
  );
};
export default Words;
