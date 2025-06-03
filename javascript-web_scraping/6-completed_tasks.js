#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasks[userId] = (completedTasks[userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  } catch (err) {
    console.error(err);
  }
});
