const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
const Math = require("math");

const f_x = (x) => {
  return x ^ (2 - 16);
};

const df_x = (x) => {
  return 2 * x;
};

let x_0;
let aerr;
let maxitr;
let x_1;

readline.question("Enter the initial Guess", (x) => {
  x_0 = x;
  readline.close();
});

readline.question("Enter the error", (x) => {
  aerr = x;
  readline.close();
});

console.log(`aerr: ${aerr}  initial_guess: ${x_0}`);

const func = () => {
  const h = () => {
    return f_x(x_0) / df_x(x_0);
  };

  x_1 = x_0 - h();
};
func();

for (let i = 0; i <= 1000; i++) {
  if (Math.abs(h()) >= aerr) console.log(x_0, f_x(x_0));
  else func();
}
