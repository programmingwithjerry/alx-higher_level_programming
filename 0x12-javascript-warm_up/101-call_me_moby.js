#!/usr/bin/node
// Export the callMeMoby function as a module
exports.callMeMoby = function (x, theFunction) {
  // Loop x times
  while (x-- > 0) {
    // Call the provided function
    theFunction();
  }
};

