import {login} from "../api.js"
import {loadPage} from "../router.js"


export function initLogin(){
    const email = document.getElementById("email")
    const password = document.getElementById("password")
    const submitLogin = document.getElementById("submit-login")
    const loginDiv = document.getElementById("loginDiv")

    submitLogin.addEventListener("click", async(e)=> {
        e.preventDefault()
        if(!loginDiv.checkValidity()){
            alert("Enter Credentials")
            return
        }
        try{
            const data = await login(email.value, password.value)
            localStorage.setItem("token",data.access_token)
            email.value = null
            password.value = null
            loadPage("app")
        }catch(error){
            if(error.status == 403){alert("Wrong Credentials")}
        }
    })
}