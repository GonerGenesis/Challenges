import re

class CuttingPalindromesPython:
    # def __init__(self, init_string: str):
    #     self.init_string = init_string
    #     self.is_palindrome(self.init_string)

    def is_palindrome(self, string: str):
        # Implement this in test scenario 1

        # print(length)
        # print(range(length//2))
        if string == string[::-1]:
            return True
        else:
            return False

    def minimum_palindrome_cuts(self, palindrome_string) -> int:
        # Implement this in test scenario 2 and 3
        if self.is_palindrome(palindrome_string):
            return 0
        else:
            i = 0
            a, b = self.cut_string(palindrome_string)
            while len(b) != 0:
                if not self.is_palindrome(a):
                    i += self.minimum_palindrome_cuts(a)
                a, b = self.cut_string(b)
                i += 1
            return len(palindrome_string) - 1 if i == 0 else i

    def cut_string(self, string: str) -> (str, str):
        slice_fwd = [m.start() for m in re.finditer(string[0], string)]
        slice_bwd = [m.start() for m in re.finditer(string[-1], string[::-1])]
        print(string)
        if len(slice_fwd) == 1:
            if len(string) == 1:
                return string, ""
            else:
                first = string[0]
                second = string[1:]
        else:
            if len(slice_bwd) > 1 and slice_bwd[1] > slice_fwd[1]:
                string = string[::-1]
                slice_fwd = slice_bwd
            first = string[0]
            second = string[1:]
            for d in slice_fwd:
                if self.is_palindrome(string[:d+1]):
                    first = string[:d + 1]
                    second = string[d + 1:]
        print(first, second)
        return first, second


if __name__ == '__main__':
    pal = CuttingPalindromesPython()
    print(pal.is_palindrome("otto"))
    print(pal.is_palindrome("java"))
    print(pal.is_palindrome("a"))
    print(pal.minimum_palindrome_cuts("otto"))
    print(pal.minimum_palindrome_cuts("python"))
    print(pal.minimum_palindrome_cuts("radarlevel"))
    print(pal.minimum_palindrome_cuts("radarrefer"))
    print(pal.minimum_palindrome_cuts("levels"))
    print("wowaphplevel", pal.minimum_palindrome_cuts("wowaphplevel"))
    print("wowpshplevel", pal.minimum_palindrome_cuts("wowpshplevel"))
    print("wowakayak", pal.minimum_palindrome_cuts("wowakayak"))
    print("aabaababa", pal.minimum_palindrome_cuts("aabaababa"))
    print("xyxyyzyyy", pal.minimum_palindrome_cuts("xyxyyzyyy"))
    print("abaxabbx", pal.minimum_palindrome_cuts("abaxabbx"))
