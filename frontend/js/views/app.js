import {convert} from "../api.js"
import {logoutUser} from "../helper.js"


export function initApp(){
    const url = document.getElementById("url")
    const submitUrl = document.getElementById("submit-url")
    const linkGenerated = document.getElementById("link-generated")

    submitUrl.addEventListener("click", async()=>{
        try{
        const token = localStorage.getItem("token")
        const data = await convert(url.value,token)
            let p = document.getElementById("result") || document.createElement("p")
            p.id = "result"
            p.textContent = data
        if (!document.getElementById("result")) {
            linkGenerated.appendChild(p)
            }
        }catch(error){
            if(error.status == 422){
                alert("Enter a valid link")
            }else if(error.status == 401){
                alert("Session expired")
                logoutUser()
            }
        }
    })
}