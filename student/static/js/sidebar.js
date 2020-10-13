// Sidebar Functions
window.addEventListener('resize', ()=>{
    let sideBar = document.querySelector('.sidebar');
    if (window.innerWidth >= 768){
        hideSide()
    }else{
        sideBar.style.left = "-500px";
    }
})

window.addEventListener('touchend', () => {
    console.log("Touched");
    
    if (window.innerWidth < 768){
        let sideBar = document.querySelector('.sidebar');
        if (sideBar.style.left == "0"){
            hideSide()
        }
    }
})
// Show SideBar
const showSide = () => {
    hideComponents()
}
// Hide SideBar
const hideSide = () => {
    showComponents()
}

let currentScroll;
// Show allcomponents except sidebar
const showComponents = () => {
    let sideBar = document.querySelector('.sidebar');
    sideBar.style.transition = "0.5s";
    sideBar.style.left = "-500px";
    document.querySelector('main').style.opacity = "1";
    document.querySelector('.topbar').style.opacity = "1";
    document.querySelector('footer').style.opacity = "1";
    const body = document.body;
    body.style.position = '';
    // window.scrollTo(0, currentScroll);
    window.scrollTo({
        top: currentScroll,
        left: 0,
        behavior: 'auto'
    })
}

// Hode allcomponents except sidebar
const hideComponents = () => {
    let sideBar = document.querySelector('.sidebar');
    sideBar.style.transition = "0.5s";
    sideBar.style.left = "0";
    document.querySelector(".main").style.opacity = "0.2";
    document.querySelector('.topbar').style.opacity = "0.2";
    document.querySelector('footer').style.opacity = "0.2";
    const scrollY = document.documentElement.style.getPropertyValue('--scroll-y');
    currentScroll = document.documentElement.scrollTop || document.body.scrollTopscrollY
    const body = document.body;
    body.style.position = 'fixed';
}

// Load Data from database
