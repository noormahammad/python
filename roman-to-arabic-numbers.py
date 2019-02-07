def numerus(roman_numerals):

         roman_numerals = roman_numerals.lower()
         romans_dict = {"i":1, "v":5, "x":10, "l":50,"d":500, "c":100, "m":1000}
         total = 0;
         previous = 0;

         for numeral in list(reversed(roman_numerals)):
             if previous > romans_dict[numeral]:
                 total = total-romans_dict[numeral]
             else:
                 total += romans_dict[numeral];
                 previous = romans_dict[numeral];
         return total
