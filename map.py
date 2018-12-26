# map

# aplly function call to each elements to iterable or data
# highly favorable when working with for large collection of data syntax



# map(function, iterable_object) --. iterator object

# note:function could be standard function or lambda expression, but most of the time we use lambda expression.


# amounts =[100, 200, 300, 500, 800]
# after_calc = map(lambda amount , interst=5: amount*(1+interest/100), amounts)
# print(list(after_calc))





# exercise 
# make the name using string to lower case using map

# name = ['Nima, dawa, Bishal, Sagar']
# name_lower = map(lambda nam  :nam.lower(), name)
# print(list(name_lower))


# names = ['Nima, dawa, Bishal, Sagar']
# print(list(map(str.lower,names)))


# for lambda 
# a = range(-10, 10)
# list(a)
# set(filter(lambda x: x>0,a))


# from functools import reduce
# reduce(lambda x, y: x*y, ranfe(1, 6))
