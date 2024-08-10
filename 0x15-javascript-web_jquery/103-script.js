$(document).ready(function () {
    // Store the base URL in a variable
    const apiUrl = 'https://fourtonfish.com/hellosalut/hello/?lang=';

    // Bind click event to the button
    $("input#btn_translate").click(function () {
        // Get the value of the language code from the input
        const language_code = $("input#language_code").val();

        // Fetch data from the API
        $.getJSON(apiUrl + language_code, function (data) {
            // Update the content of the <div> with ID 'hello'
            $("#hello").text(data.hello);
        });
    });
});
