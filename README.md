# odoo-truck-trailer-weight-distribution
Odoo 18: Modul za Raspodjelu Težine Paketa između Kamiona i Prikolice
Ovaj Odoo 18 modul razvijen je kao rješenje tehničkog zadatka. Cilj je omogućiti funkcionalnost na obrascu prodajnog predračuna koja pomaže korisnicima u ravnomjernoj raspodjeli težine paketa između kamiona i prikolice.

Opis Problema (Sažetak iz ZADATAK.pdf)
Korisnik mora prevesti teške pakete koristeći kamion i prikolicu. Kako bi se osigurala optimalna ravnoteža opterećenja i upravljivost vozila, sustav bi trebao pomoći u raspodjeli paketa tako da:

Paketi se utovaruju redoslijedom kojim su uneseni.

Sustav najprije pokušava napraviti izravnu podjelu popisa paketa na dvije podliste (kamion i prikolica) s jednakim ukupnim težinama.

Ako izravna podjela nije moguća, sustav pokušava pronaći pivot paket. Taj se paket smatra "između" kamiona i prikolice, a zbroj težina paketa prije pivot paketa (kamion) treba biti jednak zbroju težina paketa nakon pivot paketa (prikolica).

Ako nijedna metoda ne daje ravnomjernu raspodjelu, označava se kao "Nije moguće".

Implementirane Funkcionalnosti
Dodaje novu karticu "Kamion s prikolicom" u obrazac prodajnog naloga (predračuna) u Odoo-u.

Pruža ulazno polje Težine paketa gdje korisnik unosi niz prirodnih brojeva (težina paketa) odvojenih zarezima.

Automatski računa i prikazuje raspodjelu paketa u dva polja:

Kamion: Prikazuje popis paketa za kamion.

Prikolica: Prikazuje popis paketa za prikolicu.

Prikazuje "Nije moguće" ako raspodjela prema pravilima nije ostvariva.

Izračun poštuje fiksni redoslijed unesenih paketa.

Tehnički Detalji
Odoo Verzija: 18.0

Naziv Modula: uvid_sale_weight_distribution (prema predlošku)

Osnovna Logika: Implementirana u models/sale_order.py proširivanjem modela sale.order i dodavanjem metode za izračun _compute_weight_distribution koja se aktivira promjenom ulaza za težine paketa.

Izmjena Pogleda: Nova kartica i polja dodani su u sale.view_order_form pomoću naslijeđenog XML pogleda definiranog u views/sale_order_views.xml.

Okruženje za Postavljanje i Testiranje
Modul je razvijen i testiran na Ubuntu 24.04.

Kao baza podataka korišten je PostgreSQL.

Slijeđene su standardne procedure za instalaciju Odoo 18.
