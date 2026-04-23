import { getUrl, deleteUrl } from "../api.js"
import {logoutUser} from "../helper.js"
import { API_URL } from "../api.js"


export function initUser(){
    const loadBtn = document.getElementById("load-url")

    loadBtn.addEventListener("click", async()=>{
        const token = localStorage.getItem("token")
        try{
            const data = await getUrl(token)
            renderUrls(data)
        }catch(error){
            if(error.status == 401){
                alert("Session expired")
                logoutUser()
            }
        }
    })
}

function renderUrls(data) {
    const container = document.getElementById("urlList")
    container.innerHTML = ""

    if (!data.length) {
        container.textContent = "No URLs found."
        return
    }

    data.forEach((item) => {
        const card = document.createElement("div")
        card.className = "url-card"

        const shortLink = document.createElement("a")
        shortLink.href = item.formatted_short_url
        shortLink.textContent = item.short_URL
        shortLink.target = "_blank"

        const longUrl = document.createElement("p")
        longUrl.textContent = item.long_URL

        const date = document.createElement("small")
        date.textContent = new Date(item.created_at).toLocaleString()

        const copyBtn = document.createElement("button")
        copyBtn.textContent = "Copy"
        copyBtn.addEventListener("click", () => {
            navigator.clipboard.writeText(shortLink.href)
            alert("Copied!")
        })

        const deleteBtn = document.createElement("button")
        deleteBtn.textContent = "Delete"
        deleteBtn.addEventListener("click", async()=>{
            const token = localStorage.getItem("token")
            try{
            const data = await deleteUrl(item.id,token)
            }catch(error){
                alert(error.message)
            }
            container.removeChild(card)
        })

        card.appendChild(shortLink)
        card.appendChild(longUrl)
        card.appendChild(date)
        card.appendChild(copyBtn)
        card.appendChild(deleteBtn)

        container.appendChild(card)
    })
}