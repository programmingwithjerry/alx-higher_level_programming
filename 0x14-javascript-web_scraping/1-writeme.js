#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the file path and the string to write from the command-line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Check if both arguments are provided
if (!filePath || !contentToWrite) {
  console.error('Usage: node script.js <filePath> <content>');
  process.exit(1);
}

// Write the content to the file using 'utf8' encoding
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  // If an error occurred during the write operation, print the error object
  if (err) {
    console.error('An error occurred:', err);
  } else {
    console.log('File written successfully');
  }
});
