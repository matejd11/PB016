def member(prvok, zoznam):
	if prvok in zoznam:
		return 'True'
	return 'False'

def main():
	print("Príklad na zistenie, či je prvok v zozname: member('a', ['a', 'b', 'c'])")
	print(member('a', ['a', 'b', 'c']))

if __name__ == '__main__':
    main()