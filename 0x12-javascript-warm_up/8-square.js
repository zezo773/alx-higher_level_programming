#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = number
if (isNaN(number))
	console.log("Missing size");
else
	while (i > 0) {
		console.log("X".repeat(number));
		i--;
	}
