def wybor_plci():
	gender = input("Podaj plec [K/M]:").upper()
	if gender == "K":
		print("woman")
	elif gender == "M":
		print("men")
	else:
		exit("Wybor nieprawidlowy")

	return gender
gender = wybor_plci()
wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")

# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
# sprawdzanie czy wybor płci jest poprawny
if gender.upper() != 'K' and gender.upper() != 'M':
	exit('podana płeć, powinno być K lub M!')
wiek=int(wiek)
if wiek >= 30 and gender.upper() == 'K':
	print("Otrzymujesz aperol spritz pierwszy gratis!")
if wiek>=18 and wiek<40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>=40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")