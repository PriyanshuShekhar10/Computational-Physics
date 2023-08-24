const math = require("mathjs");

const f_x = (x) => {
  return x * Math.exp(-1 * x);
};

let lower_bound = 0.2;
let upper_bound = 1.4;
let array_of_bounds = [0.2, 1.4];
let integral = [];

const simpson_rule = (lb, ub) => {
  return 10 * ((ub - lb) / 3) * (f_x(lb) + f_x((ub + lb) / 2) + f_x(lb));
};

console.log(`The integral of f(x), 1 step: ${simpson_rule(0.6, 1.4)}`);

const integration = () => {
  let number_of_steps = 2;
  let integration_sum = 0;
  let lb = array_of_bounds[0],
    ub = array_of_bounds[1];

  for (number_of_steps; number_of_steps <= 20; number_of_steps++) {
    let spacing = (ub - lb) / number_of_steps;
    let expandedArray = [];
    for (let i = 0; i < number_of_steps + 1; i++) {
      expandedArray.push(lb + i * spacing);
    }
    // console.log(`the expanded array for bounds is : ${expandedArray}`);

    for (let i = 0; i < expandedArray.length - 1; i++) {
      //   integration_sum =
      //     integration_sum + simpson_rule(expandedArray[i], expandedArray[i + 1]);

      console.log(simpson_rule(expandedArray[i], expandedArray[i + 1]));
    }

    console.log(
      `The integral of f(x), ${number_of_steps} step: ${integration_sum}`
    );
  }
};

integration();
// const integration = () => {
//   let number_of_steps = 1;
//   let integral_sum = 0;

//   for (number_of_steps; number_of_steps <= 100; number_of_steps++) {
//     /* updating bounds */
//     array_of_bounds.splice(array_of_bounds.length - 1, 0, () => {
//       return (
//         (array_of_bounds[array_of_bounds.length - 1] +
//           array_of_bounds[array_of_bounds.length]) /
//         2
//       );
//     });
//     /**/

//     for (let i = 1; i < number_of_steps + 2; i++) {
//       integral_sum += simpson_rule(array_of_bounds[i - 1], array_of_bounds[i]);
//     }

//     console.log(`Integral of function, 1 Step : ${integral_sum}`);
//     let final_integration = integral_sum;
//     integral_sum = 0;
//     integral.push({ integral: final_integration, step: number_of_steps });
//   }
// };

// integration();
