const BASE_URL = window.location.origin;

export async function root() {
    try{
        const res = await fetch(`${BASE_URL}/`,{
            method : "GET",
        })
        const data = await res.json()
        console.log(data)
    }catch(error){
        console.log(error)
    }
}

export async function login(email,password){
        const res = await fetch(`${BASE_URL}/login`,{
            method : "POST",
            headers : {
                "Content-Type" : "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                username : email,
                password : password
            })
        })
        if(!res.ok){
            throw{
                status : res.status,
                message : "request failed"
            }
        }else{
           return (await res.json())
        }
}


export async function convert(url,token){
    const res = await fetch(`${BASE_URL}/url`,{
        method: "POST",
        headers: {
            "Content-Type" : "application/json",
            Authorization : `Bearer ${token}`
        },
        body: JSON.stringify({
            long_URL : url
        })
    })
    if (res.status === 401) {
        throw{
            status : res.status,
            message : "Must be a valid link"
        }
    }
    if(!res.ok){
        throw{
            status : res.status,
            message : "Must be a valid link"
        }
    }
    return await res.json()
}

export async function getUrl(token){
    const res = await fetch (`${BASE_URL}/url/user-links`,{
        method: "GET",
        headers:{
            Authorization: `Bearer ${token}`
        }
    })
    if(!res.ok){
        throw{
            status : res.status,
            message : "Error fetching URLs"
        }
    }
    return await res.json()
}

export async function deleteUrl(id,token){
    const res = await fetch (`${BASE_URL}/url/${id}`,{
        method : "DELETE",
        headers :{
            Authorization : `Bearer ${token}`
        }
    })
    if(!res.ok){
        throw{
            status: res.status,
            message : res.statusText
        }
    }
    return res.status
}
