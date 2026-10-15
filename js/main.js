/* =====================================================================
   kr1-html-css-shop — ТехноМарт
   Файл: js/main.js
   Назначение: минимальная JavaScript-логика (по методическим указаниям
   JS допускается только для открытия/закрытия модального окна).
   Весь остальной функционал реализован средствами HTML и CSS.

   Модалка построена на нативном элементе <dialog>, поэтому:
   - Enter/Space на кнопке открывает окно;
   - Esc и клик по фону (::backdrop) закрывают окно;
   - фокус переносится внутрь окна автоматически.
   ===================================================================== */
(function () {
  "use strict";

  var modalSelector = "[data-modal-open]";
  var closeSelector = "[data-modal-close]";

  /* Открытие модального окна */
  function openModal(modal) {
    if (typeof modal.showModal === "function") {
      modal.showModal();
    } else {
      // Резервный вариант для очень старых браузеров без <dialog>
      modal.setAttribute("open", "");
    }
    modal.classList.add("modal--opened");
  }

  /* Закрытие модального окна */
  function closeModal(modal) {
    if (typeof modal.close === "function") {
      modal.close();
    } else {
      modal.removeAttribute("open");
    }
    modal.classList.remove("modal--opened");
  }

  /* Делегирование: клик по кнопке с data-modal-open="id-модалки" */
  document.addEventListener("click", function (event) {
    var opener = event.target.closest(modalSelector);
    if (opener) {
      event.preventDefault();
      var modal = document.getElementById(opener.getAttribute("data-modal-open"));
      if (modal) {
        openModal(modal);
      }
      return;
    }

    /* Клик по кнопке закрытия */
    var closer = event.target.closest(closeSelector);
    if (closer) {
      event.preventDefault();
      var dialog = closer.closest("dialog, .modal");
      if (dialog) {
        closeModal(dialog);
      }
    }
  });

  /* Закрытие по клику на подложку (сам элемент <dialog>) */
  document.querySelectorAll("dialog.modal").forEach(function (modal) {
    modal.addEventListener("click", function (event) {
      if (event.target === modal) {
        closeModal(modal);
      }
    });

    /* После успешной отправки формы заявки закрываем окно */
    var form = modal.querySelector("form");
    if (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        closeModal(modal);
        form.reset();
      });
    }
  });

  /* Текущий год в подвале */
  var yearNodes = document.querySelectorAll("[data-current-year]");
  yearNodes.forEach(function (node) {
    node.textContent = new Date().getFullYear();
  });
})();
