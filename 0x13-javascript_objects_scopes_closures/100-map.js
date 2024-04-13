#!/usr/bin/node

const factList = require('./100-data').list;
const factArr = factList.map(factFunc);

function factFunc (currentValue, index) {
  return currentValue * index;
}
const o = JSON.stringify(factList, null, 1);
console.log(o);

console.log(JSON.stringify(factArr, null, 1));
