class RomanNumerals:
    roman = {
        "1": "I",
        "4": "IV",
        "5": "V",
        "9": "IX",
        "10": "X",
        "40": "XL",
        "50": "L",
        "90": "XC",
        "100": "C",
        "400": "CD",
        "500": "D",
        "900": "CM",
        "1000": "M"
    }
    
    decimal={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000, 
        }
    def to_roman(val):
        val = str(val)
        int_list = []
        roman_list = []
        for i, digit in enumerate(val):
            if digit != "0":
                int_list.append(digit+"0"*len(val[i+1:]))
        for element in int_list:
            roman_digit = RomanNumerals.roman.get(element, 0)
            if roman_digit != 0:
                roman_list.append(roman_digit)
            else:
                multiplier = int(element[0])
                element = "1"+element[1:]
                if multiplier > 5:
                    element = "1"+element[1:]
                    roman_list.append(RomanNumerals.roman.get("5"+element[1:], 0))
                    multiplier=multiplier-5
                roman_list.append(RomanNumerals.roman.get(element, 0)*multiplier)   
        # print(roman_list)
        return "".join(roman_list)

    def from_roman(roman_num):
        number=0
        for i,element in enumerate(roman_num):
            roman_number=RomanNumerals.decimal.get(element)
            if len(roman_num)>i+1:
                next_roman=RomanNumerals.decimal.get(roman_num[i+1])
                if next_roman<=roman_number:
                    number+=roman_number
                else:
                    number-=roman_number
            else:
                number+=roman_number
        return number