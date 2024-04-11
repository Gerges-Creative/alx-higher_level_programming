#!/usr/bin/node

const arg = process.argv.slice(2);

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(arg[0]));
