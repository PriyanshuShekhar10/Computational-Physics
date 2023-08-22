const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const math = require("mathjs");

let a, b, c, e, Root;
readline.question("Input Left limit guess: ", (x_l) => {
  a = parseFloat(x_l);
  readline.question("Input Right limit guess: ", (x_r) => {
    c = parseFloat(x_r);
    readline.question("Enter the error limit: ", (error) => {
      e = parseFloat(error);
      readline.close();
      console.log(`Left guess: ${a}, Right guess: ${c}, Error Limit: ${e}`);
      performBisection();
    });
  });
});

const givenFunction = (x) => {
  return math.cube(x) - 4 * x - 9;
};

const performBisection = () => {
  b = (a + c) / 2;
  if (Math.abs(a - c) < e) {
    Root = b;
    console.log(`The final root is: ${Root}`);
  } else {
    const functionAtA = givenFunction(a);
    const functionAtB = givenFunction(b);
    if (functionAtA * functionAtB < 0) {
      c = b;
    } else {
      a = b;
    }
    performBisection();
  }
};
