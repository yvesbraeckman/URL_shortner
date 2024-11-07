def make_chocolate_sauce():
    print("verwarm 100 ml room samen met 50 gram suiker in een pan op middelhoog vuur tot de suiker is opgelost. Voeg vervolgens 100 gram pure chocolade toe en roer tot de chocolade volledig is gesmolten en de saus glad is. Haal de pan van het vuur en voeg eventueel een theelepel vanille-extract toe voor extra smaak.")


def make_caramel():
    print("smelt 200 gram kristalsuiker in een pan op middelhoog vuur zonder te roeren, totdat de suiker een diep gouden kleur krijgt. Voeg voorzichtig 100 ml warme slagroom toe terwijl constant wordt geroerd; wees voorzichtig, want het mengsel kan spatten. Roer tot de saus glad is en voeg dan 50 gram boter toe; blijf roeren tot alles goed gemengd is. Laat de saus afkoelen voordat deze wordt geserveerd.")


def make_donut(saus):
    print("meng 500 gram bloem met 7 gram droge gist, 60 gram suiker en een theelepel zout in een grote kom. Maak een kuiltje in het midden en voeg 250 ml warme melk, 2 eieren en 60 gram gesmolten boter toe. Kneed het geheel tot een zacht en elastisch deeg en laat het vervolgens afgedekt ongeveer een uur rijzen op een warme plek tot het in volume is verdubbeld. Rol het deeg uit tot een dikte van ongeveer 1 centimeter en steek er rondjes uit met een uitsteker; maak desgewenst een gat in het midden voor traditionele donuts. Leg de donuts op een met bakpapier beklede bakplaat en laat ze nog eens 30 minuten rijzen. Verhit plantaardige olie in een diepe pan tot 180°C en frituur de donuts in porties goudbruin aan beide kanten. Laat ze uitlekken op keukenpapier en bestrooi ze met poedersuiker of glazuur ze naar wens.")
    print("\n")
    saus()


make_donut(make_chocolate_sauce)