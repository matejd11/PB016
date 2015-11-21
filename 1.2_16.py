def vypis(array, odsadenie = 1):
    if not type(array) is list:
        return str(array)
    odpoved = ''
    odpoved += "zoznam:[\n"
    for i, x in enumerate(array): 
        # enumerate(list) okrem prechádzania poľa, nám udržiava poradové číslo aktuálneho prvku
        odpoved += "\t"*odsadenie + str(i) + ": " + vypis(x, odsadenie+1) + '\n'
    odpoved += "\t"*(odsadenie-1) + "]"
    return odpoved

def main():
    print("Príklad na krajší výpis zoznamu.")
    print("zoznam ['a', 'b', 'c'] sa zobrazí:")
    print(vypis(['a', 'b', 'c']))
    print("zoznam: ['a', 'b', ['c1', 'c2', 'c3'], 'd', 'mezi d a e', 'e'] sa zobrazí:")
    print(vypis(['a', 'b', ['c1', 'c2', 'c3'], 'd', 'mezi d a e', 'e']))

if __name__ == '__main__':
    main()