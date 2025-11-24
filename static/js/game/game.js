import Carousel from "./read_container.js";
import Tools from "../Tools.js";

class Game {
  constructor() {
    this.tools = new Tools();
    this.carousel = new Carousel();

    this.readContainer = document.getElementById("read-container");
    this.answering = document.getElementById("answering");
    this.gameContainer = document.getElementById("game-container"); // Общий контейнер с кнопками
    this.btnContainer = document.getElementById("btn-container"); // Контейнер с кнопками
    this.btnTemplate = document.getElementById("btn-template"); // Шаблон из html
    this.init();
  }
  init() {
    let data = JSON.parse(document.getElementById("game-data").textContent);
    this.tools.createTemplate(
      "btn-template",
      "btn-container",
      data,
      this.addBorder.bind(this),
      "click"
    );
  }

  addBorder(key) {
    if (key != "true") {
      this.gameContainer.classList.add("border", "border-col_attn");
      setTimeout(() => {
        this.gameContainer.classList.remove("border", "border-col_attn");
        htmx.ajax("GET", "/game/", { target: "#main-content" });
      }, 1000);
    }
  }

  // addBorder(key) {
  //   if (key == "true") {
  //     this.readContainer.classList.add("block");
  //     this.gameContainer.classList.add("hidden");
  //     this.answering.classList.remove("hidden");
  //     this.answering.classList.add("block");
  //   } else {
  //     this.gameContainer.classList.add("border", "border-col_attn");
  //     setTimeout(() => {
  //       this.gameContainer.classList.remove("border", "border-col_attn");
  //       window.location.reload();
  //     }, 1000);
  //   }
  // }
}

export default Game;
