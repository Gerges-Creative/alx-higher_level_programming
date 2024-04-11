#!/usr/bin/node

function add (a, b) {
  const c = parseInt(a) + parseInt(b);
  console.log(c);
}

const arg = process.argv.slice(2);

add(arg[0], arg[1]);
