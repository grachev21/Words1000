document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("game_word");
  const elements = Array.from(container.children);
  const game_container = document.getElementById("game_container");
  const correct_btn = document.getElementById("correct_btn");
  const answering = document.getElementById("answering");
  const correctAnswer = JSON.parse(
    document.getElementById("game-data").textContent,
  );
  console.log(correctAnswer);

  // MIXES THE BUTTONS IN RANDOM ORDER
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  shuffleArray(elements);

  container.innerHTML = "";
  elements.forEach((el) => container.appendChild(el));

  // CLICK HANDLER
  elements.forEach((element) => {
    element.addEventListener("click", function () {
      if (element.textContent.trim() === correctAnswer) {
        console.log(element);
        game_container.classList.add("hidden");
        answering.classList.add("flex");
      } else {
        game_container.classList.add("border");
        game_container.classList.add("border-col_attn");
        setTimeout(() => {
          location.reload();
        }, 1000);
      }
    });
  });

  // Continue button handler
  correct_btn.addEventListener("click", function () {
    console.log("check...");
    document.getElementById("read_container").classList.remove("hidden");
    document.getElementById("answering").classList.remove("hidden");
    document.getElementById("game_container").classList.add("hidden");
  });
});
