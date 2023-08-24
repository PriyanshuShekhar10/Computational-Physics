const math = require("mathjs");

const f_x = (x) => {
  return x * Math.exp(-1 * x);
};

let lower_bound = 0.2;
let upper_bound = 1.4;
let array_of_bounds = [lower_bound, upper_bound];
let integral = [];

const simpson_rule = (lb, ub) => {
  return ((ub - lb) / 3) * (f_x(lb) + f_x((ub + lb) / 2) + f_x(lb));
};

const integration = () => {
  let number_of_steps = 1;
  let integral_sum = 0;

  for (number_of_steps; number_of_steps <= 100; number_of_steps++) {
    /* updating bounds */
    array_of_bounds.splice(array_of_bounds.length - 1, 0, () => {
      return (
        (array_of_bounds[array_of_bounds.length - 1] +
          array_of_bounds[array_of_bounds.length]) /
        2
      );
    });
    /**/

    for (let i = 1; i < number_of_steps + 2; i++) {
      integral_sum += simpson_rule(array_of_bounds[i - 1], array_of_bounds[i]);
    }

    console.log(`Integral of function, 1 Step : ${integral_sum}`);
    let final_integration = integral_sum;
    integral_sum = 0;
    integral.push({ integral: final_integration, step: number_of_steps });
  }
};

integration();
