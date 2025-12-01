class WriteContainer {
    constructor() {
        this.data = JSON.parse(
            document.getElementById("user-settings").textContent,
        );
        this.data_correct_word = JSON.parse(
            document.getElementById("game-data-correct-word").textContent,
        );
        console.log(this.data_correct_word);
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

    errorColor(typeError) {
        let element = typeError == "en" ? this.inputEn : this.inputRu;
        element.classList.replace("text-col_suc_ave", "text-col_attn");
        element.classList.replace("text-col_con", "text-col_attn");
    }
    normalColor(typeError) {
        let element = typeError == "en" ? this.inputEn : this.inputRu;
        element.classList.replace("text-col_attn", "text-col_suc_ave");
        element.classList.replace("text-col_con", "text-col_suc_ave");
    }
    executionColor(typeError) {
        let element = typeError == "en" ? this.inputEn : this.inputRu;
        element.classList.replace("text-col_attn", "text-col_con");
        element.classList.replace("text-col_suc_ave", "text-col_con");
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

    postRequest(wordId) {
        async function sendWordSelection(wordId) {
            const csrfToken = document.querySelector(
                "[name=csrfmiddlewaretoken]",
            ).value;

            const formData = new FormData();
            // Добавляем поля из твоей формы WordCheck (обязательно!)
            // Если форма пустая — можно ничего не добавлять, но лучше добавить хотя бы одно поле
            formData.append("select_data", wordId); // это то, что ты ловишь в view

            // Если у твоей формы WordCheck есть другие обязательные поля — добавь их тоже!
            // Например: formData.append('some_field', 'value');

            try {
                const response = await fetch('{% url "game" %}', {
                    // или точный URL
                    method: "POST",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest", // важно для Django (или 'HX-Request' если через htmx)
                        "X-CSRFToken": csrfToken,
                    },
                    body: formData,
                    credentials: "same-origin",
                });

                if (response.ok) {
                    const html = await response.text();
                    // Если используешь HTMX — он сам заменит блок
                    // Если чистый JS — заменяешь вручную:
                    document.querySelector("#game-block").innerHTML = html;
                } else {
                    console.error("Ошибка:", response.status);
                }
            } catch (err) {
                console.error("Fetch error:", err);
            }
        }
    }

    blackoutRun(typeRun) {
        if (typeRun) {
            this.blackout.value = this.data.number_write;
            this.data.number_write--;
            this.blackout.querySelector("div").textContent =
                this.data.number_write;
            this.blackout.classList.remove("invisible");
            this.counter.textContent = this.data.number_write;
        } else {
            this.blackout.classList.add("invisible");
            this.inputEn.classList.replace("text-col_con", "text-col_suc_ave");

            console.log(this.blackout.value);
            if (this.data.number_write == 0) {
                this.postRequest();
            }
        }
    }
    moveNextWord() {
        if (!this.data.number_write <= 0) {
            this.blackoutRun(true);
            setTimeout(() => {
                this.inputEn.classList.replace(
                    "text-col_con",
                    "text-col_suc_ave",
                );
                this.blackoutRun(false);
                this.visibleInvisible("en");
            }, 1000);
        }
    }

    inputSwitch() {
        !this.en ? this.visibleInvisible("ru") : none;
    }

    tracker(languish_data, fun, typeError) {
        languish_data.addEventListener("input", (e) => {
            this.strInput = e.target.value;
            if (
                this.strInput !==
                languish_data.dataset.word.slice(0, this.strInput.length)
            ) {
                this.errorColor(typeError);
            } else if (this.strInput.length == 0) {
                this.normalColor(typeError);
            } else if (this.strInput == languish_data.dataset.word) {
                fun();
            } else {
                this.executionColor(typeError);
            }
        });
    }
    changeColorError() {
        // Прячем русский input
        this.visibleInvisible("en");
        // Отслеживает английский input
        this.tracker(this.inputEn, this.inputSwitch.bind(this), "en");
        // Отслеживает русский input
        this.tracker(this.inputRu, this.moveNextWord.bind(this), "ru");
    }
}
export default WriteContainer;
