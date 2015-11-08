def permutacie(prvky):
    if len(prvky) <=1:
        yield prvky
    else:
        for perm in permutacie(prvky[1:]):
            for i in range(len(prvky)):
                yield perm[:i] + prvky[0:1] + perm[i:]

def main():
    for i in permutacie([1, 2, 3]):
    	print(i)

if __name__ == '__main__':
    main()