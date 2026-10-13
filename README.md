# Projektarbete - Python: Konfigurering & Validering av VLAN
Verktyg för automatisera generering av VLAN-konfigurationer från CSV-fil, samt validering av sparade konfigurationer mot specifika regler.

## Projektstruktur
Projektet ska bestå av en `.csv`-fil och fyra `-py`-filer: en `main`-fil, och fyra 'moduler' som innehåller funtkioner som `main` kan importera, och en CSV-tabell som innehåller dem värden som funktionerna ska hantera.

Vid deadline ska repot innehålla följande:

* **vlan_parse.py**: Öppnar och läser `.csv`-filen, tar sedan raderna ur `csv`-filens tabeller och omvandlar dem till ett strukturerat format som dem andra modulerna enkelt kan förstå.

* **vlan_generate.py**: Tar den strukturerade datan från **vlan_parse** och skapar själva kommandona för switchens konfigurering och returnerar det som en lång textsträng.

* **router_generate.py**: Tar emot datan från `.csv`-filen från **vlan_parse** och skapar kommandon som konfigurerar sub-interfaces för varje VLAN (VLAN nummer, encapsulation) och returnerar det som en lång textsträng.

* **vlan_validate.py**: Läser en sparad konfigurationsfil och kontrollerar den mot tre regler.

* **main.py**: Hämtar funktionerna från ovanstående filer och sammanfogar alla funktioner i en applikation. SKriver en konfig-fil med texten från **dem tre översta modulerna** och granskar den med **vlan_validate**. När projektet är färdigt så körs endast **main**.

* **test.csv**: En CSV-tabell som innehåller all information som behövs för konfigurering.

## Gruppmedlemmar & Rollfördelning
* **Alexander Ågren** - ansvarig för Huvudprogrammet och integration av moduler till Main.
* **Raghed Kordi** - ansvarig för generering av VLAN-konfiguration. (`vlan_generate.py`)
* **Emil Estborn** - ansvarig för generering av sub-interface till router konfiguration. (`router_generate.py`)
* **Sara Ahmed** - ansvarig för CSV-läsare.(`vlan_parser.py`)
* **Ali Heleil** - ansvarig för validering av konfig-fil. (`vlan_validate.py`)

## Funktioner - Två faser
1. **Generera konfiguration** (**vlan_parse**, **vlan_generate**, **router_generate**): Den läser in en `.csv`-fil innehållande VLAN-information och genererar automatiskt en färdig konfigurationsfil för VLAN.

2. **Validera konfiguration** (**vlan_validate**): Kontrollerar en sparad konfigurationsfil mot tre regler: 
* **Regel 1:** VLAN 1 ska inte ha ett namn.
* **Regel 2:** Det ska inte finnas lösenord i konfig-filen.
* **Regel 3:** Namnen på alla VLAN ska bestå av max. 32 tecken.

Varje modul ska innehålla en funktion som blir anropad av `main`.

Modul: `vlan_parse.py` - Funktion: `read_csv_file`


Modul `vlan_generate.py` - Funktion: `generate_sw_config`

Modul: `router_generate.py` - Funktion: `generate_r_config`

Modul: `vlan_validate.py` - Funktion: `validate_config`

## Arbetsflöde i Git
Vi arbetar i egna branches, vi pushar till dessa branches och skapar pull requests.

***PUSHA INTE TILL MAIN***

1. Clona repot till din dator och hämta den senaste koden: `git checkout main` följt av `git pull`
2. Skapa din egen branch: `git checkout -b modul-[modulnamn]`
3. Spara dina ändringar lokalt: `git add` och `git commit -m "Beskriv vad du har gjort/ändrat och varför"`
4. Pusha till GitHub:
* Första gången, när branchen just har skapats: `git push -u origin [namnet på er branch]`
* Efter första gången: `git push`
5. Skapa en pull request så granskar vi den som grupp. Om allting fungerar som det ska, så mergas den med `main`.
6. Projektet är klart när alla pull requests är stängda/mergade.

***Om du inte kan använda Git:***
1. Gå till repot i GitHub.
2. Skapa en ny branch eller byt till den branch du arbetar inuti.
3. Lägg till filen i mappen `Projekt-GruppDelta`, eller redigera filen om den redan finns.
4. När du är klar, klicka på **"Commit changes..."**
5. Skriv ett meddelande om vad som har gjorts/ändrats.
6. **Se till att du sparar till din egen branch, inte till** `main`.
7. Klicka på **"Commit changes."**
8. Ladda om GitHub och öppna en pull request.