import {register} from "../api.js"
import {loadPage} from "../router.js"


export function initRegister(){
    const emailReg = document.getElementById("emailReg")
    const passwordReg = document.getElementById("passwordReg")
    const passwordConfirm = document.getElementById("passwordConfirm")
    const submitRegister = document.getElementById("submit-register")
    const registerDiv = document.getElementById("registerDiv")

    submitRegister.addEventListener("click", async(e)=> {
        e.preventDefault()
        if(!registerDiv.checkValidity()){
            alert("Error")
            return
        }
        if(passwordConfirm.value != passwordReg.value){
            alert("Password mismatch")
            return
        }
        try{
            const data = await register(emailReg.value, passwordReg.value)
            if(data == null){
                loadPage("login")
            }
            alert(data.detail)
        }
        catch(error){
            return error
        }
    })
}