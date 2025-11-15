// document.addEventListener("DOMContentLoaded", function () {
//   let readContainer = document.getElementById("read-container");
//   let answering = document.getElementById("answering");
//   let gameData = document.getElementById("game-data");
//   let gameContainer = document.getElementById("game-container");
//   let btnContainer = document.getElementById("btn-container");
//   let btnTemplate = document.getElementById("btn-template");

//   let gd = JSON.parse(gameData.textContent);

//   Object.keys(gd).forEach((key, index) => {
//     let clone = btnTemplate.content.cloneNode(true).firstElementChild;
//     clone.innerText = gd[key].en;
//     clone.dataset.index = index;
//     clone.dataset.option = gd[key].option;
//     clone.addEventListener("click", () => {
//       addBorder(key);
//     });
//     btnContainer.appendChild(clone);
//     console.log(gd[key]);
//   });

//   function addBorder(key) {
//     if (key == "option_true") {
//       readContainer.classList.remove("hidden");
//       readContainer.classList.add("block");
//       gameContainer.classList.add("hidden");
//       answering.classList.remove("hidden");
//       answering.classList.add("block");
//     } else {
//       gameContainer.classList.add("border", "border-col_attn");
//       setTimeout(() => {
//         gameContainer.classList.remove("border", "border-col_attn");
//         window.location.reload();
//       }, 1000);
//     }
//   }
// });
