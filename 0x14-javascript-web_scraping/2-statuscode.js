#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL from the command-line arguments
const targetUrl = process.argv[2];

// Make an HTTP GET request to the specified URL
request(targetUrl, (err, res) => {
  // If an error occurred during the request, print the error object
  if (err) {
    console.error(err);
    return;
  }
  // Print the HTTP status code of the response
  console.log(`code: ${res.statusCode}`);
});
