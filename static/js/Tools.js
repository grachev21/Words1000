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
  ajaxGet(url, targetSelector) {
    fetch(url)
      .then((response) => {
        if (!response.ok) throw new Error("Ошибка сети");
        return response.text(); // Получаем HTML как текст
      })
      .then((html) => {
        // Вставляем ответ в контейнер
        const target = document.querySelector(targetSelector);
        if (target) {
          target.innerHTML = html;
        } else {
          console.error("Целевой элемент не найден:", targetSelector);
        }
      })
      .catch((err) => {
        console.error("Ошибка при запросе:", err);
      });
  }
}

export default Tools;
