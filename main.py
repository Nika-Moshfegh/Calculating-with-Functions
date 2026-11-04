def sum_for_list(lst):
    lst=[12,15]
    # for i in lst:
        # divisiton(i)
    

def divisiton(n):
    res=[]
    for i in range(2,n//2+1):
        if n%i==0:
            res.append(i)
    return res


def prime(lst):
    res=[]
    for i in lst:
        print(divisiton(i))
            # res.append(i)
    # return res

lst=[12,15]
print(
    prime([2,3,4,6])
)