#!/usr/bin/node
/* This script create an function that converts a number
from base 10 to another base passed as argument */
exports.converter = function (base) {
  return function myConverter (a) {
    return a.toString(base);
  };
};
