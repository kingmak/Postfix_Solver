from Parse import Parse # my parse class   

postfixStrings =    [
                        '4 5 +',             # 9
                        '9 3 /',             # 3
                        '17 8 -',            # 9
                        '6 2 / 5 +',         # 8
                        '4 5 + 7 2 -  *',    # 45
                        '4 5 7 2 + - *',     # -16
                        '3 4 + 2  * 7 /',    # 2 
                        '5 7 + 6 2 -  *',    # 48
                        '4 2 3 5 1 - + * +', # 18
                        '4 2 + 3 5 1 -  * +' # 18
                    ]

# input format : 'operand operand operator'
for string in postfixStrings:
    print '{:18} = {}'.format(string, Parse(string).evaluate())