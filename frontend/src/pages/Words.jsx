import ListWord from "@/components/organism/ListWord";
import CardWord from "@/components/organism/CardWord";
import TabButton from "@/components/buttons/TabButton";
import { useState } from "react";

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

        {isActiveTab == "tab1" && (
          <div className="p-4 rounded-lg">
            <ListWord />
            list word
          </div>
        )}

        {isActiveTab == "tab2" && (
          <div className="p-4 rounded-lg">
            <CardWord />
            card word
          </div>
        )}
      </div>
    </main>
  );
};
export default Words;
