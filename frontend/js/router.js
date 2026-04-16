import { initLogin } from "./views/login.js"
import { initApp } from "./views/app.js"
import { initUser } from "./views/user.js"
import { isLoggedIn } from "./helper.js"
import { logoutUser } from "./helper.js"

const userBtn = document.getElementById("userBtn")
const convertBtn = document.getElementById("convertBtn")
const logoutBtn = document.getElementById("logoutBtn")

// localStorage.removeItem("token")
export async function loadPage(page) {
    const res = await fetch(`/pages/${page}.html`)
    const html = await res.text()

    document.getElementById("app").innerHTML = html
    const initMap = {
        login : initLogin,
        app : initApp,
        user : initUser
    }
    initMap[page]?.()
    updateHeader()
}

export function updateHeader() {

    if (isLoggedIn()) {
        userBtn.style.display = "inline-block"
        convertBtn.style.display = "inline-block"
        logoutBtn.style.display = "inline-block"
    } else {
        userBtn.style.display = "none"
        convertBtn.style.display = "none"
        logoutBtn.style.display = "none"
    }
}


userBtn.addEventListener("click", () => {
    history.hash = "#/user"
    loadPage("user")
})

convertBtn.addEventListener("click", () => {
    history.hash = "#/app"
    loadPage("app")
})

logoutBtn.addEventListener("click", () => {
    logoutUser()
    updateHeader()
    history.hash = "#/frontend"
    loadPage("login")
})

const token = localStorage.getItem("token")

if (token){
    loadPage("app")
}else{
    loadPage("login")
}