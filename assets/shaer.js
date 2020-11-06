var button = document.querySelector('.button-backdrup');
var social = document.querySelector('.social-link');

button.addEventListener("click", function(e) {
    e.preventDefault();
    button.classList.add('show');
    setTimeout(function() {
        button.classList.remove("show");
    }, 7000)
});

social.addEventListener("click", function(e) {
    e.preventDefault();
    social.classList.toggle('hidden');
});