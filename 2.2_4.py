def delete(prvok, list):
    i = len(list) -1

    while i >= 0:
        if list[i] == prvok:
            list.pop(i)
        i -= 1    

    return list

def delete1(prvok, list):
    index = list.index(prvok)
    list.pop(index)
    return list

def insert(prvok, list):
    return list.append(prvok)

def main():
    a = [1,2,1,1,2,3,1,1]
    print("Príklad pridania '1' do zoznamu [1,2,1,1,2,3,1,1]")
    insert(1, a)
    print(a)
    print("Príklad vymazania jednej '1' do zoznamu")
    delete1(1, a)
    print(a)
    print("Príklad vymazania vsetkých '1' do zoznamu")
    delete(1, a)
    print(a)

if __name__ == '__main__':
    main()