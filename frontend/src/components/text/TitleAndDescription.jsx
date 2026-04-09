const TitleAndDescription = ({ start, center, finish, description }) => {
    return (
        <div className="mb-22 mt-44">
            <div>
                <span className="text-col_con text-3xl font-bold">{start}</span>
                <span className="text-col_bright_6 text-3xl font-bold">
                    {center}
                </span>
                <span className="text-col_con text-3xl font-bold">
                    {finish}
                </span>
            </div>
            <p className="text-col_con_inv mt-4">{description}</p>
        </div>
    );
};
export default TitleAndDescription;
