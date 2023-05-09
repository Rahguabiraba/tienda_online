window.onload = function () {
  let buttons = document.querySelectorAll(".button-producto");

  //Para cada botón, añadimos el listener
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", bloquearButton);
  }
};
let listaInventarios = [];

function bloquearButton(e) {
  let button = e.target;
  listaInventarios.push(button.value);
  button.classList.remove("button-producto");
  button.classList.add("button-disable");
  button.disabled = true;
}
