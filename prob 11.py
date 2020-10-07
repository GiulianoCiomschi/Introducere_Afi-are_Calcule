#Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
#începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
#realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
#iepuri sunt în crescătorie?

n1=int(input(" nr. Iepuri la început de luna "))
n2=int(input(" nr. iepuri morti "))
n3=int(input(" nr. iepuri nascuti  "))
nt=n1-n2+n3
print("La sfarsitul lunei sunt",nt,"iepuri")
