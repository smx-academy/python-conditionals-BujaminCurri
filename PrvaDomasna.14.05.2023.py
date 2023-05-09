#1 Zadaca: Напишете програма која ќе 
# прочита два броја од корисникот и ќе го 
# испечати збирот, разликата, производот и 
# количникот на двата броја. 
# Споредете кој резултат е поголем, збирот или производот

"""broj1 = int(input('Vnesete go vasiot prv broj: '))
broj2 = int(input('Vnesete go vasiot vtor broj: '))

print('Vasiot prv broj e {}.'.format(broj1))
print('Vasiot vtor broj e {}.'.format(broj2))

zbir = broj1 + broj2
print('Zbirot na vasite broevi {} + {} e: {}.'.format(broj1, broj2, zbir))"""

#razlikata1 = abs(broj1 - broj2)
#razlikata mozeme da ja resime i so funkcijata abs, kade sto rezultatot
#sto ke go dobieme ako e negativen da ni se pretvora vo pozitivna brojka
#no jas resiv da ja resam so if uslovot, bidejki ne znaeme dali prvata
#brojka e negativna ili ne bidejki korisnikot ke vnese podatoci, pa ja 
#resiv na vakov nacin, mozebi postoi i pokratok pat no za mene 
#ova mi e popregledno i polesno svatlivo.

"""razlikata1 = abs(broj1 - broj2)
print('Razlikata na vasite broevi e: {}'.format(razlikata1))
razlika = broj1 - broj2
if broj1 < broj2:
    razlikata = broj2 - broj1
    print('Razlikata na vasite broevi {} - {} e: {}.'.format(broj2, broj1, razlikata))
else:
    print('Razlikata na vasite broevi {} - {} e: {}.'.format(broj1, broj2, razlika))

proizvod = broj1 * broj2
print('Proizvodot na vasite broevi {} * {} e: {}.'.format(broj1, broj2, proizvod))

kolicnik = broj1 / broj2
print('Kolicnikot na vasite broevi {} / {} e: {}.'.format(broj1, broj2, kolicnik))"""


#2 Zadaca: Напишете програма која ќе прочита 
# број од корисникот и ќе го провери дали тој 
# е деллив со 3, 5, 3 и 5, а 
# потоа ќе испечати соодветната порака.

"""korisnik1 = int(input('Vnesete go vasiot broj: '))
print('Vasiot broj koj go vnesovte e: {}.'.format(korisnik1))

if korisnik1 %3 == 0 and korisnik1 %5 == 0:
    print('Vasiot broj {} e deliv so brojot 3 i 5.'.format(korisnik1))
elif korisnik1 % 5 == 0:
    print('Vasiot broj {} e deliv so brojot 5.'.format(korisnik1))
elif korisnik1 %3 == 0:
    print('Vasiot broj {} e deliv so brojot 3.'.format(korisnik1))
else:
    print('Vasiot broj {} ne e deliv so brojot 3 i 5.'.format(korisnik1))"""


#3 Zadaca: Напишете програма која ќе прочита број 
#од корисникот и ќе го провери дали тој е парен, 
#и потоа ќе испечати соодветната порака.

"""korisnik = int(input('Vnesete go vasiot broj: '))
print('Vasiot broj koj go vnesovte e: {}.'.format(korisnik))

if korisnik %2==0:
    print('Vasiot broj {} e paren broj.'.format(korisnik))
else:
    print('Vasiot broj {} e neparen broj.'.format(korisnik))"""


#4 Zadaca: Напишете програма која ќе прочита 
#два броја од корисникот и ќе го испечати збирот 
#на броевите помеѓу нив што се делливи со 4.

"""korisnik10 = int(input('Vnesete go vasiot prv broj: '))
korisnik11 = int(input('Vnesete go vasiot vtor broj: '))

zbir12 = korisnik10 + korisnik11

if zbir12 % 4 == 0:
    print('Zbirot na vasite dva broevi {} e deliv so brojot 4.'.format(zbir12))
else:
    print('Zbirot na vasite dva broevi {} ne e deliv so brojot 4.'.format(zbir12))"""


#5 Zadaca: Напишете програма која ќе прочита 
# два броја од корисникот и ќе го испечати 
# производот на броевите, да се провери дали 
# резултатот е парен или не парен.

"""korisnik6 = int(input('Vnesete go vasiot prv broj: '))
korisnik7 = int(input('Vnesete go vasiot vtor broj: '))

proizvod = korisnik6 * korisnik7

if proizvod % 2 == 0:
    print('Proizvodot na vasite dva broevi {} e paren broj.'.format(proizvod))
else:
    print('Proizvodot na vasite dva broevi {} e neparen broj.'.format(proizvod))"""


#6 Zadaca: Напишете програма која ќе прочита 
# страни на правоаголник и квадрат, да се пресмета 
# плоштината и да се провери дали збирот 
# на плоштините е деллив со 2,3 или 5

"""stranaA = int(input('Vnesete dimenzii na stranaA od pravoagolnikot: '))
stranaB = int(input('Vnesete dimenzii na stranaB od pravoagolnikot: '))

stranaD = int(input('Vnesete dimenzii na stranaD od kvadratot: '))

plostinapravoagolnik = stranaA * stranaB
plostinakvadrat = 4 * stranaD

if plostinapravoagolnik % 2 == 0:
    print('Plostinata na vasiot triagolnik {} e deliv so brojot 2.'.format(plostinapravoagolnik))
elif plostinapravoagolnik % 3 == 0:
    print('Plostinata na vasiot triagolnik {} e deliv so brojot 3.'.format(plostinapravoagolnik))
elif plostinapravoagolnik % 5 == 0:
    print('Plostinata na vasiot triagolnik {} e deeliv so brojot 5.'.format(plostinapravoagolnik))
else:
    print('Plostinata na vasiot triagolnik {} ne e deliv so brojot 2, 3 ili 5.'.format(plostinapravoagolnik))

if plostinakvadrat % 2 == 0:
    print('Plostinata na vasiot kvadrat {} e deliv so brojot 2.'.format(plostinakvadrat))
elif plostinakvadrat % 3 == 0:
    print('Plostinata na vasiot kvadrat {} e deliv so brojot 3.'.format(plostinakvadrat))
elif plostinakvadrat % 5 == 0:
    print('Plostinata na vasiot kvadrat {} e deliv so brojot 5.'.format(plostinakvadrat))
else: 
    print('Plostinata na vasiot kvadrat {} ne e deliv so brojot 2, 3 ili 5.'.format(plostinakvadrat))"""

#7 Zadaca: Напишете програма која ќе прочита 
# големина на агли во триаголник, да се провери 
# дали може да се формира триаголник со 
# тие агли(збирот мора да биде 180) и ако може да 
# се формира триаголник да се провери 
# каков триаголник може да се формира

"""alfa = int(input("Vnesete golemina na alfa agolot od triagolnikot: "))
beta = int(input("Vnesete golemina na beta agolot od triagolnikot: "))
gama = int(input("Vnesete golemina na gama agolot od triagolnikot: "))

zbirot = alfa + beta + gama
print('Zbriot na trite agli od vasiot triagolnik e {}.'.format(zbirot))

if zbirot == 180:
    print('Vasiot triagolnik e so golemina od {} stepeni.'.format(zbirot))
    if alfa == 90 or beta == 90 or gama == 90:
        print('Vasiot triagolnik e PRAVOAGOLEN')
    elif alfa < 90 or beta < 90 or gama < 90:
        print('Vasiot triagolnik e OSTROAGOLEN')
    elif alfa > 90 or beta > 90 or gama > 90:
        print('Vasiot triagolnik e TAPOAGOLEN')
else:
    print('Ne moze da se formira triagolnik od 180 stepeni')"""

#Bonus Zadaca: Да се напише програма која ќе прочита 
# година од корисникот и да одреди дали е 
# годината престапна (разгледајте и размислете како може да се креира вакво нешто)

"""ime = input('Vnesete go vaseto ime: ')
prezime = input('Vnesete go vaseto prezime: ')
godina = int(input('{} {} ve molime vnesete go vaseto godina na raganje: '.format(ime.capitalize(), prezime.capitalize())))

if godina % 4 == 0:
    if godina % 100 == 0:
        if godina % 400 == 0:
            print('{} {} vasata godina na raganje {} e pristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))
        else:
            print('{} {} vasata godina na raganje {} e nepristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))
    else:
        print('{} {} vasata godina na raganje {} e pristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))
else:
    print('{} {} vasata godina na raganje {} e nepristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))"""


"""ime = input('Vnesete go vaseto ime: ')
prezime = input('Vnesete go vaseto prezime: ')
godina = int(input('{} {} ve molime vnesete go vaseto godina na raganje: '.format(ime.capitalize(), prezime.capitalize())))

if godina % 4 == 0:
    print('{} {} vasata godina na raganje {} e pristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))
else:
    print('{} {} vasata godina na raganje {} e nepristapna godina.'.format(ime.capitalize(),prezime.capitalize(),godina))"""
  