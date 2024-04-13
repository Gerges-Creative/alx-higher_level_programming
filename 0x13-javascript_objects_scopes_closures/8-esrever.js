#!/usr/bin/node

exports.esrever = function (list) {
  let arrLength = list.length - 1;

  for (let i = 0; i <= arrLength; i++) {
    const temp = list[i];
    list[i] = list[arrLength];
    list[arrLength] = temp;
    arrLength--;
  }

  return list;
};
