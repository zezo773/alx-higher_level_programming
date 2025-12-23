#!/usr/bin/node

exports.esrever = function (list) {
	let count = list.length - 1;
	let s = [];
	let i = 0;
	while (count >= 0) {
		s[i] = list[count];
		count--;
		i++;
	}
	return s;
}
