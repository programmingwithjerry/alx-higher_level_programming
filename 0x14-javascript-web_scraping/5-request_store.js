#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');
// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the URL and the file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make an HTTP GET request to the specified URL
request(url, (err, res, body) => {
  // If an error occurred during the request, print the error object
  if (err) {
    console.error('Error:', err);
    return;
  }
  
  // Write the response body to the file using 'utf8' encoding
  fs.writeFile(filePath, body, 'utf8', (writeErr) => {
    // If an error occurred during the file write, print the error object
    if (writeErr) {
      console.error('Write Error:', writeErr);
      return;
    }
    // Print a success message
    console.log('File saved successfully');
  });
});
