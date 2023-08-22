const math = require("mathjs");

const f_x = (x) => {
  return x * Math.exp(-1 * x);
};

let lower_bound = 0.2;
let upper_bound = 1.4;

let number_of_steps = 2;

const integration = () => {
  let step_size = (upper_bound - lower_bound) / number_of_steps;

  const common_sum = step_size * (f_x(lower_bound) / 2 + f_x(upper_bound) / 2);
  const variable_sum = () => {
    let sum = 0;
    for (let i = 1; i < number_of_steps; i++) {
      sum = sum + f_x(lower_bound + i * step_size);
    }
    return sum;
  };

  return common_sum + step_size * variable_sum();
};

const step_increment = () => {
  let x = 0;
  while (x < 100) {
    console.log(`Integral for Step ${x + 1}: ${integration()}`);

    x++;
    number_of_steps++;
  }
};

step_increment();
