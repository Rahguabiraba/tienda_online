window.onload = function () {
  let imagenes = document.querySelectorAll(".graficos");

  //Para cada imagen, añadimos el listener
  for (let i = 0; i < imagenes.length; i++) {
    imagenes[i].addEventListener("click", getSrc);
  }
};

function getSrc(e) {
    let imagen = e.target.src
    let input = e.target.previousElementSibling;
    let form = e.target.parentNode;
    //Podemos el valor dentro del input
    input.value = imagen;
    //Realizamos el submit
    form.submit();
}
