$(document).ready(() => {
  $(".subscribe-input").on("keydown", () => {
    $(".validation-message").hide();
  });

  $(".validation-message").on("click", () => {
    $(".validation-message").hide();
  });
});
