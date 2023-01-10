// Firing The Event 
// URL Align

// let countryName = search.value;
let finalUrl = `https://newsapi.org/v2/top-headlines?country=us&apiKey=c1c6b2768bce47959b6a33cf57d850fb`;
// console.log(finalUrl);

// Initializing API

let request = new XMLHttpRequest();
request.open("GET", finalUrl);
request.send();


// Getting Data 

request.addEventListener("load", function () {
    //  console.log(this.responseText);
    let data = JSON.parse(this.responseText);
    // let data = this.data;
    console.log(data)


});