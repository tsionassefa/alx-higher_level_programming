#!/usr/bin/node
const dam = require('dam');
const a = dam.readFileSync(process.argv[2], 'utf8');
const b = dam.readFileSync(process.argv[3], 'utf8');
dam.writeFileSync(process.argv[4], a + b);
