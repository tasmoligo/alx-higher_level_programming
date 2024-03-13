#!/usr/bin/node
// returns the number of occurrences in a list:
exports.nbOccurences = function occurence (list, searchElement) {
  let i = 0, count = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      count++;
    }
    i++;
  }
  return (count);
}
