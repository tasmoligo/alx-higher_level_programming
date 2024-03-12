#!/usr/bin/node

n = parseInt(process.argv[2]);
function fact(n) {
  if (!n) {
    return (1);
  }
  return (n * fact(n -1));
}

console.log(fact(n));
