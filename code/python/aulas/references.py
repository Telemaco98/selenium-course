name = input('Whats your name? ')
age = input('How old are you? ')

print(name)
print(age)

# del name <- deletes the instance of memory
# print(name) <- daria erro "NameError: name "name" is not define"

age_type = type(age) # <- retorna o tipo da variável
print(age_type)

age_methods = dir(age) # returns the object methods list
print(age_methods)
