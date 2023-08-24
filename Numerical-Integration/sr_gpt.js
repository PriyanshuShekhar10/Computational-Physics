const math = require("mathjs");

const f_x = (x) => {
  return x * math.exp(-1 * x);
};

let lower_bound = 0.2;
let upper_bound = 1.4;
let array_of_bounds = [lower_bound, upper_bound];
let integral = [];

const simpson_rule = (lb, ub) => {
  return ((ub - lb) / 6) * (f_x(lb) + 4 * f_x((ub + lb) / 2) + f_x(ub)); // Correct Simpson's rule formula
};

const integration = () => {
  let number_of_steps = 1;

  for (number_of_steps; number_of_steps <= 20; number_of_steps++) {
    // Update bounds
    const newBounds = [];
    for (let i = 0; i < array_of_bounds.length - 1; i++) {
      newBounds.push(array_of_bounds[i]);
      newBounds.push((array_of_bounds[i] + array_of_bounds[i + 1]) / 2);
    }
    newBounds.push(array_of_bounds[array_of_bounds.length - 1]);
    array_of_bounds = newBounds;

    let integral_sum = 0;
    for (let i = 1; i < array_of_bounds.length; i += 2) {
      integral_sum += simpson_rule(array_of_bounds[i - 1], array_of_bounds[i]);
    }

    console.log(
      `Integral of function, ${number_of_steps} Steps : ${integral_sum}`
    );
    integral.push({ integral: integral_sum, step: number_of_steps });
  }
};

integration();
console.log(integral);
