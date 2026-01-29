const TitleDescription = ({ start, center, finish, description }) => {
  return (
    <div class="mb-22 mt-44">
      <div>
        <span class="text-col_con text-3xl font-bold">{start}</span>
        <span class="text-col_bright_6 text-3xl font-bold">{center}</span>
        <span class="text-col_con text-3xl font-bold">{finish}</span>
      </div>
      <p class="text-col_con_inv mt-4">{description}</p>
    </div>
  );
};
export default TitleDescription;
