import React, { useState, useEffect } from "react";
import Load from "@/components/other/Load";
import ListSimple from "@/components/list/ListSimple";
import FilterItem from "@/components/filters/FilterItem";
import useGetRequestToken from "@/hooks/useGetRequestToken";
import Paginator from "@/components/paginations/Paginator"; // переименуй позже

const ListWord = () => {
  const [page, setPage] = useState(1);

  // Добавляем зависимость от страницы
  const dataAllWords = useGetRequestToken(`api/users/ListWord/?page=${page}`);

  if (dataAllWords.loading) return <Load />;
  console.log(dataAllWords.data);

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  return (
    <main>
      <FilterItem />
      <div className="space-y-3">
        {dataAllWords.data.results.map((item, index) => (
          <ListSimple key={index} item={item} />
        ))}
      </div>

      {dataAllWords.data && (
        <Paginator data={dataAllWords.data} onChangePage={handlePageChange} currentPage={page} />
      )}
    </main>
  );
};

export default ListWord;
