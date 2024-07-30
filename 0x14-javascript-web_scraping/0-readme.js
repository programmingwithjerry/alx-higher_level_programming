#!/usr/bin/node

// Import the 'fs' module to handle file system operations
//const fs = require('fs');

// Read the content of the file specified by the first command-line argument using 'utf8' encoding
//fs.readFile(process.argv[2], 'utf8', function (err, contents) {
  // Check if 'contents' is undefined, indicating an error occurred during the file read
//  if (contents === undefined) {
    // Print the error object to the console
//    console.log(err);
//  } else {
    // Print the file content to the console
//    console.log(contents);
//  }
//});

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
