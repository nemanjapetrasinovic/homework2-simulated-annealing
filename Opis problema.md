## Opis problema:

Problem koji je zamišljen za ovaj zadatak jeste problem rekreiranja fotografija. Naime programu se prosleđuje fotografija koju je potrebno rekreirati, a zatim program iscrtava trouglove različitih dimenzija kako bi što vernije rekreirao prosledjenu fotografiju. Algoritam korišćen za implementaciju ovog rešenja je algoritam simuliranog kaljenja. 

## Opis rešenja:
Dato rešenje predstavlja aplikaciju izrađenu u programskom jeziku *Python*, koristeći OpenCV za editovanje fotografija i iscrtavanje poligona.

Aplikacija sadrži klasu *imgLib.py*, ova klasa sadrži sve funkcije potrebne za učitavanje fotografija, zatim funkciju za iscrtavanje trouglova, funkciju koja računa razliku između dve fotografije, kao i funkciju za snimanje rezultujuće fotografije na disk.

Za algoritam simuliranog kaljenja potrebno je da imamo početno stanje. Početno stanje u ovom slučaju je fotografija sa belom pozadinom. 

Generisanje novog stanja odvija se tako što se na početnu, belu fotografiju, dodaje trougao nasumičnih dimenzija i nasumične boje. Za dodavanje novog trougla koristi se funkcija *drawTriangle*.

Funkcija *drawTriangle* iscrtava trougao. Za trougao se nasumično biraju koordinate, vodeći računa da izabrane koordinate ne smeju da budu veće od dimenzija fotografije.

 Kako bi ocenili da li je novo stanje bolje od prethodnog implementirana je funkcija *calculateDifference*. 
Funkcija *calculateDifference* računa razliku između ciljnje fotografije i trenutnog stanja fotografije kreirane algoritmom. Razlika između fotorafija predstavlja sumu razlika vrednosti piksela na istim koordinatama obe fotografije. Što je suma manja razlika između fotografija je manja, odnosno fotografija kreirana algoritmom je sve bliža ciljnoj fotografiji.

U fajlu *main.py* se nalazi kod potreban za učitavanje određene fotografije sa diska, koja za algoritam predstavlja ciljnju fotografiju. Zatim kod koji kreira početnu fotografiju, fotografiju sa belom pozadinom, koja je istih dimenzija kao i ciljna fotografija. U fajlu se takođe nalazi i kod algoritma simuliranog kaljenja.

## Funkcionisanje algoritma:
* Na početku programa učitava se fotografija. Ova fotografija predstavlja ciljnju fotografiju, odnosno fotografiju koju algoritam treba da rekreira. Kreira se fotografija sa belom pozadinom koja predstavlja početno stanje algoritma. 

* Zatim se generiše nasumično rešenje. Nasumično rešenje se generiše dodavanjem novog trougla na fotografiju koja predstavlja trenutno stanje.

* Računa se cena starog i novog rešenja

* Prihvatanje ili odbacivanje novog rešenja na osnovu izlaza funkcije verovatnoće


* Zatim se postavlja trenutno najbolje rešenje, u zavisnosti da li je novo rešenje bolje ili ne

* Ukoliko je zadovoljavajuće rešenje nađeno tada se algoritam prekida

* Ukoliko zadovoljavajuće rešenje nije nađeno, samnjuje se temperatura i nastavlja se sa koracima algoritma.