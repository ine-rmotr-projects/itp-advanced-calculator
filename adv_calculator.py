def add(*args):
    return sum(args)

    # ALTERNATIVE SOLUTION
    # total = 0
    # for arg in args:
    #     total += arg 
    # return total 


def multiply(*args):
    total = 1 
    for arg in args:
        total *= arg 
    return total 


def maximum(*args):
    return max(args)
    
    # ALTERNATIVE SOLUTION
    # greatest_num = None

    # for arg in args: 
    #     if greatest_num == None or arg > greatest_num:
    #         greatest_num = arg
    # return greatest_num
  
def minimum(*args):
    return min(args)

    # ALTERNATIVE SOLUTION
    # lowest_num = None 

    # for arg in args: 
    #     if lowest_num == None or arg < lowest_num:
    #         lowest_num = arg
    # return lowest_num

def mean(*args): 
    return sum(args) / len(args)

    # ALTERNATIVE SOLUTION
    # total = 0 
    # for arg in args:
    #     total += arg 

    # return total/len(args)

def variance(*args):
    _mean = mean(*args)
    variance_sum_total = 0
    for arg in args:
        variance_sum_total += (arg - _mean) ** 2
    return variance_sum_total / len(args)



def std(*args):
    def sqrt(x):
        return x**(1/2)
    return sqrt(variance(*args))