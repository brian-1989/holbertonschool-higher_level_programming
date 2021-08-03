#!/usr/bin/node
/* This script create an function that returns the reversed version of a list */
exports.esrever = function (list) {
  const myList = [];
  const lengthMyList = list.length - 1;
  for (let i = lengthMyList; i >= 0; i--) {
    myList.push(list[i]);
  }
  return myList;
};
