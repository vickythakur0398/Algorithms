

''' devide  n conquor algo   '''
"""
1) Initialize count as 0
2) Sort all numbers in increasing order.
3) Remove duplicates from array.
4) Do following for each element arr[i]
   a) Binary Search for arr[i] + k in subarray from i+1 to n-1.
   b) If arr[i] + k found, increment count. 
5) Return count. 

"""

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        
        mid = len(alist)//2

        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        

        mergeSort(lefthalf)
    
        mergeSort(righthalf)
    
        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)



"""
******************************************************************************************************************
result delete this whole comment   



('Splitting ', [54, 26, 93, 17, 77, 31, 44, 55, 20])
('Splitting ', [54, 26, 93, 17])
('Splitting ', [54, 26])
('Splitting ', [54])
('Merging ', [54])
('Splitting ', [26])
('Merging ', [26])
('Merging ', [26, 54])
('Splitting ', [93, 17])
('Splitting ', [93])
('Merging ', [93])
('Splitting ', [17])
('Merging ', [17])
('Merging ', [17, 93])
('Merging ', [17, 26, 54, 93])
('Splitting ', [77, 31, 44, 55, 20])
('Splitting ', [77, 31])
('Splitting ', [77])
('Merging ', [77])
('Splitting ', [31])
('Merging ', [31])
('Merging ', [31, 77])
('Splitting ', [44, 55, 20])
('Splitting ', [44])
('Merging ', [44])
('Splitting ', [55, 20])
('Splitting ', [55])
('Merging ', [55])
('Splitting ', [20])
('Merging ', [20])
('Merging ', [20, 55])
('Merging ', [20, 44, 55])
('Merging ', [20, 31, 44, 55, 77])
('Merging ', [17, 20, 26, 31, 44, 54, 55, 77, 93])
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""






