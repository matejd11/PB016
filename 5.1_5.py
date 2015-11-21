def hanoi(n, zaciatocna, cielova, pomocna):
    if n > 0:
        
        hanoi(n - 1, zaciatocna, pomocna, cielova)

        if zaciatocna[0]:
            disk = zaciatocna[0].pop()
            print("presúvam " + str(disk) + " z " + zaciatocna[1] + " na " + cielova[1])
            cielova[0].append(disk)

        hanoi(n - 1, pomocna, cielova, zaciatocna)
        
def main():
    print("Príklad hanojské veže:")
    zaciatocna = ([3,2,1], "A")
    cielova = ([], "B")
    pomocna = ([], "C")
    
    print(zaciatocna[0], cielova[0], pomocna[0])

    hanoi(len(zaciatocna[0]), zaciatocna, cielova, pomocna)

    print(zaciatocna[0], cielova[0], pomocna[0])

if __name__ == '__main__':
    main()