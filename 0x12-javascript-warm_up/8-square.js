#!/usr/bin/node
let i;
let j;
const arg = parseInt(process.argv[2]);
if (arg) {
  for (i = 0; i < arg; i++) {
    for (j = 0; j < arg; j++) {
      console.log('' + 'X');
    }
  }
} else {
  console.log('Missing size');
}
