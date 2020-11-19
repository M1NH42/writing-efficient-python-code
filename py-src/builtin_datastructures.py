# some python built-in data structures
# 1. lists
# 2. tuples
# 3. dictionary
# 4. sets

# **************LIST***************
fruits = ['apple', 'orange', 'grapes']

for i in range(len(fruits)):
    print(i, fruits[i])

# map upercase function
u_fruits = map(str.upper, fruits)

# for i in range(len(FRUITS)):
#     print(i, FRUITS[i])

# unpack
FRUITS = [*(u_fruits)]

for i in range(len(FRUITS)):
    print(i, FRUITS[i])
