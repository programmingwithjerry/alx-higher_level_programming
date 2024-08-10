$(document).ready(function () {
    // Store the API URL in a variable
    var apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";
    
    // Fetch data from the API
    $.getJSON(apiUrl, function (data) {
        // Iterate over each film and create a list item for each title
        data.results.forEach(function (film) {
            $("<li>").text(film.title).appendTo("ul#list_movies");
        });
    });
});
