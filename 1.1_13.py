class Osoba():
	"""trieda osoba"""
	def __init__(self, meno):
		self.meno = meno
		self.otec = None
		self.mama = None

	def nastavOtca(self, otec):
		self.otec = otec

	def nastavMamu(self, mama):
		self.mama = mama
		
	def ziskajRodicov(self):
		rodicia = []
		rodicia.append(self.otec)
		rodicia.append(self.mama)
		return rodicia

	def ziskajSurodencov(self, vsetci):
		surodenci = []

		for osoba in vsetci:
			if osoba != self:
				if osoba.ziskajRodicov() == self.ziskajRodicov():
					surodenci += [osoba]

		return surodenci

def main():
	dana = Osoba("dana")
	petr = Osoba("petr")
	david = Osoba("david")
	milan = Osoba("milan")
	jan = Osoba("jan")
	pavla = Osoba("pavla")
	jana = Osoba("jana")

	dana.nastavOtca(milan)
	petr.nastavOtca(milan)
	david.nastavOtca(jan)

	dana.nastavMamu(pavla)
	petr.nastavMamu(pavla)
	david.nastavMamu(jana)

	vsetci = [dana, petr, david, milan, jan, pavla, jana]

	print("Príklad na ukládanie a hľadanie v rodokmeni. (rodicia, surodenci)")
	print()

	print("dana.rodicia =>")

	for x in dana.ziskajRodicov():
		print(" ",x.meno)

	print("dana.surodenci =>")

	for x in dana.ziskajSurodencov(vsetci):
		print(" ",x.meno)


if __name__ == '__main__':
    main()