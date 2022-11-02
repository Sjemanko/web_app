from lab3.models import Osoba, Druzyna
Osoba.objects.all()
Osoba.objects.get(id=3)
Osoba.objects.filter(imie\_\_startswith="Thomas")
--
--
Druzyna.objects.order_by('nazwa')
new_person = Osoba(imie="imie1", nazwisko="nazwisko1", miesiac_urodzenia=5, druzyna=Druzyna.objects.get(id=1))
