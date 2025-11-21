const Game = () => {
  let readContainer = document.getElementById("read-container");
  let answering = document.getElementById("answering");
  let gameContainer = document.getElementById("game-container"); // Общий контейнер с кнопками
  let btnContainer = document.getElementById("btn-container"); // Контейнер с кнопками
  let btnTemplate = document.getElementById("btn-template"); // Шаблон из html

  // Данные с сервера
  let gameData = JSON.parse(document.getElementById("game-data").textContent);
  console.log(gameData);

  // Перебираем данные с сервера
  gameData.forEach((value, index) => {
    console.log(value);
    // Создает копию шаблона true означает копирование со всем содержимым
    // firstElementChild Извлекает первый элемент из DocumentFragment
    let clone = btnTemplate.content.cloneNode(true).firstElementChild;
    clone.innerText = value.en;
    clone.addEventListener("click", () => {
      addBorder(value.option);
    });
    btnContainer.appendChild(clone);
  });

  function addBorder(key) {
    console.log(key);
    if (key == "true") {
      readContainer.classList.remove("hidden");
      readContainer.classList.add("block");
      gameContainer.classList.add("hidden");
      answering.classList.remove("hidden");
      answering.classList.add("block");
    } else {
      gameContainer.classList.add("border", "border-col_attn");
      setTimeout(() => {
        gameContainer.classList.remove("border", "border-col_attn");
        window.location.reload();
      }, 1000);
    }
  }
};

export default Game;
