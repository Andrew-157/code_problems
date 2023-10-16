class Solution:
    def intToRoman(self, num: int) -> str:
        matches = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        num_str = str(num)
        counter = len(num_str)
        roman = ''

        for i in num_str:
            if i == '0':
                counter -= 1
                continue
            else:
                leading = int(i)
                number = int(f'{i}{"0" * (counter - 1)}')
                if number in matches:
                    roman += matches[number]
                    counter -= 1
                else:
                    if number > 1 and number < 4:
                        roman += 'I' * leading
                    elif number > 5 and number < 9:
                        roman += 'V' + 'I' * (leading - 5)
                    elif number > 10 and number < 40:
                        roman += 'X' * leading
                    elif number > 50 and number < 90:
                        roman += 'L' + 'X' * (leading - 5)
                    elif number > 100 and number < 400:
                        roman += 'C' * leading
                    elif number > 500 and number < 900:
                        roman += 'D' + 'C' * (leading - 5)
                    else:
                        roman += 'M' * leading
                    counter -= 1

        return roman


sol = Solution()
print(sol.intToRoman(1994))
print(sol.intToRoman(3891))
print(sol.intToRoman(3000))
print(sol.intToRoman(2))
