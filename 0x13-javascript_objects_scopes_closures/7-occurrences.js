#!/usr/bin/node
/* This script create an function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  const lengthMyList = list.length;
  let count = 0;
  for (let i = 0; i < lengthMyList; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return count;
};
