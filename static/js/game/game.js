// import Carousel from "./read_container.js";
// import Tools from "../Tools.js";
// import WriteContainer from "./write_container.js";

// class Game {
//   constructor() {
//     new WriteContainer();
//     new Carousel();

//     this.tools = new Tools();

//     this.readContainer = document.getElementById("read-container");
//     this.writeContainer = document.getElementById("write-container");
//     this.answering = document.getElementById("answering");
//     this.gameContainer = document.getElementById("game-container");
//     this.btnContainer = document.getElementById("btn-container");
//     this.btnTemplate = document.getElementById("btn-template");
//     this.init();
//   }
//   init() {
//     let data = JSON.parse(document.getElementById("game-data").textContent);
//     this.tools.createTemplate(
//       "btn-template",
//       "btn-container",
//       data,
//       this.trackingResponse.bind(this),
//       "click"
//     );
//   }

//   trackingResponse(key) {
//     if (key != "true") {
//       this.gameContainer.classList.add("border", "border-col_attn");
//       console.log("red");
//       setTimeout(() => {
//         this.gameContainer.classList.remove("border", "border-col_attn");
//         // htmx.ajax("GET", "/game/", { target: "#main-content" });
//       }, 1000);
//     } else {
//       this.gameContainer.classList.add(
//         "border",
//         "border-col_suc",
//         "transition-all"
//       );
//       setTimeout(() => {
//         this.gameContainer.classList.replace("flex", "hidden");
//         this.writeContainer.classList.replace("hidden", "flex");
//       }, 1000);
//     }
//   }

//   showReadContainer() {}
// }

// export default Game;
