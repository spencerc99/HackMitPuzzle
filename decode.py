diff = ord('i') - ord('e');

inp = "Cnawp Oykpp! /oqydoaynap/a6b18wbbzx7xb9z92b289ww7bwbb1400y0313z09z24wy65zway81327b99aw529.fwn"

"""
Ep eo pda uawn IITREE. 1000 dwygano cwpdan wp pda Iwoowydqoappo Ejopepqpa kb Paydjkhkcu bkn epo wjjqwh qjzancnwzqwpa opqzajp dwygwpdkj
"""

def decode(inp):
    result = ""
    for letter in inp.upper():
        if not letter.isalpha():
            result += letter
        else:
            result += chr(ord('A') + ((ord(letter) + diff - ord('A')) % 26))
    return result.lower()

print (decode(inp))
