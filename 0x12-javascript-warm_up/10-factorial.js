#!/usr/bin/node

const input = parseInt(process.argv[2]);

function factorial (input) {
  if (input === 0 || input === 1) {
    return (1);
  } else {
    return input * factorial(input - 1);
  }
}

if (isNaN(input)) {
  console.log(1);
} else {
  console.log(factorial(input));
}
