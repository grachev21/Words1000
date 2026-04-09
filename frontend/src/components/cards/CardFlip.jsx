import { useState } from "react";
import ButtonLight from "@/components/buttons/ButtonLight";
import Button from "@/components/buttons/Button";

const CardFlip = ({ item }) => {
  const [flipped, setFlipped] = useState(false);

  return (
    <main>
      <div className="w-64 h-86 m-8" style={{ perspective: "1000px" }}>
        <div
          style={{
            transformStyle: "preserve-3d",
            transition: "transform 0.7s cubic-bezier(0.4, 0, 0.2, 1)",
            transform: flipped ? "rotateY(180deg)" : "rotateY(0deg)",
            position: "relative",
            width: "100%",
            height: "100%",
          }}
        >
          {/* Передняя сторона */}
          <div
            className="absolute w-full h-full border border-col_con/15 rounded-xl shadow-lg p-6 flex flex-col justify-center items-center"
            style={{ backfaceVisibility: "hidden" }}
          >
            <h3 className="text-3xl font-bold text-col_con_inv mb-2">{item.core_words.word_en}</h3>
            <Button content="Перевернуть" onClick={() => setFlipped(true)} />
          </div>

          {/* Задняя сторона */}
          <div
            className="absolute w-full h-full bg-linear-to-br from-col_bright_1 to-col_bas_mai text-col_con rounded-xl shadow-lg p-6 flex flex-col justify-center items-center border border-col_con/15"
            style={{
              backfaceVisibility: "hidden",
              transform: "rotateY(180deg)",
            }}
          >
            <h3 className="text-2xl font-bold mb-2">Ответ</h3>
            <p className="text-center">{item.core_words.word_ru}</p>
            <ButtonLight content="Назад" className="mt-4" onClick={() => setFlipped(false)} />
          </div>
        </div>
      </div>
    </main>
  );
};

export default CardFlip;
