#!/usr/bin/node
// Define a class Rectangle
module.exports = class Rectangle {
  // Constructor that takes two arguments: w (width) and h (height)
  constructor(w, h) {
    // Check if both w and h are greater than 0
    if (w > 0 && h > 0) {
      // Initialize instance attributes width and height
      [this.width, this.height] = [w, h];
    }
    // If w or h is not greater than 0, the constructor does nothing
  }
};

