# import math
#
# print(math.ceil(3.5))
# print(math.ceil(3.4))
# print(math.floor(3.5))
# print(math.floor(3.4))
# print(math.pow(2, 10))
# print(math.sin(math.pi / 2))
#
# import random
#
# print(random.random())
# print(random.randrange(1, 10))
# print(random.randint(1, 10))
# list1 = ['김치찌개', '비빔면', '안먹고 잠']
# print(random.choice(list1))
#
# print('before: ', list1)
# random.shuffle(list1)
# print('after: ', list1)
#
# print(random.sample(list1, 2))

import datetime

now = datetime.datetime.now()
birthday = datetime.datetime(2004, 5, 14, 0)
print(birthday)
print(now - birthday)
