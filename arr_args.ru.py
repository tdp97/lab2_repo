def minarr (arr):
     a = arr [0]
     for i  in arr:
         if i < a:
             a = i
     return a

def avgarr(arr):
    summ = 0.0
    for i in arr :
        summ+=i
    return summ/len(arr)

arr1 = [4, 6, 2, 9, 4, 7, 13, 8, 0]
print(minarr(arr1))
print(avgarr(arr1))