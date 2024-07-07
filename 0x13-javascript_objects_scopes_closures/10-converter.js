#!/usr/bin/node
exports.converter = function(base) {
  // Define a recursive function to convert a number to the specified base
  function convertToBase(num) {
    if (num >= base) {
      convertToBase(Math.floor(num / base)); // Recursive call with the quotient
    }
    console.log(num % base); // Print the remainder (digit in new base)
  }

  return convertToBase;
};
