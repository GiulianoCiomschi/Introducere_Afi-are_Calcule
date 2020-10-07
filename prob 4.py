#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
#albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
#globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
#albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. 

n=int(input("dați nr. globuri:"))
nr=n+3
na=(n+nr)-2
nt=n+na+nr
print("Pe bread sunt",nt,"globuri")