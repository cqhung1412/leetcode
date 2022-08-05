const validChars = ["I", "V", "X", "L", "C", "D", "M"];

const romanNumberMap = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = function (s) {
  if (s.length < 1 || s.length > 15) throw new Error("Invalid string length");
  if (!/^[IVXLCDM]+$/.test(s)) throw new Error("Invalid character in string");
  let total = 0;
  const reversedStringArray = s.split("").reverse();
  reversedStringArray.forEach((roman, index) => {
    if (index == 0) {
      total += romanNumberMap[roman];
    } else if (
      romanNumberMap[roman] < romanNumberMap[reversedStringArray[index - 1]]
    ) {
      total -= romanNumberMap[roman];
    } else {
      total += romanNumberMap[roman];
    }
  });

  return total;
};


["III", "LVIII", "MCMXCIV"].forEach((num) => {
  console.log(romanToInt(num));
});