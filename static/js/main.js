const ENGLISH = document.getElementsByTagNameNS("http://www.w3.org/1999/xhtml",
    "html")[0].getAttribute("lang") === "en";

if (location.hash === '#force_lang') {
    document.cookie = "lang=" + (ENGLISH ? "en" : "ru") + ";path=/";
    window.location.href = window.location.href.split("#")[0];
}

function dismissLanguageSwitchPopup() {
    document.getElementById("language-switch-popup").classList.toggle("hidden-popup");
    document.cookie = "lang=" + (ENGLISH ? "en" : "ru") + ";path=/";
}

function scrollUp() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function scrollDown() {
    const scrollDiv = document.getElementById("about").offsetTop;
    window.scrollTo({top: scrollDiv, behavior: 'smooth'});
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
    httpGet("https://nawinds.dev/api/v1/stats/social-click/" + site);
}

function projectLink(thisElem, projectName, linkNumber) {
    let linkName;
    switch (linkNumber) {
        case 0:
            linkName = "на сайт";
            break;
        case 1:
            linkName = "на исходный код";
            break;
        default:
            linkName = linkNumber;
    }
    socialClick("проект " + projectName +
        " (ссылка " + linkName + ")");
}

function showAllProjects() {
    document.getElementById("show-more-projects-btn-text").innerText = (ENGLISH ? "Hide" : "Свернуть");
    document.getElementById("show-more-projects-btn").onclick = hideProjects;
    document.getElementsByClassName("show-more-projects-btn-img")[0].style.transform = "none";
    document.getElementsByClassName("show-more-projects-btn-img")[1].style.transform = "none";
    const hiddenProjects = document.getElementsByClassName("hidden-project");
    for (let i = 0; i < hiddenProjects.length; i++) {
        hiddenProjects[i].style.display = "";
    }
}

function hideProjects() {
    document.getElementById("show-more-projects-btn-text").innerText = (ENGLISH ? "All projects" : "Все проекты");
    document.getElementById("show-more-projects-btn").onclick = showAllProjects;
    document.getElementsByClassName("show-more-projects-btn-img")[0].style.transform = "rotate(180deg)";
    document.getElementsByClassName("show-more-projects-btn-img")[1].style.transform = "rotate(180deg)";
    const hiddenProjects = document.getElementsByClassName("hidden-project");
    for (let i = 0; i < hiddenProjects.length; i++) {
        hiddenProjects[i].style.display = "none";
    }
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

console.log("%cHey there!",
    "color: white; font-style: bold; background-color: black; font-size: 30px;");
console.log("%cYou're lucky to find a surprise from me!",
    "color: black; font-style: bold; background-color: white; font-size: 20px;");
console.log("%cGo to https://nawinds.dev/lucky and enjoy it!",
    "color: black; font-style: bold; background-color: yellow; font-size: 20px;");

window.onload = function () {
    let version_hashtags = document.getElementsByClassName("version-hashtag");
    Array.prototype.forEach.call(version_hashtags, function (el) {
        const ghRepo = el.innerText;

        let xmlHttpReq = new XMLHttpRequest();
        xmlHttpReq.open("GET", "/api/v1/projects/get_version?github_repo=" + ghRepo, false);
        xmlHttpReq.send(null);
        if (xmlHttpReq.status === 200) {
            el.innerText = xmlHttpReq.responseText;
            el.style = "";
        }
    });
}

// NEW DOMAIN

function hideNewDomain() {
    const background = document.getElementById("new-domain-background");
    const banner = document.getElementById("new-domain");
    background.style.display = "none";
    banner.style.display = "none";

    const url = window.location.href;
    const urlObj = new URL(url);
    urlObj.search = '';
    const result = urlObj.toString();
    history.pushState({}, null, result);
}