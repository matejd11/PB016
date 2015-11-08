def member(prvok, zoznam):
	if prvok in zoznam:
		return 'True'
	return 'False'

def main():
	print(member('a', ['a', 'b', 'c']))

if __name__ == '__main__':
    main()