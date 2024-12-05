/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
   const toggle = document.getElementById(toggleId),
         nav = document.getElementById(navId)

   toggle.addEventListener('click', () =>{
       // Add show-menu class to nav menu
       nav.classList.toggle('show-menu')

       // Add show-icon to show and hide the menu icon
       toggle.classList.toggle('show-icon')
   })
}

showMenu('nav-toggle','nav-menu')




let nextButton = document.querySelector('.carousel-next');
let prevButton = document.querySelector('.carousel-prev');

nextButton.addEventListener('click', function() {
    let items = document.querySelectorAll('.carousel-item');
    document.querySelector('.carousel-slides').appendChild(items[0]);
});

prevButton.addEventListener('click', function() {
    let items = document.querySelectorAll('.carousel-item');
    document.querySelector('.carousel-slides').prepend(items[items.length - 1]); // here the length of items = 6
});










