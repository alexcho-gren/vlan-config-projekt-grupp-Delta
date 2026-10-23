# VLAN- och Routerkonfigurationsverktyg

Detta är ett Python-baserat automatiseringsverktyg utvecklat som ett gruppprojekt. Programmet läser nätverksdata från en CSV-fil, genererar färdiga konfigurationsfiler för både Cisco IOS-switchar (Layer 2) och Cisco IOS-routrar (Layer 3), samt validerar de genererade filerna mot tre specifika säkerhets- och arkitekturregler.

## Projektstruktur
Projektet är uppdelat i en huvudfil och fyra fristående moduler:
* `main.py` – Programmets motor och orkestrator.
* `vlan_parse.py` – Läser och strukturerar CSV-data.
* `vlan_generate.py` – Genererar Cisco IOS Switch-konfiguration.
* `router_generate.py` – Genererar Cisco IOS Router-konfiguration (sub-interfaces).
* `vlan_validate.py` – Granskar konfigurationsfilerna mot regelverket.

---

## Installation

Programmet kräver inga externa bibliotek, det använder Pythons inbyggda standardbibliotek.

1. **Kloning av repo:**
   Ladda ner projektet till din dator via Git:
   ```bash
   git clone <länk-till-ert-repo>
   cd <projektmappens-namn>
   ```

2. **Förbered källfilen:**
   Säkerställ att det finns en fil med namnet `vlan_data.csv` i samma mapp som programkoderna (se exempel på struktur nedan).

3. **Körningskrav:**
   Du behöver ha **Python 3.5** eller nyare installerat på din dator.

---

## Hur man kör programmet

Programmet startas via terminalen.

1. Öppna terminalen och navigera till projektmappen.
2. Exekvera main-filen med följande kommando:
   ```bash
   python main.py
   ```
3. Programmet kommer att fråga efter sökvägen till din CSV-fil. Tryck på **Enter** för att använda standardfilen `vlan_data.csv`, eller skriv in sökvägen till en egen fil.

---

## Exempel på användning

### 1. Indata (`vlan_data.csv`)
En korrekt utformad indatafil ser ut så här:
```text
vlan_id,vlan_name,interface,ip_address,subnet
1,,GigabitEthernet0/0,192.168.1.1,255.255.255.0
10,Ekonomi,GigabitEthernet0/0,192.168.10.1,255.255.255.0
20,IT_Support,GigabitEthernet0/0,192.168.20.1,255.255.255.0
```

### 2. Körning i terminalen
När programmet startas möts användaren av följande flöde:
```text
=== Startar nätverkskonfigurering och validering ===
Ange sökväg till CSV-fil (Tryck Enter för standard 'vlan_data.csv'): 

[1/4] Läser data från vlan_data.csv...
[2/4] Genererar switch-konfiguration: switch_config.txt...
[3/4] Genererar router-konfiguration: router_config.txt...
[4/4] Validerar de genererade filerna mot reglerna...

=================== SLUTRESULTAT ===================
Status: Godkänd. Alla konfigurationer uppfyller kraven.
====================================================
```

### 3. Skapad utdata (`switch_config.txt` & `router_config.txt`)
Verktyget skapar nu två textfiler i mappen. 
`router_config.txt` innehåller då exempelvis:
```text
!
interface GigabitEthernet0/0
 no shutdown
!
interface GigabitEthernet0/0.1
 encapsulation dot1q 1
 ip address 192.168.1.1 255.255.255.0
!
interface GigabitEthernet0/0.10
 encapsulation dot1q 10
 ip address 192.168.10.1 255.255.255.0
!
```
*(Om en genererad fil skulle innehålla ett lösenord, ett VLAN-namn över 32 tecken eller om VLAN 1 namnges, kommer slutresultatet istället slå om till "Icke godkänd" och peka ut felet).*

---

## Användning av AI

I detta projekt har generativa AI-verktyg (så som ChatGPT och Mistral) varit tillåtna som **pedagogiska stöd**. 

**Vår policy och tillämpning:**
* AI har använts för att förklara nätverkssyntax (Cisco IOS-ordning) samt ge tips på isolerade Python-byggstenar (t.ex. hur `csv.DictReader` eller strängmetoder fungerar).
* Ingen färdig kod har genererats i sin helhet av AI utan att den ansvarige gruppmedlemmen har granskat och förstått logiken.

**Alexander:**

* Jag har huvudsakligen använt AI för att skapa projektets struktur, uppdelning av moduler, generering av pseudokod, samt konsultation/granskning om/av kod.

* När det kommer till själva kodningen har jag använt AI mest till att ställa frågor om **hur** kod ska implementeras, enklare sätt att skriva dem andra modulerna så jag kan bättre hjälpa dem andra i gruppen, samt hjälp med kommentering och dokumentation.

**Raghed:**

* Jag använde AI framför allt som stöd under utvecklingen för att förstå python och för att förbättra dokumentationen.

**Sara:**

* Jag har använt AI som ett hjälpmedel för att skriva och förstå koden. 

* Jag har också tagit hjälp av mina gruppkamrater till att få min del att fungera med resterande moduler, samt fått rådgivning om andra delar inom projektet.

**Emil:**

* Mistral har hjälpt mig får rätt på write-raderna, jag hade inte använt parenteser för att stänga in raden.

* Alexander (main.py) hjälpte mig använda variabler ur vlan_data istället för att behöva skriva ut värdena på varje f.write-rad samt sett till att raden med no shutdown bara skrivs en gång, med mera.

**Ali:**

* Jag använde ChatGPT för att förstå uppgiften och lära mig hur Python-kod med def, for, if, open(), strip(), len() och return fungerar. 

* Jag fick hjälp att skapa branchen modul-vlan-validate på GitHub, skriva den första versionen och rätta indragningar. Först returnerade modulen en lista med felmeddelanden. Efter diskussion i gruppen hjälpte en gruppkamrat till att uppdatera koden så att funktionen i stället returnerar True eller False och skriver ut felmeddelanden. 

* Jag lade in den uppdaterade koden i min branch och öppnade Pull Request #4 för granskning.
