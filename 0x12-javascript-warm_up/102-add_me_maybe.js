#!/usr/bin/node
// This line indicates that the script should be run using the Node.js interpreter

// Export the addMeMaybe function as a module
exports.addMeMaybe = function (number, theFunction) {
  // Call the provided function with the number incremented by 1
  theFunction(number + 1);
};

