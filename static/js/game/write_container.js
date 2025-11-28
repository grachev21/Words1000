class WriteContainer {
    constructor() {
        // this. settings = JSON.parse(document.getElementById("settings-data").textContent)
        this.input = document.getElementById("input-text-en");
        this.init();
    }

    init() {
        this.changeColorError();
    }

    // sessionStorageData(){
    //     let data = JSON.parse(document.getElementById("game-data").textContent);
    // }
    changeColorError() {
        this.input.addEventListener("input", (e) => {
            this.strInput = e.target.value;

            if (
                this.strInput !==
                this.input.dataset.word.slice(0, this.strInput.length)
            ) {
                this.input.classList.replace(
                    "text-col_suc_ave",
                    "text-col_attn",
                );
                this.input.classList.replace("text-col_con", "text-col_attn");
            } else if (this.strInput.length == 0) {
                this.input.classList.replace(
                    "text-col_attn",
                    "text-col_suc_ave",
                );
                this.input.classList.replace(
                    "text-col_con",
                    "text-col_suc_ave",
                );
            } else {
                this.input.classList.replace("text-col_attn", "text-col_con");
                this.input.classList.replace(
                    "text-col_suc_ave",
                    "text-col_con",
                );
            }
        });
    }
}
export default WriteContainer;
