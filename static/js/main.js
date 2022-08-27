function scrollUp() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function scrollDown() {
    const scrollDiv = document.getElementById("about").offsetTop;
    window.scrollTo({ top: scrollDiv, behavior: 'smooth'});
}

function ReLoadImages() {
    const images = document.getElementsByClassName("gallery-image");
    for (let i = 0; i < images.length; i++) {
        images[i].src =
            document.getElementsByTagName("img")[i].getAttribute("data-lazysrc");
    }
}

function loaded() {
    darkerActive = true;
    document.getElementById("darker").style.animation = "darkerAnim 4s";
    document.getElementById("darker").style.backgroundColor = "transparent";
}

function httpGet(theUrl) {
    let xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("GET", theUrl, false);
    xmlHttpReq.send(null);
    return xmlHttpReq.responseText;
}

function socialClick(site) {
    httpGet("https://nawinds.top/api/v1/stats/social-click/" + site);
}

// EVENT LISTENERS

let darkerActive = false;

document.getElementsByClassName("last-gallery-image")[0].addEventListener('load', loaded);

document.addEventListener('animationend', (event) => {
    if (event.animationName === "collapseAnim") {
        ReLoadImages();
    }
});

window.addEventListener("scroll", (event) => {
    let scrollY = this.scrollY;
    let vh = window.innerHeight;
    if (scrollY > vh / 4) {
        document.getElementById("scroll-up").style.opacity = 1;
    }

    if (scrollY < vh / 4) {
        document.getElementById("scroll-up").style.opacity = 0;
    }

    if (darkerActive) {
        document.getElementById("darker").style.backgroundColor = "rgba(0, 0, 0, " + scrollY / vh + ")";
    }
});