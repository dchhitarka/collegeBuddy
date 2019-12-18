window.addEventListener('resize', ()=>{
    if (window.innerWidth >= 768){
        let afterTopbar = document.querySelector('.hot-corner');
        afterTopbar.style.marginTop = `${topbar.offsetHeight - 5}px`;
    }
    else{
        document.querySelector('.hot-corner').style.marginTop = '2px';
        let afterTopbar = document.querySelector('.mobile-search');
        afterTopbar.style.marginTop = `${topbar.offsetHeight - 7}px`;
    }
})
// Dynamically add margin-top to hot-corner based on topbar's height;
let topbar = document.querySelector('.topbar');
if(window.innerWidth >= 768){
    let afterTopbar = document.querySelector('.hot-corner');
    afterTopbar.style.marginTop = `${topbar.offsetHeight - 5}px`;    
}else{
    let afterTopbar = document.querySelector('.mobile-search'); 
    afterTopbar.style.marginTop = `${topbar.offsetHeight - 7}px`;
}

// Hot Corner Slide Show
var slideIndex = 1;
showSlides(slideIndex); //Manual SlideShow
slideShow(); //Automatic SlideShow
function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("trending-item");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active-dot", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active-dot";
}

function slideShow(){
    var i;
    var slides = document.getElementsByClassName("trending-item");
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    for(i = 0; i < dots.length; i++){
        dots[i].classList.remove('active-dot');
    } 
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block"; 
    dots[slideIndex-1].className += " active-dot";    
    setTimeout(slideShow, 2000);
}

let cart = document.querySelector('.cart-no');
if (cart.innerHTML == 0) cart.style.display = 'none';