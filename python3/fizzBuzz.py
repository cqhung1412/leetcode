class Solution:
    def addElement(self, current: int) -> str:
        string = str(current)
        isBy3 = current % 3 == 0
        isBy5 = current % 5 == 0
        if isBy3 and isBy5:
            string = "FizzBuzz"
        elif isBy3:
            string = "Fizz"
        elif isBy5:
            string = "Buzz"
        return string

    def fizzBuzz(self, n: int) -> list[str]:
        array = []
        for x in range(n):
            array.append(self.addElement(x+1))
        return array


if __name__ == "__main__":
    solution = Solution()
    print(solution.fizzBuzz(15))
