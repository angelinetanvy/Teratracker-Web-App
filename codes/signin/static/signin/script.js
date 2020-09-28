const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
let buttonName = document.getElementById('button-name');
let signupFail = document.getElementById('signupFail')


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

if(signupFail.value === "true"){
	container.classList.add("right-panel-active");
}