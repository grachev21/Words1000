document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("game_word");
  const elements = Array.from(container.children);
  const game_container = document.getElementById("game_container");
  const correct_btn = document.getElementById("correct_btn");
  const answering = document.getElementById("answering");
  const gameData = JSON.parse(document.getElementById("game-data").textContent);

  container.innerHTML = "";
  elements.forEach((el) => container.appendChild(el));

  console.log(gameData);
  // CLICK HANDLER
  Array.isAgameData.forEach((element) => {
    console.log(element.en);
  });

  // Continue button handler
  correct_btn.addEventListener("click", function () {
    console.log("check...");
    document.getElementById("read_container").classList.remove("hidden");
    document.getElementById("answering").classList.remove("hidden");
    document.getElementById("game_container").classList.add("hidden");
  });
});
