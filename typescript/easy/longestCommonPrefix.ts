function longestCommonPrefixP1(strs) {
  const substrs = strs.map((str) => {
    const len = str.length;
    if (len == 1) return [str];
    const substrArr = [];
    for (let j = 1; j < len; j++) {
      substrArr.push(str.slice(0, j));
    }
    return [...substrArr, str];
  });
  console.log(substrs);

  let longest = "";
  let minSubstrArrLength = Math.min(
    ...substrs.map((substrArr) => substrArr.length)
  );
  let minLengthArrIndex = substrs.findIndex(
    (substrArr) => substrArr.length === minSubstrArrLength
  );
  if (substrs[minLengthArrIndex].length !== 1)
    substrs[minLengthArrIndex].sort((a, b) => a.length - b.length);
  for (const element of substrs[minLengthArrIndex]) {
    const strForCompare = element;
    let isCommon = true;
    for (let j = 0; j < substrs.length; j++) {
      if (j == minLengthArrIndex) continue;
      if (!substrs[j].includes(strForCompare)) isCommon = false;
    }
    if (isCommon) {
      longest = strForCompare;
    }
  }
  console.log("longest:", longest);
  return longest;
}

function longestCommonPrefixP2(strs) {
  const minLength = Math.min(...strs.map((str) => str.length));
  const minLengthIndex = strs.findIndex((str) => str.length === minLength);
  let longest = "";
  for (let j = 0; j < strs[minLengthIndex].length; j++) {
    let isCommon = true;
    for (let i = 0; i < strs.length; i++) {
      if (i == minLengthIndex) continue;
      if (strs[i].substring(0, j) !== strs[minLengthIndex].substring(0, j))
        isCommon = false;
    }
    if (isCommon) {
      longest =
        j == 0 ? strs[minLengthIndex] : strs[minLengthIndex].substring(0, j);
    }
  }
  console.log("longest:", longest);
  return longest;
}

longestCommonPrefixP2(["flower", "flow", "flight"]);
longestCommonPrefixP2(["dog", "racecar", "car"]);
longestCommonPrefixP2(["a"]);
longestCommonPrefixP2(["a", "ab"]);
longestCommonPrefixP2(["reflower", "flow", "flight"]);
longestCommonPrefixP2(["flower", "flower", "flower", "flower"]);
