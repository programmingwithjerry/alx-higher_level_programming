#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make an HTTP GET request to the specified API URL
request(apiUrl, (err, res, body) => {
  // If an error occurred during the request, print the error object
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse the response body from JSON format
  const todos = JSON.parse(body);

  // Initialize an object to keep track of completed tasks by user ID
  const completedTasks = {};

  // Iterate through each task in the list of todos
  todos.forEach(todo => {
    // Check if the task is completed
    if (todo.completed) {
      // If the user ID is not yet in the completedTasks object,
      // initialize it to 0
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      // Increment the count of completed tasks for the user ID
      completedTasks[todo.userId]++;
    }
  });

  // Iterate through the completedTasks object and print the user
  // IDs and their completed task counts
  for (const userId in completedTasks) {
    console.log(`User ${userId}: ${completedTasks[userId]} completed tasks`);
  }
});
