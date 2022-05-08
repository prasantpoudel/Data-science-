def sort(a,n):
    lo=0
    mid=0
    hi=n-1
    while mid<=hi:
        if a[mid]==0:
            a[lo],a[mid]=a[mid],a[lo]
            lo=lo+1
            mid=mid+1
        elif a[mid]==1:
            mid=mid+1
        else:
            a[mid],a[hi]=a[hi],[mid]
            hi=hi-1
    return a
def printarray(a):
    for k in a:
        print(k,end='')

arr=[1,2,1,2,0,1,0,2,0]
arr_size=len(arr)
sort(arr,arr_size)
print("the  sorted arrayed is:")
printarray(arr)
