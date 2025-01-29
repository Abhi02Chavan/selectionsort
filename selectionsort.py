def selectionsort(array):
    for i in range (len(array)):
        for j in range(len(array)):
            if array[j] < array[i]:
                array[i],array[j]=array[j],array[i]
    return array
                
            
# size=int(input("enter the size of array: "))
# array=[]
# while size !=0:
#     element=input("enter your elemnt: ")
#     array.append(element)
#     size = size-1
# print(f"Your entered array is : {array}")
array=[23,21,43,56,12,32]
sortedarray=selectionsort(array)
arrayt=int(reversed(sortedarray))
print(arrayt)
