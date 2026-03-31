import React, { useState } from "react";
import Load from "@/components/other/Load";
import ListSimple from "@/components/list/ListSimple";
import FilterItem from "@/components/filters/FilterItem";
import useGetRequestToken from "@/hooks/useGetRequestToken";
import Paginator from "@/components/paginations/Paginator";

const statusOptions = [
  { value: "", label: "Все" },
  { value: "1", label: "Неизвестно" },
  { value: "2", label: "Изучаю" },
  { value: "3", label: "Повторяю" },
  { value: "4", label: "Изучил" },
];

const ListWord = () => {
  const [page, setPage] = useState(1);
  const [status, setStatus] = useState("");

  // Строим URL с параметрами
  const params = new URLSearchParams({ page });
  if (status) params.append("status", status);

  const dataAllWords = useGetRequestToken(`api/users/ListWord/?${params}`);
  console.log(`api/users/ListWord/?${params}`)

  // Сброс страницы при смене фильтра
  const handleStatusChange = (newStatus) => {
    setStatus(newStatus);
    setPage(1);
  };

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  if (dataAllWords.loading) return <Load />;

  return (
    <main>
      {/* Фильтр по статусам */}
      <div className="flex gap-2 mb-4 flex-wrap">
        {statusOptions.map((option) => (
          <button
            key={option.value}
            onClick={() => handleStatusChange(option.value)}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors
              ${status === option.value
                ? "bg-col_bright_2 text-col_con"
                : "bg-col_bright_1 hover:bg-col_bright_4 text-col_con"
              }`}
          >
            {option.label}
          </button>
        ))}
      </div>

      <div className="space-y-3">
        {dataAllWords.data?.results?.map((item, index) => (
          <ListSimple key={index} item={item} />
        ))}
      </div>

      {dataAllWords.data && (
        <Paginator
          data={dataAllWords.data}
          handlePageChange={handlePageChange}
          currentPage={page}
        />
      )}
    </main>
  );
};

export default ListWord;