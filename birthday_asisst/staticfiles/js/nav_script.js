function toggleMenu() {
  const menu = document.getElementById('offcanvasMenu');
  menu.classList.toggle('show');
}

// بستن منو هنگام کلیک خارج از آن
document.addEventListener('click', function (event) {
  const menu = document.getElementById('offcanvasMenu');
  if (!menu.contains(event.target) && !event.target.closest('.navbar-toggler')) {
    menu.classList.remove('show');
  }
});
