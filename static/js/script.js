window.onload = function () {
  let buttons = document.querySelectorAll(".button-producto");

  //Para cada botón, añadimos el listener
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", bloquearButton);
  }
};
let listaInventarios = [];
let listaNombres = [];

function bloquearButton(e) {
  
  //Declaramos las variables que utilizaremos
  let button = e.target;
  let inputInventario = document.getElementById("numero_inventario");
  let inputNombres = document.getElementById("nombre_producto");
  let nombre = button.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.childNodes[0].textContent;

  //Guardamos los valores de los inputs dentro de una lista
  listaInventarios.push(button.value);
  listaNombres.push(nombre);
  //Desabilitamos el botón 
  button.classList.remove("button-producto");
  button.classList.add("button-disable");
  button.disabled = true;
  //Luego, añadimos la información a los inputs que están escondidos
  inputInventario.value = listaInventarios;
  inputNombres.value = listaNombres;

  if (listaNombres.length > 2){
    let button_analisis = document.getElementById("button-analisis");
    button_analisis.classList.remove("button-disable");
    button_analisis.classList.add("button-analisis");
    button_analisis.disabled = false;
  } else if(listaNombres.length == 2) {
    alert("Tienes que seleccionar más de 2 productos.");
  }
}
