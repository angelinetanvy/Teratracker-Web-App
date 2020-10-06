document.getElementById('closeTask').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "flex";
});

document.getElementById('deleteTask').addEventListener("click", function() {
	document.querySelector('.bg-modalz').style.display = "flex";
});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});

document.querySelector('.closez').addEventListener("click", function() {
	document.querySelector('.bg-modalz').style.display = "none";
});