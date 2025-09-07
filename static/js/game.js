document.addEventListener("DOMContentLoaded", function () {
  const readContainer = document.getElementById("read-container");
  const answering = document.getElementById("answering");
  const gameData = document.getElementById("game-data");
  const gameContainer = document.getElementById("game-container");
  const btnContainer = document.getElementById("btn-container");
  const btnTemplate = document.getElementById("btn-template");

  const gd = JSON.parse(gameData.textContent);

  gd.forEach((element, index) => {
    const clone = btnTemplate.content.cloneNode(true).firstElementChild;
    clone.innerText = element.en;
    clone.dataset.index = index;
    clone.dataset.option = element.option;
    clone.addEventListener("click", () => {
      addBorder(element);
    });
    btnContainer.appendChild(clone);
    console.log(element);
  });

  function addBorder(e) {
    console.log(e.option);
    if (e.option == 1) {
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
});
