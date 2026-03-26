const InfoMarker = ({ styleClass, content }) => {
    return (
        <div className="flex flex-row items-center text-col_con ml-6">
            <div
                className={`p-1 h-4 w-4 my-2 rounded-full ${styleClass}`}
            ></div>

            <p className="ml-4 font-light">{content}</p>
        </div>
    );
};

export default InfoMarker;
