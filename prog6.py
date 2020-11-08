# imie = "Ala"
# zwierze = "kot"
# ile = 5
#
# if ile == 1:
#     print("{0} ma {1}a".format(imie, zwierze))
# else:
#     print("{0} ma {1} {2}ow".format(imie, ile, zwierze))

marka_samochodu = "Opel"
rocznik = 1988
status = "stary"

if rocznik <= 2000:
    print("{0} z {1} jest {2}".format(marka_samochodu, rocznik, status))
else:
    print("{0} z {1} jest nowy".format(marka_samochodu, rocznik, status))
