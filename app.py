region = input("Wybierz region (EUR/USA): ")
if region == "EUR":
    print("Wybrałeś region EUR (Europa).")
elif region == "USA":
    print("Wybrałeś region USA (Stany Zjednoczone")
wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if wiek>=18 and wiek<40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>=40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

