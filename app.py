def wybor_plci():
  gender = input("Podaj plec [K/M]:").upper()
  if gender == "K":
    print("woman")
  elif gender == "M":
    print("men")
  else:
    exit("Wybor nieprawidlowy, wprowadz poprawnie K lub M")
  return gender

def wybor_regionu():
  region = input("Wybierz region (EUR/USA): ")
  if region == "EUR":
    print("Wybrałeś region EUR (Europa).")

  elif region == "USA":
    print("Wybrałeś region USA (Stany Zjednoczone")
  return region

def sprawdzenie_poprawnosci_wieku():
  if wiek > 120:
	  print('Wprowadzono wiek powyzej 120 lat. ')
	  print('Czy na pewno masz tyle lat?')
    exit("Zamykam aplikacje")
    # Sprawdzamy czy podany wiek jest liczbą
  elif wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")    

def obslugaUSA():  
  if wybrany_region == "USA" and wiek<21:
    exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
  if wiek >= 30 and gender == 'K':
    print("Otrzymujesz aperol spritz pierwszy gratis!")
  if wiek>=18 and wiek<40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
  elif wiek>=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
  else:
    exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

def obslugaEUR():
   if wybrany_region == "EUR" and wiek<18:
    exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
  if wiek >= 30 and gender == 'K':
    print("Otrzymujesz aperol spritz pierwszy gratis!")
  if wiek>=18 and wiek<40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
  elif wiek>=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
  else:
    exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
sprawdzenie_poprawnosci_wieku()
wiek=int(wiek)    
    
#Poczatek dzialania aplikacji
gender = wybor_plci()
wybrany_region = wybor_regionu()

if wybrany_region == "USA":
  print("Wybrano region USA")
  obslugaUSA()
  
elif wybrany_region == "EUR":
  print("Wybrano region EUR")
  obslugaEUR()  
else
  exit("Aplikacja nie obsługuje użytkowników z regionów innych niż EUR/USA")