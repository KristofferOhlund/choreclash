document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("reward-modal");

  if (!modal) return;

  const closeButton = modal.querySelector(".modal-close");

  modal.showModal();

  closeButton.addEventListener("click", () => {
    modal.close();
  });
});
