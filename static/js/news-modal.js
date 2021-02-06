$(document).ready(() => {
  const displayModal = localStorage.getItem("modalNewsOpened") !== "true";

  if (displayModal) {
    $("#newsModal").modal("show");
    localStorage.setItem("modalNewsOpened", "true");
  }
});
