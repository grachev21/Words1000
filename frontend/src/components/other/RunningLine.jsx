<main
  className="w-full border border-col_con/15 rounded-lg flex flex-row 
        flex-wrap p-12 bg-linear-to-br from-col_bas_hig to-col_bas_mai shadow-lg"
>
  <header className="w-full flex flex-row mb-8 m-1">
    <div className="flex flex-row items-center text-col_con">
      <div className="bg-col_bright_1 p-1 h-4 w-4 my-2 rounded-full"></div>
      <p className="ml-4 font-light">Неизвестно</p>
    </div>
    <div className="flex flex-row items-center text-col_con ml-10">
      <div className="bg-col_bright_2 p-1 h-4 w-4 my-2 rounded-full"></div>
      <p className="ml-4 font-light">Изучаю</p>
    </div>
    <div className="flex flex-row items-center text-col_con ml-10">
      <div className="bg-col_bright_3 p-1 h-4 w-4 my-2 rounded-full"></div>
      <p className="ml-4 font-light">Повторяю</p>
    </div>
    <div className="flex flex-row items-center text-col_con ml-10">
      <div className="bg-col_bright_4 p-1 h-4 w-4 my-2 rounded-full"></div>
      <p className="ml-4 font-light">Изучил</p>
    </div>
  </header>

  {/* {% for word in all_words %}
        <div className="w-6 h-6 flex justify-center items-center group">
            <div
            {% if word.status == '1' %}
            className="bg-col_bright_1 rounded-full m-1 p-2 relative group-hover:bg-col_bright_5/70"
            {% elif word.status == '2' %}
            className="bg-col_bright_2 rounded-full m-1 p-2 relative group-hover:bg-col_bright_5/70"
            {% elif word.status == '3' %}
            className="bg-col_bright_3 rounded-full m-1 p-2 relative group-hover:bg-col_bright_5/70"
            {% elif word.status == '4' %}
            className="bg-col_bright_4 rounded-full m-1 p-2 relative group-hover:bg-col_bright_5/70"
            {% endif %}
            >
            <p
                className="text-col_con font-bold absolute bg-col_bright_4
                z-50 p-2 rounded-lg border border-col_con/15 cursor-none
                shadow-md -top-14 left-9 invisible group-hover:visible"
            >
                {{word.core_words}} {{forloop.counter}}
            </p>
            </div>
        </div>
    {% endfor %} */}
</main>;
