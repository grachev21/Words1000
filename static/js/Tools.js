class Tools {
    /**
     * Обрабатывает клик и вызывает присланную функцию
     * @param {string} id - Элемент который нужно отслеживать
     * @param {function} fun - Функция которая должна вызваться при клике
     */
    onClickMethod({ id, fun }) {
        // Выполняет клик по id и вызывает fun

        document.getElementById(id).addEventListener("click", () => {
            fun.call(this);
        });
    }

    /**
     * Создает шаблоны по указанным данным и назначает на них функцию которая вызывается
     * по параметру typeEvent
     * @param {string} templateId - Ссылка на шаблон
     * @param {string} containerId - Контейнер в который будет вставляться контент
     * @param {list} data - Список данных которые нужно записать в шаблон
     * @param {function} fun - Функция которая назначается на элемент
     * @param {string} typeEvent - Событие по которому должна вызваться функция, click...
     */
    createTemplate(templateId, containerId, data, fun, typeEvent) {
        data.forEach((value) => {
            // Создает копию шаблона true означает копирование со всем содержимым
            // firstElementChild Извлекает первый элемент из DocumentFragment
            let clone = document
                .getElementById(templateId)
                .content.cloneNode(true).firstElementChild;
            clone.innerText = value.en;
            clone.addEventListener(typeEvent, () => {
                fun(value.option);
            });
            document.getElementById(containerId).appendChild(clone);
        });
    }
    /**
     * Показывает все что в idOpen п действию с idAction
     * @param {string} action - Тип действия, click, ...
     * @param {string} idOpen - Блок который нужно показать
     * @param {string} idAction - Блок по которому происходит действие
     */

    actionOpenClose(action, idOpen, idAction) {
        let element = document.getElementById(idAction);
        let idOpenBlock = document.getElementById(idOpen);

        // Проверяем data-атрибут
        if (element.dataset.menu === "true") {
            return;
        }

        element.addEventListener(action, () => {
            console.log("run function");
            if (idOpenBlock.classList.contains("invisible")) {
                console.log("open");
                idOpenBlock.classList.remove("invisible");
            } else {
                console.log("close");
                idOpenBlock.classList.add("invisible");
            }
        });

        // Закрытие при клике вне меню
        document.addEventListener("click", (e) => {
            if (
                !idOpenBlock.classList.contains("invisible") &&
                !idOpenBlock.contains(e.target) &&
                !element.contains(e.target)
            ) {
                idOpenBlock.classList.add("invisible");
            }
        });

        element.dataset.menu = "true";
    }
}

export default Tools;
