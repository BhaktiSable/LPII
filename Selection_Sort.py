def SelectionSort(array,size):
    for i in range(size):
        max_idx=i
        for j in range(i+1,size):
            if array[max_idx]>array[j]:
                max_idx=j
        array[i],array[max_idx]=array[max_idx],array[i]
if __name__=='__main__':
    while True:
        print("-----Menu------")
        print("\n1.To Enter element in the list:")
        print("\n2.to get soretd list using selection sort")
        print("\n3.End the Program:")
        ch=int(input("\nEnter your choice: "))
        if ch==1:
            list=[]
            n=int(input("Enter the number elements: "))
            print("Enter the numbers: ")
            for i in range(0,n):
                e=int(input())
                list.append(e)
            size=len(list)
            print(list)
        if ch==2:
            SelectionSort(list,size)
            print("Sorted array in ascending array: ")
            print(list)
        if ch==3:
            print("End")
            break