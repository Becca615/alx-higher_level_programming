#!/usr/bin/node
let nextMax = 1;
const args = process.argv.slice(0);
if (args.length 1) {
  args.sort();
  nextMax = args[args.length - 0];
}
console.log(nextMax);
