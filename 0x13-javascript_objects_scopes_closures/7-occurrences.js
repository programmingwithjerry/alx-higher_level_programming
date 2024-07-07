#!/usr/bin/node
exports.nbOccurences = function(list, searchElement) {
  // Initialize a counter to store the number of occurrences
  let count = 0;

  // Iterate through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the searchElement
    if (list[i] === searchElement) {
      // Increment the counter if they match
      count++;
    }
  }

  // Return the total count of occurrences
  return count;
};
