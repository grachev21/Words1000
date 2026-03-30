import { GrLinkNext } from "react-icons/gr";

const CardInfo = ({ name, icon: Icon, description, data, className }) => {
  return (
    <div className="w-full mt-4 mx-auto bg-linear-to-br from-col_bas_hig to-col_bas_mai rounded-lg border shadow-lg border-col_con/15">
      <div className="px-6 py-5">
        <div className="flex items-start">
          <div className="grow truncate">
            <div className="w-full sm:flex justify-between items-center mb-3">
              <h2 className="text-1xl leading-snug font-extrabold text-col_con_inv truncate mb-1 sm:mb-0">
                {name}
              </h2>
              <Icon className={className} />
            </div>
            <a
              href=""
              className="bg-col_bright_4/25 px-4 py-2 font-light text-xs rounded-lg text-col_con"
            >
              ПОСМОТРЕТЬ
            </a>
            <div className="flex items-end justify-between whitespace-normal mt-4">
              <div className="max-w-md text-indigo-100">
                <p className="mb-2">{description} </p>
              </div>
            </div>
            <div className="flex items-center">
              <GrLinkNext className="w-6 h-6 text-col_bright_3 mr-2" />
              <span className="text-2xl font-bold text-col_bright_1">
                {data}
              </span>
            </div>
          </div>
          <div className="flex flex-col mt-auto gap-2.5"></div>
        </div>
      </div>
    </div>
  );
};

export default CardInfo;
