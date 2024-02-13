#!/usr/bin/node
const args = process.argv.slice(2);

const firstArg = Number(args[0]);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(firstArg)}`);
}
