import { initLogin } from "./views/login.js"
import { initApp } from "./views/app.js"
import { initUser } from "./views/user.js"
import { isLoggedIn } from "./helper.js"
import { logoutUser } from "./helper.js"
import { API_URL } from "./api.js"
import { initRegister } from "./views/register.js"


const userBtn = document.getElementById("userBtn")
const convertBtn = document.getElementById("convertBtn")
const logoutBtn = document.getElementById("logoutBtn")
const registerBtn = document.getElementById("registerBtn")
const loginBtn = document.getElementById("loginBtn")



// localStorage.removeItem("token")
export async function loadPage(page) {
    const res = await fetch(`/frontend/pages/${page}.html`)
    const html = await res.text()

    document.getElementById("app").innerHTML = html
    const initMap = {
        login : initLogin,
        app : initApp,
        user : initUser,
        register : initRegister
    }
    initMap[page]?.()
    updateHeader()
}

export function updateHeader() {

    if (isLoggedIn()) {
        userBtn.style.display = "inline-block"
        convertBtn.style.display = "inline-block"
        logoutBtn.style.display = "inline-block"
        registerBtn.style.display = "none"
        loginBtn.style.display = "none"

    } else {
        registerBtn.style.display = "inline-block"
        loginBtn.style.display = "inline-block"
        userBtn.style.display = "none"
        convertBtn.style.display = "none"
        logoutBtn.style.display = "none"
    }
}

loginBtn.addEventListener("click", () => {
    history.hash = "#/user"
    loadPage("login")
})

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
})

registerBtn.addEventListener("click", () => {
    history.hash = "#/register"
    loadPage("register")
})

const token = localStorage.getItem("token")

if (token){
    loadPage("app")
}else{
    loadPage("login")
}