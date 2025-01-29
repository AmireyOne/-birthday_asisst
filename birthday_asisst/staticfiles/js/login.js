const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

$(".logins").click(function() {
    $("#formlog").attr("action", "ChekLogin");
});

$(".singups").click(function() {
    $("#formsin").attr("action", "Singup_User");
});
