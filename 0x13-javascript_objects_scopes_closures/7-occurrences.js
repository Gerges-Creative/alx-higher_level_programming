#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let x of list) {
    if (x === searchElement) {
      count++;
    }
  }

  return count;
}
