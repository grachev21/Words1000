import React, { useState } from "react";
import Load from "@/components/other/Load";
import ListSimple from "@/components/lists/ListSimple";
import useGetRequestToken from "@/hooks/useGetRequestToken";
import Paginator from "@/components/paginations/Paginator";
import BorderButton from "@/components/buttons/BorderButton";
import statusOptions from "@/assets/statusOption";
import CardFlip from "@/components/cards/CardFlip";

const ListWord = ({ isActiveTab }) => {
  const [page, setPage] = useState(1);
  const [status, setStatus] = useState("");

  // Строим URL с параметрами
  const params = new URLSearchParams({ page });
  if (status) params.append("status", status);

  const dataAllWords = useGetRequestToken(`api/users/ListWord/?${params}`);
  console.log(`api/users/ListWord/?${params}`);

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
        {statusOptions.map((option, index) => (
          <BorderButton
            key={index}
            onClick={() => handleStatusChange(option.value)}
            active={status}
            value={option.value}
            content={option.label}
          />
        ))}
      </div>

      <div
        className={
          isActiveTab === "tab2"
            ? "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
            : undefined
        }
      >
        {dataAllWords.data?.results?.map((item, index) => (
          <div key={index}>
            {isActiveTab === "tab1" && <ListSimple item={item} />}
            {isActiveTab === "tab2" && <CardFlip item={item} />}
          </div>
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
