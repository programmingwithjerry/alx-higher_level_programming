$(document).ready(function () {
    // Store the API URL in a variable
    var apiUrl = "https://fourtonfish.com/hellosalut/?lang=fr";
    
    // Fetch data from the API
    $.getJSON(apiUrl, function (data) {
        // Update the content of the <div> with ID 'hello'
        $("div#hello").text(data.hello);
    });
});
