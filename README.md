# Projektarbete - Python: Konfigurering & Validering av VLAN
Verktyg för automatisera generering av VLAN-konfigurationer från CSV-filer samt validering av sparade konfigurationer mot specifika regler.

## Projektstruktur
Projektet ska bestå av fyra `-py`-filer: en `main`-fil, och tre 'moduler' som innehåller funtkioner som `main` kan importera.

Vid deadline ska repot innehålla följande:

* **vlan_parse.py**: Öppnar och läser `.csv`-filen, tar sedan raderna ur `csv`-filens tabeller och omvandlar dem till ett strukturerat format som dem andra modulerna enkelt kan förstå.

* **vlan_generate.py**: Tar den strukturerade datan från **vlan_parse** och skapar själva kommandona för switchen/routerns konfigureringsterminal som den sedan skriver ut som en textsträng eller sparar i `.txt`-fil.

* **vlan_validate.py**: Läser en sparad konfigurationsfil och kontrollerar den mot tre regler.

* **main.py**: Hämtar funktionerna från ovanstående filer och sammanfogar alla funktioner i en applikation. När projektet är färdigt så är det endast den här filen som körs.

## Gruppmedlemmar & Rollfördelning
* **Alexander Ågren** - <roll>
* **Emil Estborn** - <roll>
* **Raghed Kordi** - <roll>
* **Sara Ahmed** - <roll>
* **Ali Heleil** - <roll>

## Funktioner - Två faser
1. **Generera konfiguration** (**vlan_parse**, **vlan_generate**): Den läser in en `.csv`-fil innehållande VLAN-information och genererar automatiskt en färdig konfigurationsfil för VLAN.

2. **Validera konfiguration** (**vlan_validate**): Kontrollerar en sparad konfigurationsfil mot tre regler: 
* **Regel 1:**
* **Regel 2:**
* **Regel 3:**

## Arbetsflöde i Git
Vi arbetar i egna branches, vi pushar till dessa branches och skapar pull requests.

***PUSHA INTE TILL MAIN***

1. Clona repot till din dator och hämta den senaste koden: `git checkout main` följt av `git pull`
2. Skapa din egen branch: `git checkout -b modul-[modulnamn]`
3. Spara dina ändringar lokalt: `git add` och `git commit -m "Beskriv vad du har gjort/ändrat och varför"`
4. Pusha till GitHub:
* Första gången, när branchen just har skapats: `git push -u origin [namnet på er branch]`
* Efter första gången: `git push`
5. Skapa en pull request så granskar vi den som grupp. Om allting fungerar som det ska så mergas den med `main`. 