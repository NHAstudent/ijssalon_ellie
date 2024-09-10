prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5",
}
Aanbieding = 3 * 0.8
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {Aanbieding}")
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
el = reclame_tekst4
for i in el:
    (len(i))
    if len(i)>4:
        print(i.upper())
    else:
        print(i.lower())