document.getElementById('closeTask').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "flex";
});

document.getElementById('deleteTask').addEventListener("click", function() {
	document.querySelector('.delete-bg-modal').style.display = "flex";
});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});

document.querySelector('.delete-close').addEventListener("click", function() {
	document.querySelector('.delete-bg-modal').style.display = "none";
});