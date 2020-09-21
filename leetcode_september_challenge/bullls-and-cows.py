"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = {}
        for i in secret:
            secret_count[i] = secret_count.get(i, 0) + 1

        cow_index = []
        cow = 0
        bull = 0

        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bull = bull + 1
                secret_count[secret[i]] = secret_count[secret[i]] - 1
            else:
                cow_index.append(i)

        for index in cow_index:
            #count[secret[index]] = count[secret[index]] - 1
            if guess[index] not in secret_count:
                continue
            if secret_count[guess[index]] > 0:
                secret_count[guess[index]] = secret_count[guess[index]] - 1
                cow = cow + 1
                print (index)
        print ("{}A{}B".format(bull, cow))
        return "{}A{}B".format(bull, cow)


if __name__ == '__main__':
    print("Running version comparison Program")

    secret = "1807"
    guess = "7810"
    print("Case 1 : secret : {}, guess : {}".format(secret, guess))
    sol = Solution().getHint(secret, guess)
    print("Solution : {}".format(sol))

    secret = "1122"
    guess = "2211"
    print("Case 2 : secret : {}, guess : {}".format(secret, guess))
    sol = Solution().getHint(secret, guess)
    print("Solution : {}".format(sol))

    secret = "1123"
    guess = "0111"
    print("Case 3 : secret : {}, guess : {}".format(secret, guess))
    sol = Solution().getHint(secret, guess)
    print("Solution : {}".format(sol))

    secret = "1232"
    guess = "0111"
    print("Case 4 : secret : {}, guess : {}".format(secret, guess))
    sol = Solution().getHint(secret, guess)
    print("Solution : {}".format(sol))
