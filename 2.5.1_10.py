def quickSort(array=[12,4,5,6,7,3,1,15]):
    mensie = []
    rovne = []
    vatsie = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                mensie.append(x)
            if x == pivot:
                rovne.append(x)
            if x > pivot:
                vatsie.append(x)
        return quickSort(mensie)+rovne+quickSort(vatsie)  # + na spojenie zoznamov
    # pozor potrebujes     rovne ^^^^^ nie povot
    else:  # base case, ukoncenie rekurzie, ak je v poli iba jeden prvok
        return array

def main():
    # pre veľké zoznamy
    # sys.setrecursionlimit(10000) 
    print("Príklad použitia QuickSort-u na zozname [5, 2, 8, 2, 654, 8, 3, 4]")
    print(quickSort([5, 2, 8, 2, 654, 8, 3, 4]))

if __name__ == '__main__':
    main()