#!/usr/bin/node

const arg = process.argv.slice(2);

let array = [];
for (let i = 0; i < arg.length; i++) {
  let num = Number(arg[i]);
  array.push(num);
}

function print2Biggest (arr, arrSize) {
  let i;
  let biggest = second = -2454635434;

  if (arrSize < 2) {
      console.log(0);
      return;
  }

  // Find the biggest element
  for (i = 0; i < arrSize; i++) {
      if (arr[i] > biggest) {
	  biggest = arr[i];
      }
  }

  // Find the second biggest element
  for (i = 0; i < arrSize; i++) {
      if (arr[i] > second && arr[i] < biggest) {
	  second = arr[i];
      }
  }

  if (second == -2454635434) {
      console.log(0);
  } else {
      console.log(second);
  }
}

  let n = array.length;
  print2Biggest(array, n);
