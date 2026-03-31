import ReactPaginate from "react-paginate";

const Paginator = ({ data, handlePageChange, currentPage = 1 }) => {
  if (!data?.count) return null;

  const pageCount = Math.ceil(data.count / 10); // если page_size = 10

  const handlePageClick = (event) => {
    handlePageChange(event.selected + 1); // ReactPaginate считает с 0
  };

  return (
    <div className="flex mt-8 mb-6 justify-center">
      <ReactPaginate
        previousLabel="Назад"
        nextLabel="Вперёд"
        pageCount={pageCount}
        marginPagesDisplayed={2}
        pageRangeDisplayed={5}
        onPageChange={handlePageClick}
        forcePage={currentPage - 1} // важно для синхронизации
        // ==================== Tailwind классы ====================
        containerClassName="flex items-center gap-1.5 flex-wrap justify-center" // общий контейнер
        pageClassName="page-item"
        pageLinkClassName="px-4 py-2.5 text-sm font-medium rounded-lg bg-col_bright_1
                    hover:bg-col_bright_4 transition-colors cursor-pointer
                    flex items-center justify-center min-w-10.5 text-col_con"
        activeClassName="active"
        activeLinkClassName="bg-col_bright_2 text-col_con"
        previousClassName="page-item"
        previousLinkClassName="px-4 py-2.5 text-sm text-col_con font-medium rounded-lg 
                    bg-col_bright_5 hover:bg-col_bright_2 border cursor-pointer"
        nextClassName="page-item"
        nextLinkClassName="px-4 py-2.5 text-sm text-col_con font-medium rounded-lg 
                    bg-col_bright_5 hover:bg-col_bright_2 border cursor-pointer"
        breakClassName="page-item"
        breakLinkClassName="px-4 py-2.5 text-sm font-medium text-col_con_inv"
        disabledClassName="disabled opacity-50 pointer-events-none"
      />
    </div>
  );
};

export default Paginator;
