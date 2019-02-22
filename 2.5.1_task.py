def mod_checker(x, mod=0):
    return lambda y: y % x == mod
mod_3 = mod_checker(3)
print(type(mod_3))
print(mod_3(3))
print(mod_3(4))
print(mod_3(26))
print(mod_3(10))
print(mod_3(11))
print(mod_3(15))
mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
