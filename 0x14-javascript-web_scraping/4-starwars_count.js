#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make an HTTP GET request to the specified API URL
request(apiUrl, (err, res, body) => {
  // If an error occurred during the request, print the error object
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body from JSON format
  const films = JSON.parse(body).results;
  let count = 0;

  // Iterate through each film
  films.forEach(film => {
    // Check if the character "Wedge Antilles" (character ID 18) is in the film's characters list
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });

  // Print the number of films where "Wedge Antilles" is present
  console.log(count);
});
