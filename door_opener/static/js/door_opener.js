/*
    Connor DeJohn
    Description: This Javascript file powers the normal html page that the user will see.
    Mainly, this file will work the button, update the current status, and run the python 
    toggle script.
*/

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


docReady(function(){
    document.querySelector("#btn_toggleDoor").addEventListener("click", (e) => {
        /* When the toggleDoor button is clicked..... */ 
        // change the button color
        document.getElementById("btn_toggleDoor").style.color = 'red';
        // create POST for python

        // get local information
        let csrftoken = getCookie('csrftoken');
        fetch('http://127.0.0.1:8000/garagedoor/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({  "type":     "toggle",
                                "csrf":     csrftoken
                            })
        })
        .then((response) => {
            if (response.status == 200) {
                // if a good response came back
                document.getElementById("btn_toggleDoor").style.backgroundColor = 'green';
            } else {
                document.getElementById("btn_toggleDoor").style.backgroundColor = 'indigo';
            }});
   });
})




function docReady(fn) {
    // see if DOM is already available
    if (document.readyState === "complete" || document.readyState === "interactive") {
        // call on next available tick
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}    



