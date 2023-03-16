/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    const find = target - nums[i];
    if (Number.isInteger(map[`${find}`])) return [map[`${find}`], i];
    map[`${nums[i]}`] = i;
  }
};

const testNums = [2, 7, 11, 15];
const testTarget = 9;

console.log(twoSum(testNums, testTarget));
