const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';


export async function login(email,password){
        const res = await fetch(`${API_URL}/login`,{
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

export async function register(email,password){
        const res = await fetch(`${API_URL}/register`,{
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                email : email,
                password : password
            })
        })
        const data = await res.json()
        return data
}


export async function convert(url,token){
    const res = await fetch(`${API_URL}/url/`,{
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
    const res = await fetch (`${API_URL}/url/user-links`,{
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
    const res = await fetch (`${API_URL}/url/${id}`,{
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
