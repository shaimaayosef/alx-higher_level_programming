#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }

  print () {
    if (this.width && this.height) {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output += 'X';
        }
        output += '\n';
      }
      console.log(output);
    }
  }

  rotate () {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Rectangle;
