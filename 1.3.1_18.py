import sys

def fib_rec(i):
	if i < 3:
		return 1
	return fib_rec(i - 1) + fib_rec(i - 2)

def fib_iter(i):
	array = [1, 1]
	for j in range(2, i):
		array.append(array[j-1] + array[j-2])
	return array[i-1]  # pole indexujeme od nuly

def main():
	# pre veľké čísla
	# sys.setrecursionlimit(10000)
	print("Príklad na výpočet fibonaciho postupnosti")
	print("pomalšia verzia (rekurzívna): fib_rec(27)")
	print(fib_rec(27))
	print("rýchlejšia verzia (iteračná): fib_iter(27)")
	print(fib_iter(27))

if __name__ == '__main__':
    main()