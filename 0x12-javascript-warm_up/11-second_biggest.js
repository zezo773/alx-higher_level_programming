#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);

if (argv.length < 2) {
	console.log(0);
	return;
}
let larg = -Infinity;
let slarg = -Infinity;
for (let n of argv) {
	if (n > larg)
		larg = n;
}
for (let n of argv) {
	if (n > slarg && n !== larg)
		slarg = n;
}
console.log(slarg);
