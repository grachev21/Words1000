document.addEventListener("DOMContentLoaded", function () {
  const readContainer = document.getElementById("read-container");
  const answering = document.getElementById("answering");
  const gameData = document.getElementById("game-data");
  const gameContainer = document.getElementById("game-container");
  const btnContainer = document.getElementById("btn-container");
  const btnTemplate = document.getElementById("btn-template");

  const gd = JSON.parse(gameData.textContent);

  Object.keys(gd).forEach((key, index) => {
    const clone = btnTemplate.content.cloneNode(true).firstElementChild;
    clone.innerText = gd[key].en;
    clone.dataset.index = index;
    clone.dataset.option = gd[key].option;
    clone.addEventListener("click", () => {
      addBorder(key);
    });
    btnContainer.appendChild(clone);
    console.log(gd[key]);
  });

  function addBorder(key) {
    if (key == "option_true") {
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
