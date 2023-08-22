const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
const math = require("mathjs");

let alpha, a, V_0, E, m, h_;
let beta, x_0, aerr, x_1;

readline.question("Enter the value of V_0: ", (value) => {
  V_0 = parseFloat(value);
  readline.question("Enter the value of E: ", (y) => {
    E = parseFloat(y);
    readline.question("Enter the value of a: ", (aVal) => {
      a = parseFloat(aVal);
      readline.question("Enter the initial Guess: ", (x) => {
        x_0 = parseFloat(x);
        readline.question("Enter the error: ", (error) => {
          aerr = parseFloat(error);
          readline.close();
          console.log(`aerr: ${aerr}  initial_guess: ${x_0}`);
          initializeVariables();
          performNewtonRaphson();
        });
      });
    });
  });
});

const initializeVariables = () => {
  alpha = beta / a;
  m = h_ ** 2 / 0.076199682;
};

const f_x = (x) => {
  return beta * math.cos(alpha * a) - alpha * math.sin(alpha * a);
};

const df_x = (x) => {
  return (
    -1 * alpha * beta * math.sin(alpha * a) -
    alpha * alpha * math.cos(alpha * a)
  );
};

const func = (x) => {
  const h = f_x(x) / df_x(x);
  x_1 = x - h;
};

const performNewtonRaphson = () => {
  for (i = 0; i <= 1000; i++) {
    if (Math.abs(f_x(x_0)) >= aerr) {
      console.log(`Iteration ${i}: x = ${x_0}, f(x) = ${f_x(x_0)}`);
      func(x_0);
      x_0 = x_1;
    } else {
      break;
    }
  }

  if (i > 1000) {
    console.log("Iteration limit reached without convergence.");
  } else {
    console.log(`Converged to a solution: x = ${x_0}, f(x) = ${f_x(x_0)}`);
  }
};
