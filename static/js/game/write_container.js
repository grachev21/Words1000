class WriteContainer {
    constructor() {
        this.max_number_read = this.getSettings().max_number_read;
        this.inputEn = document.getElementById("input-text-en");
        this.inputRu = document.getElementById("input-text-ru");
        this.en = false;
        this.blackout = document.getElementById("screen-blackout");
        this.counter = document.getElementById("counter-write");
        this.init();
    }

    init() {
        this.changeColorError();
        this.counter.textContent = this.max_number_read;
    }

    getSettings() {
        return JSON.parse(document.getElementById("user-settings").textContent);
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
    moveNextWord() {
        this.blackout.value = this.max_number_read;
        if (!this.max_number_read <= 0) {
            this.max_number_read--;
            this.blackout.querySelector("div").textContent =
                this.max_number_read;
            this.blackout.classList.remove("invisible");
            this.counter.textContent = this.max_number_read;
            setTimeout(() => {
                this.inputEn.value = "";
                this.blackout.classList.add("invisible");
            }, 1000);
        }
    }

    wordSwithc() {
        if (!this.en) {
            this.en = true;
            this.inputRu.classList.remove("hidden");
            this.inputEn.classList.add("hidden");
        }
    }
    changeColorError() {
        this.inputEn.addEventListener("input", (e) => {
            this.strInput = e.target.value;

            if (
                this.strInput !==
                this.inputEn.dataset.word.slice(0, this.strInput.length)
            ) {
                this.errorColor();
            } else if (this.strInput.length == 0) {
                this.normalColor();
            } else if (this.strInput == this.inputEn.dataset.word) {
                this.wordSwithc();
                // this.moveNextWord();
            } else {
                this.executionColor();
            }
        });

        this.inputRu.addEventListener("input", (e) => {
            this.strInput = e.target.value;
            console.log(this.strInput);
            console.log(
                this.strInput,
                this.inputRu.dataset.word.slice(0, this.strInput.length),
            );

            if (
                this.strInput !==
                this.inputRu.dataset.word.slice(0, this.strInput.length)
            ) {
                this.errorColor();
            } else if (this.strInput.length == 0) {
                this.normalColor();
            } else if (this.strInput == this.inputRu.dataset.word) {
                this.moveNextWord();
            } else {
                this.executionColor();
            }
        });
    }

    // settionStorage(){
    //     sessionStorage.sessionStorage("number": )
    // }
}
export default WriteContainer;
