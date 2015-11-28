def permutacie(prvky):
    if len(prvky) <=1:
        yield prvky
    else:
        for perm in permutacie(prvky[1:]):
            for i in range(len(prvky)):
                yield perm[:i] + prvky[0:1] + perm[i:]

def sum(values): # s e n d m o r y
    return 10000*values[4] + 1000*values[5] + 100*values[2] + 10*values[1] + values[7]  

def add(values): # s e n d m o r y
    return 1000*(values[0] + values[4]) + 100*(values[1] +  values[5]) + 10*(values[2] + values[6]) + values[3] + values[1]  

def main():
    print("CLP - Algebrogram")
    print("  S E N D")
    print("+ M O R E")
    print("---------")
    print("M O N E Y")

    for num in permutacie(list(range(10))):
        if sum(num) == add(num):
            if num[0] != 0 and num[4] != 0:
                print(num)

if __name__ == '__main__':
    main()


