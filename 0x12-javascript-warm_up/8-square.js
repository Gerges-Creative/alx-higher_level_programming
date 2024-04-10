#!/usr/bin/node

const arg = process.argv.slice(2);

const num = parseInt(arg[0], 10);

if (isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let square = '';
  for (let j = 0; j < num; j++) {
    square += 'X';
  }

  console.log(square);
}
