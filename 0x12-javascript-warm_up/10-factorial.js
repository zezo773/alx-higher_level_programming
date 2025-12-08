#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial(n) {
	if (isNaN(n) || n < 0)
		return (1);
	if (n === 1 || n === 0)
		return (1);
	else
		return (n * factorial(n - 1));
}
const result = factorial(num);
console.log(result);
