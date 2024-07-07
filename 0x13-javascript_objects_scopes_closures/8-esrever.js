#!/usr/bin/node
exports.esrever = function (list) {
  // Check if list is valid and is an array
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array');
  }
  // Initialize variables for reversing the list
  let start = 0;
  let end = list.length - 1;

  // Swap elements from start to end
  while (start < end) {
    // Swap elements at start and end indices
    let temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    // Move start and end indices towards each other
    start++;
    end--;
  }

  // Return the reversed list
  return list;
};
