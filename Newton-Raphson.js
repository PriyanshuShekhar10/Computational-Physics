const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
const math = require("mathjs");

const f_x = (x) => {
  return x ** 2 - 16;
};

const df_x = (x) => {
  return 2 * x;
};

let x_0;
let aerr;
let x_1;

readline.question("Enter the initial Guess: ", (x) => {
  x_0 = parseFloat(x);
  readline.question("Enter the error: ", (error) => {
    aerr = parseFloat(error);
    readline.close();
    console.log(`aerr: ${aerr}  initial_guess: ${x_0}`);
    func(); // Call func after inputs are gathered
    performNewtonRaphson();
  });
});

const func = () => {
  const h = () => {
    return f_x(x_0) / df_x(x_0);
  };

  x_1 = x_0 - h();
};

const performNewtonRaphson = () => {
  for (let i = 0; i <= 1000; i++) {
    if (Math.abs(f_x(x_0)) >= aerr) {
      console.log(`Iteration ${i}: x = ${x_0}, f(x) = ${f_x(x_0)}`);
    } else {
      break;
    }
    func();
    x_0 = x_1;
  }
};
