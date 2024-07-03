#!/usr/bin/node
// This line indicates that the script should be run using the Node.js interpreter

// Export the callMeMoby function as a module
exports.callMeMoby = function (x, theFunction) {
  // Loop x times
  while (x-- > 0) {
    // Call the provided function
    theFunction();
  }
};

