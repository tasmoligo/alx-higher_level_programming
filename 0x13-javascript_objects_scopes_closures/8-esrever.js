#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function revList (list) {
  let firstIdx = 0;
  let lastIdx = list.length - 1;
  while (firstIdx < lastIdx) {
    const temp = list[firstIdx];
    list[firstIdx] = list[lastIdx];
    list[lastIdx] = temp;
    firstIdx++;
    lastIdx--;
  }
  return (list);
};
