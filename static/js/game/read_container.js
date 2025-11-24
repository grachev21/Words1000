import Tools from "../Tools.js";

class Carousel {
  constructor() {
    this.tools = new Tools();
    this.slideWidth = 640;
    this.line = document.getElementById("line-carousel");
    this.quantityCards = this.line.querySelectorAll("section").length;
    this.currentPosition = 0;
    this.currentSlide = 1;

    this.init();
  }

  init() {
    this.line.style.left = `${this.currentPosition}px`;
    this.updateCounter();
    this.actionBtn();
  }

  next() {
    if (this.currentSlide < this.quantityCards) {
      this.currentPosition -= this.slideWidth;
      this.line.style.left = `${this.currentPosition}px`;
      this.currentSlide++;
      this.updateCounter();
    }
  }

  back() {
    if (this.currentSlide > 1) {
      this.currentPosition += this.slideWidth;
      this.line.style.left = `${this.currentPosition}px`;
      this.currentSlide--;
      this.updateCounter();
    }
  }

  updateCounter() {
    const counter = document.getElementById("carousel-counter");
    if (counter) {
      counter.innerText = `${this.currentSlide}/${this.quantityCards}`;
    }
  }

  translatePhrases() {
    const elements = document.querySelectorAll("#russian-words-translate");
    const currentElement = elements[this.currentSlide - 1];

    if (currentElement) {
      currentElement.classList.toggle("opacity-0");
    }
  }

  // Initialize buttons
  actionBtn() {
    this.tools.onClickMethod({
      id: "translate-phrases",
      fun: this.translatePhrases.bind(this),
    });
    this.tools.onClickMethod({ id: "next-done", fun: this.next.bind(this) });
    this.tools.onClickMethod({ id: "back-done", fun: this.back.bind(this) });
  }
}

export default Carousel;
