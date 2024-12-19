#!/usr/bin/node
const input = parseInt(process.argv[2]);
if (isNaN(input)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < input; i++) {
    let row = '';
    for (let j = 0; j < input; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
