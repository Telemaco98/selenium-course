# There is not a type to represent a matrix. But we can represent it with lists:

matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix[0]       # [0, 1, 2]
matrix[0][1:]   # [1, 2]

matrix3d = [[[1, 2, 3]], [[4, 5, 6]]]
matrix3d[0][0][0]   # 1
matrix3d[1][0][2]   # 6

"""
Methods of List

>>> dir(List)

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__',
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Plus: Underscore in Python = https://www.datacamp.com/tutorial/role-underscore-python
"""

x = [1, 2, 3]

x.append(4)          # x = [1, 2, 3, 4]         -> Insert in the end
x.insert(0, -1)      # x = [-1, 1, 2, 3, 4]     -> Insert in the position i = 0 the number y = -1
x.remove(2)          # x = [-1, 1, 3, 4]        -> Removes the value y = 2
x.pop()              # x = [-1, 1, 3]            -> Removes the last value
x.count(2)           # 0                        -> Counts how many values equals y = 2 there are in the list
x.reverse()          # x = [3, 1, -1]           -> Reverses the list
