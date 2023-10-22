// JavaScript para mostrar y ocultar la ventana emergente
const popup = document.getElementById("popup");
const closePopupButton = document.getElementById("closePopup");

function showPopup() {
  popup.classList.add("show");
}

function hidePopup() {
  popup.classList.remove("show");
}

closePopupButton.addEventListener("click", hidePopup);
