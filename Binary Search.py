def bs(vals, low, high, target):

    while(low<high):

        mid=(low+high)//2

        if vals[mid]>target:
            high=mid-1
        elif vals[mid]<target:
            low=mid+1
        else:
            return mid
    
    return -1