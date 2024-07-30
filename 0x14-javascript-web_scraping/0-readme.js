#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Read the content of the file specified by the first command-line argument using 'utf8' encoding
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Print the error object if an error occurred, otherwise print the file content
  console.log(error || content);
});
