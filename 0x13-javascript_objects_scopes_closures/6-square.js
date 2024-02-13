#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    let output = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        output += 'X';
      }
      output += '\n';
    }
    console.log(output);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
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
      output += '\n';
    }
    console.log(output);
  }
}
module.exports = NewSquare;
