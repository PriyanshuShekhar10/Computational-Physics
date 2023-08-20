const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
const math = require("mathjs");

//finite potential problem in Quantum Mechanics

let beta, alpha, a, V_0, E, m, h_;

//to remove the high order value of h_ and m

m = h_ ** 2 / 0.076199682;

beta = math.sqrt(2 * (V_0 - E) * (m / h_ ** 2));

const f_x = () => {
  return beta * math.cos(alpha * a) - alpha * math.sin(alpha * a);
};

const df_x = () => {
  return (
    -1 * alpha * beta * math.sin(alpha * a) -
    alpha * alpha * math.cos(alpha * a)
  );
};

let x_0;
let aerr;
let x_1;

readline.question("Enter the value of V_0", (value) => {
  V_0 = parseFloat(value);
  readline.question("Enter the value of E", (y) => {
    E = parseFloat(y);
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
