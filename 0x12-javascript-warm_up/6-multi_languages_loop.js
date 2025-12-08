#!/usr/bin/node
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let out = '';
for (let i = 0; i < arr.length; i++) {
  out += arr[i];
  if (i < arr.length - 1) out += '\n';
}
console.log(out);
