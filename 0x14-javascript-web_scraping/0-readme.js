#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (error, data) => {
  if (data === undefined) {
    console.error(error);
  } else {
    console.log(data);
  }
});
