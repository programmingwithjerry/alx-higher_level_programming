#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL using the base URL and the movie ID from
// the command-line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make an HTTP GET request to the specified URL
request(apiUrl, (err, res, body) => {
  // If an error occurred during the request, print the error object
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse the response body from JSON format
  const film = JSON.parse(body);

  // Get the list of character URLs
  const characters = film.characters;

  // Iterate through each character URL and make a request
  // to get character details
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      // If an error occurred during the request, print the error object
      if (err) {
        console.error('Error:', err);
        return;
      }

      // Parse the response body from JSON format
      const character = JSON.parse(body);

      // Print the name of the character
      console.log(character.name);
    });
  });
});
