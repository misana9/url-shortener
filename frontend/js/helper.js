import {loadPage} from "./router.js"

export function logoutUser(){
    localStorage.removeItem("token")
    loadPage("login")
}

export function isLoggedIn(){
    return !!localStorage.getItem("token")
}