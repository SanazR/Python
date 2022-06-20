def power(base_num,pow_num):
    result = 1
    for indeex in range(pow_num):
        result = result *base_num
    return result

print (power(2,8))    