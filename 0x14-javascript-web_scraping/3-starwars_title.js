#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Construct the URL using the base URL and the film ID from the command-line arguments
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

// Make an HTTP GET request to the specified URL
request(apiUrl, function (err, res, body) {
  // If an error occurred during the request, print the error object
  // Otherwise, parse the response body and print the title of the film
  console.log(err || JSON.parse(body).title);
});
