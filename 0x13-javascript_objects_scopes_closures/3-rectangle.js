#!/usr/bin/node
class Rectangle {
	constructor (h, w) {
		if (h <= 0 && w <= 0) {
			this.height = undefined;
			this.width = undefined;
		} else {
			this.height = h;
			this.width = w;
		}
	}

print() {
	let stringDisp = '';
    for (let x = 0; x < this.width; x++) {
    for (let y = 0; y < this.height; y++) {
        stringDisp += 'X';
      }
      console.log(stringDisp);
      stringDisp = '';
    }
  }
}
