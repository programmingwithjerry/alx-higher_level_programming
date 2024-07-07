#!/usr/bin/node
exports.logMe = function (item) {
  // Initialize a static variable to keep track of the number of arguments printed
  if (!exports.logMe.counter) {
    exports.logMe.counter = 0;
  }
  // Print the output in the specified format
  console.log(`${exports.logMe.counter}: ${item}`);
  // Increment the counter for the next call
  exports.logMe.counter++;
};
