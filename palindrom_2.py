import re


class CuttingPalindromesPython:

    def is_palindrome(self, string):
        # Implement this in test scenario 1
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
        slice_at = [m.start() for m in re.finditer(string[0], string)]
        if len(slice_at) == 1:
            if len(string) == 1:
                return string, ""
            else:
                return string[0], string[1:]
        else:
            first = string[:slice_at[1] + 1]
            second = string[slice_at[1] + 1:]
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
    print(pal.minimum_palindrome_cuts("wowaphplevel"))
    print(pal.minimum_palindrome_cuts("wowpshplevel"))
