#!/usr/bin/node

const arg = process.argv.slice(2).map(Number);

if (arg.length < 2) {
    console.log(0); 
} else {
    let largest = arg[0];
    let second_largest = arg[1];

    for (let i = 1; i < arg.length; i++) {

        if (arg[i] > largest) {
            second_largest = largest;
            largest = arg[i];
        }

        if (arg[i] > second_largest && arg[i] < largest) {
            second_largest = arg[i];
        }
    }
    console.log(second_largest);
}