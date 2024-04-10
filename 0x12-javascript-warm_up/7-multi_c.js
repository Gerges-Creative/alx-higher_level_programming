#!/usr/bin/node

const arg = process.argv.slice(2);

const num = parseInt(arg[0], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

let i = 0;

while (i < num) {
  console.log('C is fun');
  i++;
}
