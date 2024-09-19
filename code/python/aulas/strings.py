# intializing
str_00 = "I am a string"
str_01 = 'I am a string too'
str_03 = """I am a multline string
I can jump line and rewrite these characters: ' and "

This is all"""

# contac
str_04 = str_00 + str_01
str_05 = str_00 * 5

"a" in str_00 # -->> returns a booelan

### Formatação de String
# F-String
f_string = f"String #0: '{str_00}', String #1: '{str_01}'"

# str.format()
str_format = "String #0: '{}', String #1: '{}'".format(str_00, str_01)

# old school
old_school = "String #0: '%s', String #1: '%s'" % (str_00, str_01)
