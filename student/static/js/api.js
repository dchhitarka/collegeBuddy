const BASE_URL = "http://localhost:8000/"
const headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-CSRFToken": csrftoken,
}

const saveTimetableApi = async (timetable) => {
    try{
        let res = await fetch(`${BASE_URL}timetable/save`, 
                                {
                                    body: JSON.stringify(timetable),
                                    headers: headers,
                                    method:"POST"
                                } 
                            )
        let data = await res.json()
        console.log(data)
    }
    catch (error){
        console.log(error.message)
    }    
}