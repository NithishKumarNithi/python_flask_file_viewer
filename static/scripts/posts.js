/* host name */
var host_url = window.location.origin;

/* 
    get the initial resource the browser start loading
*/
window.onload = function(){
    getResources(host_url+'/home/lists');
}

/* 
    posts scripts for the application
*/
function getResources(url){
    var httpxhr = new XMLHttpRequest();
    httpxhr.onload = function(){
        if(httpxhr.status == 200){
            appendToBody(httpxhr.response);
            initiateResourceFunctions();
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
    get the selected name from event 
*/
function resourceFetch(){

    /* 
        returns resources object from the client
    */
    return resourceObj = {
        'file__folder_selection' : document.querySelectorAll('.file__folder-list-left .file_folder-name'),
        'path_hierachy_selection': document.querySelectorAll('.file__folder-path-name-text'),
    }
    
}

/*
    initializes resources object
*/

function initiateResourceFunctions(){
    var resourcesele = resourceFetch();
    loopResourcesEleDom(resourcesele['file__folder_selection']);
    loopResourcesEleDom(resourcesele['path_hierachy_selection']);
}

/*
    looping through resources DOM
*/
function loopResourcesEleDom(resourceobj){
    resourceobj.forEach(function(ff){
        ff.addEventListener('click',function(e){
            e.preventDefault();
            getResources(host_url+'/'+e.target.innerText);
        });
    });
}