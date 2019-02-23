# Largest product in a series
# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
_1 = '73167176531330624919225119674426574742355349194934'
_2 = '96983520312774506326239578318016984801869478851843'
_3 = '85861560789112949495459501737958331952853208805511'
_4 = '12540698747158523863050715693290963295227443043557'
_5 = '66896648950445244523161731856403098711121722383113'
_6 = '62229893423380308135336276614282806444486645238749'
_7 = '30358907296290491560440772390713810515859307960866'
_8 = '70172427121883998797908792274921901699720888093776'
_9 = '65727333001053367881220235421809751254540594752243'
_10 = '52584907711670556013604839586446706324415722155397'
_11 = '53697817977846174064955149290862569321978468622482'
_12 = '83972241375657056057490261407972968652414535100474'
_13 = '82166370484403199890008895243450658541227588666881'
_14 = '16427171479924442928230863465674813919123162824586'
_15 = '17866458359124566529476545682848912883142607690042'
_16 = '24219022671055626321111109370544217506941658960408'
_17 = '07198403850962455444362981230987879927244284909188'
_18 = '84580156166097919133875499200524063689912560717606'
_19 = '05886116467109405077541002256983155200055935729725'
_20 = '71636269561882670428252483600823257530420752963450'
number = _1 + _2 +_3 + _4 +_5 + _6 + _7 +_8 + _9 +_10 + _11 + _12 +_13 + _14 +_15 + _16 + _17 +_18 + _19 + _20
product_list = []
def adjacent_numbers(index,number):
    return number[index:index+13]
def product_numbers(num):
    product = 1
    if '0' in num:
        return 0
    else:
        for i in num:
            product = product * int(i)
        return product

for index in range(1,1000-12):
        num = adjacent_numbers(index,number)
        product_list.append(product_numbers(num))

print(max(product_list))

#answer
#23514624000