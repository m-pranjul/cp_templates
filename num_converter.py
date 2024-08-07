class num_converter:
    ones = ["",         "One",      "Two",       "Three",     "Four",
            "Five",     "Six",      "Seven",     "Eight",     "Nine",
            "Ten",      "Eleven",   "Twelve",    "Thirteen",  "Fourteen",
            "Fifteen",  "Sixteen",  "Seventeen", "Eighteen",  "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    trip = ["" , "Thousand" , "Million" , "Billion" , "Trillion"]


    def triples(self, num):
        ans = ""
    
        if num >= 100:
            r = num % 100
            num //= 100
            ans += self.ones[num] + " Hundred "
            num = r


        if num >= 20:
            r = num % 10
            ans += self.tens[num//10]
            if r > 0:
                ans += " " + self.ones[r]

        elif num > 0:
            ans += self.ones[num]

        return ans.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        ans = ""
        c = 0
        while num > 0:
            r = num%1000
            num //= 1000

            if r:
                temp = self.triples(r) + " " + self.trip[c]
                ans = temp if (ans == "") else temp + " " + ans
            c+=1

        return ans.strip()

if __name__ == "__main__":

    obj = num_converter()
    
    num = int(input("Enter the Number to convert into alphabets: "))

    ans = obj.numberToWords(num)

    print(ans)