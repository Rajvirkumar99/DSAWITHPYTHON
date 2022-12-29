# how to calculate the power of number using recursion

def PowerNumber2(base,exp):
    assert int(exp)==exp,'Must we integer number Number '
    if exp==0:
        return 1
    return base *PowerNumber2(base,exp-1)
print(PowerNumber2(5,4))
