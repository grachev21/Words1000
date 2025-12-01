class WriteContainer {
  constructor() {
    this.data = JSON.parse(
      document.getElementById("user-settings").textContent
    );
    this.inputEn = document.getElementById("input-text-en");
    this.inputRu = document.getElementById("input-text-ru");
    this.en = false;
    this.blackout = document.getElementById("screen-blackout");
    this.counter = document.getElementById("counter-write");
    this.init();
  }

  init() {
    this.changeColorError();
    this.counter.textContent = this.data.number_write;
  }

  errorColor() {
    this.inputEn.classList.replace("text-col_suc_ave", "text-col_attn");
    this.inputEn.classList.replace("text-col_con", "text-col_attn");
  }
  normalColor() {
    this.inputEn.classList.replace("text-col_attn", "text-col_suc_ave");
    this.inputEn.classList.replace("text-col_con", "text-col_suc_ave");
  }
  executionColor() {
    this.inputEn.classList.replace("text-col_attn", "text-col_con");
    this.inputEn.classList.replace("text-col_suc_ave", "text-col_con");
  }

  visibleInvisible(optionInput) {
    if (optionInput == "en") {
      this.en = false;
      this.inputEn.classList.remove("invisible");
      this.inputEn.value = "";
      this.inputEn.focus();
      this.inputRu.classList.add("invisible");
    } else {
      this.en = true;
      this.inputRu.classList.remove("invisible");
      this.inputRu.value = "";
      this.inputRu.focus();
      this.inputEn.classList.add("invisible");
    }
  }

  blackoutRun(typeRun) {
    typeRun
      ? ((this.blackout.value = this.data.number_write),
        this.data.number_write--,
        (this.blackout.querySelector("div").textContent =
          this.data.number_write),
        this.blackout.classList.remove("invisible"),
        (this.counter.textContent = this.data.number_write))
      : (this.blackout.classList.add("invisible"),
        this.inputEn.classList.replace("text-col_con", "text-col_suc_ave"));
  }
  moveNextWord() {
    if (!this.data.number_write <= 0) {
      this.blackoutRun(true);
      setTimeout(() => {
        this.inputEn.classList.replace("text-col_con", "text-col_suc_ave");
        this.blackoutRun(false);
        this.visibleInvisible("en");
      }, 1000);
    }
  }

  inputSwitch() {
    !this.en ? this.visibleInvisible("ru") : none;
  }

  tracker(languish_data, fun) {
    languish_data.addEventListener("input", (e) => {
      this.strInput = e.target.value;
      if (
        this.strInput !==
        languish_data.dataset.word.slice(0, this.strInput.length)
      ) {
        this.errorColor();
      } else if (this.strInput.length == 0) {
        this.normalColor();
      } else if (this.strInput == languish_data.dataset.word) {
        fun();
      } else {
        this.executionColor();
      }
    });
  }
  changeColorError() {
    // Прячем русский input
    this.visibleInvisible("en");
    // Отслеживает английский input
    this.tracker(this.inputEn, this.inputSwitch.bind(this));
    // Отслеживает русский input
    this.tracker(this.inputRu, this.moveNextWord.bind(this));
  }
}
export default WriteContainer;
