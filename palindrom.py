class CuttingPalindromesPython:
    # def __init__(self, init_string: str):
    #     self.init_string = init_string
    #     self.is_palindrome(self.init_string)

    def is_palindrome(self, string: str):
        # Implement this in test scenario 1
        length = len(string)
        print(length)
        print(range(length//2))
        for i in range(length//2):
            print(string[i])
            print(string[-(i+1)])
            if string[i] != string[-(i+1)]:
                return False
        return True

    def minimum_palindrome_cuts(self, palindrome_string: str) -> int:
        # Implement this in test scenario 2 and 3
        return 0


if __name__ == '__main__':
    pal = CuttingPalindromesPython()
    print(pal.is_palindrome("java"))
