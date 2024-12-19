#!/usr/bin/node
const input = parseInt(process.argv[2]);
if (isNaN(input)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < input) {
    console.log('C is fun');
    i++;
  }
}
