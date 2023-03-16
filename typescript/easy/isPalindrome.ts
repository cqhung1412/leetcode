function isPalindromeP1(x) {
  const str = x.toString();
  const len = str.length;
  for (let i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) return false;
  }
  return true;
}

function isPalindromeP2(x) {
  if (x < 0 || (x < 100 && x >= 10 && x % 11 !== 0)) return false;
  if (x >= 0 && x < 10) return true;

  let reversed = 0;
  let remainder = x;
  let original = x;

  while (x !== 0) {
    remainder = x % 10;
    reversed = reversed * 10 + remainder;
    x = Math.floor(x / 10);
  }

  return reversed === original;
}

[121, -121, 10, 100, 11].forEach((num) => {
  console.log(isPalindromeP2(num));
});
