#!/usr/bin/node

let count = 0;

exports.logMe = function logMe (item) {
  console.log(`${count}: ${item}`);
  count++;
};
