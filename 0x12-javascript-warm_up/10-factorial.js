#!/usr/bin/node

const arg = process.argv.slice(2);

if (isNaN(arg[0])) {
  console.log(1);
}

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(arg[0]));
