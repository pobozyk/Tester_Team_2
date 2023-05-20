def wybor_plci():
	gender = input("Podaj plec: K/M")
	if gender == "K":
		print("woman")
	elif gender == "M":
		print("men")
	else:
		print("Wybor nieprawidlowy")

wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if wiek>=18 and wiek<40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	wybor_plci()
elif wiek>=40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
	wybor_plci()
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")