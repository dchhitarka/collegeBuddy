window.addEventListener('resize', ()=>{
    if (window.innerWidth >= 768){
        let sideBar = document.querySelector('.sidebar');
        if(sideBar.style.left == "-500px")
            sideBar.style.left = "0";
    }
})
// Show SideBar
const showSide = () => {
    let sideBar = document.querySelector('.sidebar');
    sideBar.style.left = "0";
    document.querySelector('.main').style.opacity = "0.3";
    document.querySelector('.topbar').style.opacity = "0.3";
}
// Hide SideBar
const hideSide = () => {
    let sideBar = document.querySelector('.sidebar');
    sideBar.style.transition = "0.5s";
    sideBar.style.left = "-500px";
    document.querySelector('main').style.opacity = "1";
    document.querySelector('.topbar').style.opacity = "1";
}
