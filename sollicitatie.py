print(""" ---------------------------------------------------------------------
hallo u heeft hier een paar vragen die u moet beantwoorden
als u onze vragen kunt beantwoorden kunnen we gaan kijken of u op een gesprek kunt
----------------------------------------------------------------------""")

# Alle vragen

Dierenvraag = input("heeft u meer dan 4 jaar praktijk ervaring in dieren-dressuur? J/N :")
Jongleervraag = input("heeft u meer dan 5 jaar jongleer ervaring? J/N :")
Acrobatiekvraag = input("heeft u meer dan 3 jaar praktijk ervaring in acrobatiek? J/N :")
mbo4vraag = input("bent u in bezit van een mbo-4 diploma? J/N :")   
Vrachtwagenbewijsvraag = input("bent u in bezit van een vrachtwagenrijbewijs? J/N :")
Hogehoedvraag = input("bent u in bezit van een hogehoed? J/N :")

#man of vrouw vraag

manofvrouwVraag = input("Bent u een Man of Vrouw? :")
if manofvrouwVraag == "man":
    Manvraag = input("heeft u een snor die langer dan 10 cm is? J/N :")
else:
    Vrouwvraag = input("heeft u rood haar en krullen? J/N :")

Langervraag = input("bent u langer dan 150 cm? J/N :")
zwaardervraag = input("bent u zwaarder dan 90 kilo? J/N :")

eindresultaat = Dierenvraag == "j" or Jongleervraag == "j" or Acrobatiekvraag == "j" and mbo4vraag == "j" and Vrachtwagenbewijsvraag == "j" and Hogehoedvraag == "j" and Manvraag == "j" and Vrouwvraag == "j" and Langervraag == "j" and zwaardervraag == "j"

if eindresultaat:
    print("We willen u graag uitnodigen voor gesprek")
else:
    print("sorry we kunnen u niet verder helpen")