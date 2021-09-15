#!/usr/bin/node
/* This script computes the number of tasks completed by user id */
const request = require('request');

request(process.argv[2], (error, process, body) => {
  if (error) {
    return console.error(error);
  }
  const listTask = JSON.parse(body);
  const dict = {};
  for (let i = 1; i < 11; i++) {
    let countComplete = 0;
    for (const task of listTask) {
      if (task.userId === i && task.completed === true) {
        countComplete += 1;
      }
    }
    if (countComplete !== 0){
      dict[i] = countComplete;
    }
  }
  console.log(dict);
});
