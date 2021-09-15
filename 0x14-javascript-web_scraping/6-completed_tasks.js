#!/usr/bin/node
/* This script computes the number of tasks completed by user id */
const request = require('request');
const dict = {};

request.get(process.argv[2], (error, process, body) => {
  if (error) {
    return console.error(error);
  }
  const listTask = JSON.parse(body);
  for (let i = 1; i < 11; i++) {
    let countComplete = 0;
    for (const task of listTask) {
      if (task.userId === i && task.completed === true) {
        countComplete += 1;
      }
    }
    dict[i] = countComplete;
  }
  console.log(dict);
});
