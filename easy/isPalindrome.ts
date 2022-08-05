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
  const str = x.toString();
  const len = str.length;
  const firstHalf = str.slice(0, len / 2);
  const secondHalf = str.slice(0, -(len % 2) - 1);
  const reverseSecondHalf = secondHalf.length == 1 ? secondHalf : secondHalf.split("").reverse().join("");
  console.log(firstHalf, reverseSecondHalf)
  if (firstHalf == reverseSecondHalf) return true;
  return false;
}

[121, -121, 10, 100, 11].forEach((num) => {
  console.log(isPalindromeP2(num));
});
