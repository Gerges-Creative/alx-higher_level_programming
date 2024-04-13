#!/usr/bin/node

exports.esrever = function (list) {
  const arrLength = list.length - 1;

  for (let i = 0; i < arrLength; i++) {
    const temp = list[0];
    list[0] = list[arrLength];
    list[arrLength] = temp;
  }
};
