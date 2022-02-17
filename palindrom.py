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
            palindrome_string
            count = self.cut_string(palindrome_string)

            return count

    def cut_string(self, string: str) -> int:
        # print(string)
        letters = {}
        for letter in string:
            pals = []
            pals_lit = []
            if letter not in letters.keys():
                occ = [m.start() for m in re.finditer(letter, string)]
                print("letter", letter)
                count = len(occ)
                if count > 1:
                    for i in range(count - 1):
                        print(i)
                        for j in range(1, count):
                            is_pal = string[occ[i]:occ[j] + 1]
                            print("check", is_pal)
                            if self.is_palindrome(is_pal):
                                pals.append((occ[i], occ[j] + 1))
                                pals_lit.append(is_pal)
                # print("pal", pal)
                if pals:
                    best_combo = {'length': 0, 'index': [0, 1]}
                    longest = 0
                    count = len(pals)-1
                    if count > 1:
                        for i in range(count):
                            for j in range(1, count):
                                # index = []
                                a, b = pals[i]
                                ab = b - a
                                c, d = pals[j]
                                cd = d-c
                                if c >= b:
                                    length = d - a - (c - b)
                                    index = [a,b,c,d]
                                else:
                                    if ab > cd:
                                        length = ab
                                        index = [a,b]
                                    else:
                                        length = cd
                                        index = [c, d]
                                if length > best_combo['length']:
                                    best_combo['length'] = length
                                    best_combo['index'] = index
                    else:
                        a, b = pals[0]
                        best_combo['length'] = b-a
                        best_combo['index'] = [a,b]

                    letters[letter] = best_combo
                print(pals)
                print(pals_lit)
        print(letters)
        long_pal = ""
        if letters:
            return len(letters)
        else:
            return len(string) - 1
        # print("letters", letters)



if __name__ == '__main__':
    pal = CuttingPalindromesPython()
    print(pal.is_palindrome("otto"))
    print(pal.is_palindrome("java"))
    print(pal.is_palindrome("a"))
    print("otto", pal.minimum_palindrome_cuts("otto"))
    print("python", pal.minimum_palindrome_cuts("python"))
    print("reward", pal.minimum_palindrome_cuts("reward"))
    print("radarlevel", pal.minimum_palindrome_cuts("radarlevel"))
    # print("radarrefer", pal.minimum_palindrome_cuts("radarrefer"))
    # print("levels", pal.minimum_palindrome_cuts("levels"))
    # print("wowaphplevel", pal.minimum_palindrome_cuts("wowaphplevel"))
    # print("wowpshplevel", pal.minimum_palindrome_cuts("wowpshplevel"))
    # print("wowakayak", pal.minimum_palindrome_cuts("wowakayak"))
    print("aabaababa", pal.minimum_palindrome_cuts("aabaababa"))
    # print("xyxyyzyyy", pal.minimum_palindrome_cuts("xyxyyzyyy"))
    # print("abaxabbx", pal.minimum_palindrome_cuts("abaxabbx"))
