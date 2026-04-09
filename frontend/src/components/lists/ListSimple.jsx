const ListSimple = ({ item }) => {
  return (
    <div className="border border-col_suc_mai rounded-lg p-4 hover:shadow-md transition-shadow">
      <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2 mb-2">
        <h5 className="text-lg font-semibold text-col_con">{item.core_words.word_en}</h5>
        <span className="text-sm text-col_con_inv">{item.created_at}</span>
      </div>

      <p className="text-col_con mb-2">{item.core_words.word_ru}</p>
      <p className="text-sm text-col_con_inv mb-3">{item.core_words.transcription}</p>

      <div className="flex flex-wrap items-center gap-2">
        <span className="text-sm text-col_con_inv">Статус:</span>
        <div className="px-3 py-1 rounded-full text-xs font-medium text-col_bright_3">
          {item.status}
        </div>

        <span className="text-sm text-col_con_inv">Повторов:</span>
        <span className="px-3 py-1 rounded-full bg-blue-100 text-blue-800 text-xs font-medium">
          {item.number_repetitions}
        </span>
      </div>
    </div>
  );
};
export default ListSimple;
