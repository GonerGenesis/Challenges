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
            palindrome_string = [palindrome_string]
            while len(palindrome_string) != 0:
                print(palindrome_string)
                palindroms = []
                # palindrome_string = palindrome_string.replace(self.cut_string(palindrome_string), "", 1)
                left = []
                for string in palindrome_string:
                    # if len(string) == 1:
                    #     continue
                    pal = self.cut_string(string)
                    string = list(string.partition(pal))
                    string = list(filter(('').__ne__, string))
                    string.remove(pal)
                    left += string
                    i += 1
                print(palindrome_string)
                palindrome_string = left
                print(palindrome_string)
            return len(palindrome_string) - 1 if i == 0 else i - 1

    def cut_string(self, string: str) -> str:
        # print(string)
        slice_fwd = [m.start() for m in re.finditer(string[0], string)]
        slice_bwd = [m.start() for m in re.finditer(string[-1], string[::-1])]
        letters = {}
        for letter in string:
            if letter not in letters.keys():
                pal = letter
                occ = [m.start() for m in re.finditer(letter, string)]
                # print("occ", occ)
                count = len(occ)
                if count > 1:
                    for i in range(count - 1):
                        # print(range(1, count-1))
                        for j in range(1, count):
                            is_pal = string[occ[i]:occ[j] + 1]
                            # print("check", is_pal)
                            if self.is_palindrome(is_pal) and len(is_pal) > len(pal):
                                pal = is_pal
                # print("pal", pal)
                letters[letter] = pal
        long_pal = ""
        # print("letters", letters)
        for let, pal in letters.items():
            # print(let, pal)
            if len(pal) > len(long_pal):
                long_pal = pal
        print("longest pal", long_pal)
        return long_pal


if __name__ == '__main__':
    pal = CuttingPalindromesPython()
    print(pal.is_palindrome("otto"))
    print(pal.is_palindrome("java"))
    print(pal.is_palindrome("a"))
    print("otto", pal.minimum_palindrome_cuts("otto"))
    print("python", pal.minimum_palindrome_cuts("python"))
    print("reward", pal.minimum_palindrome_cuts("reward"))
    print("radarlevel", pal.minimum_palindrome_cuts("radarlevel"))
    print("radarrefer", pal.minimum_palindrome_cuts("radarrefer"))
    print("levels", pal.minimum_palindrome_cuts("levels"))
    print("wowaphplevel", pal.minimum_palindrome_cuts("wowaphplevel"))
    print("wowpshplevel", pal.minimum_palindrome_cuts("wowpshplevel"))
    print("wowakayak", pal.minimum_palindrome_cuts("wowakayak"))
    print("aabaababa", pal.minimum_palindrome_cuts("aabaababa"))
    print("xyxyyzyyy", pal.minimum_palindrome_cuts("xyxyyzyyy"))
    print("abaxabbx", pal.minimum_palindrome_cuts("abaxabbx"))
