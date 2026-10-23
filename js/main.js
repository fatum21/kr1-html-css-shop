/* =====================================================================
   Lumen — каталог настольных ламп
   Файл: js/main.js
   Назначение: минимальная логика модального окна и форм.
   ===================================================================== */
document.querySelectorAll("[data-open-order]").forEach((button) => {
  button.addEventListener("click", () => {
    const dialog = document.getElementById(button.dataset.openOrder);

    if (!dialog) {
      return;
    }

    const message = dialog.querySelector(".form-message");
    if (message) {
      message.hidden = true;
    }

    if (typeof dialog.showModal === "function") {
      dialog.showModal();
    } else {
      dialog.setAttribute("open", "");
    }
  });
});

document.querySelectorAll("[data-close-order]").forEach((button) => {
  button.addEventListener("click", () => {
    const dialog = button.closest("dialog");
    if (dialog) {
      dialog.close();
    }
  });
});

document.querySelectorAll(".order-dialog").forEach((dialog) => {
  dialog.addEventListener("click", (event) => {
    if (event.target !== dialog) {
      return;
    }

    const rect = dialog.getBoundingClientRect();
    const isInside =
      event.clientX >= rect.left &&
      event.clientX <= rect.right &&
      event.clientY >= rect.top &&
      event.clientY <= rect.bottom;

    if (!isInside) {
      dialog.close();
    }
  });
});

document.querySelectorAll(".order-form").forEach((form) => {
  const message = form.querySelector(".form-message");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    form.reset();

    if (message) {
      message.hidden = false;
      message.scrollIntoView({ block: "nearest" });
    }
  });

  form.addEventListener("input", () => {
    if (message) {
      message.hidden = true;
    }
  });

  form.addEventListener("reset", () => {
    if (message) {
      message.hidden = true;
    }
  });
});
