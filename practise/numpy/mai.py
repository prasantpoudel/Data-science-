# arr=[6,1,2,8,3,4,7,10,5]
# arr=[1,2,3,5]
# n=5

# def dis(arr,n):
#     arr.sort()
#     for i in range(n):
#         if arr[i]+1==arr[i+1]:
#             continue
#         else:
#             return arr[i]+1
# print(dis(arr,n))

# arr=[2,3,1,2,3]

# # arr=[0,3,1,2]
# arr=[13,9,25,1,1,0,22,13,22,20,3,8,11,25,10,3,15,11,19,20,2,4,25,14,23,14]
# n=len(arr)

# def occ(arr,n):
    
    # b=[]
    # for i in range(n-1):
        
    #     if arr[i]==arr[i+1]:
    #         if arr[i] not in b:
    #             b.append(arr[i])
            
                
        
    # if len(b)>=1:
    #     return b
    # else:
    #     return [-1]
#     A=[]
#     s=[]
#     for i in range(n):
#         if len(s) and arr[i] in s:
#             A.append(arr[i])
#         else:
#             s.append(arr[i])
#         if (len(A)==0):
#            return [-1]
#         else:
#            return A
        
    

# ans=occ(arr,n)
# for i in ans:
#     print(i,end=" ")
    
n=8

def findsqrt(n):
    low =1
    high=n
    ans=0
    while low<=high:
        mid=int((high+low)/2)
        sqr=mid*mid
        
        if sqr==n:
            return mid
        elif sqr<n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return mid
print(findsqrt(n))
