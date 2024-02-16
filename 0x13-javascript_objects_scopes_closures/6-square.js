#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        return {}; // Create an empty object
      }
      this.width = w;
      this.height = h;
    }
  
    print() {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  
    rotate() {
      [this.width, this.height] = [this.height, this.width];
    }
  
    double() {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
}
class NewSquare extends Square {
    charPrint (c) {
        let output = '';
        const printChar = c !== undefined ? c : 'X';
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                output += printChar;
            }
            if (i < this.height - 1) {
                output += '\n';
            }
        }
        console.log(output);
    }
}
module.exports = NewSquare;
