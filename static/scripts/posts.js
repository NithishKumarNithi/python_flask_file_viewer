/* 
    posts scripts for the application
*/

function getResources(url){
    var httpxhr = new XMLHttpRequest();
    httpxhr.onload = function(){
        if(httpxhr.status == 200){
            appendToBody(httpxhr.response);
            resourceFetch();
        }
        
    }
    httpxhr.open('GET',url,true);
    httpxhr.send();
}

/*
    appending response to the view
*/
function appendToBody(chunk){
    var wrapper = document.querySelector('.display-content-wrapper');
    wrapper.innerHTML = chunk;
}

/* 
    get the initial resource the browser start loading
*/
window.onload = function(){
    getResources('http://127.0.0.1:5000/home/lists');
}

/*
    get the selected name from event 
*/
function resourceFetch(){
    var file__folder_selection = document.querySelectorAll('.file__folder-list-left .file_folder-name'); // file folder selection in client

    /* looping file folder selection */
    file__folder_selection.forEach(function(ff){
        ff.addEventListener('click',function(e){
            e.preventDefault();
            getResources('http://127.0.0.1:5000/'+e.target.innerText);
        });
    });
}


