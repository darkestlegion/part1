odp = random.randint(1, 100)

while (true) :
    kostka = input("wspisz liczbę od 1 do 100")

    if(kostka == odp): 
        print("wygraeś")
        break 
    elif (kostka < opd):
        print ("liczba jest więksksza")
    else:
        print ("liczba jest mniejsza")        

