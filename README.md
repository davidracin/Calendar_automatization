# Automatizace Kalendáře
Zvolil jsem si programovací jazyk Python. Projekt obsahuje soubory pro vytvoření a smazání událostí v google kalendáři.
## Popisek
Využívám Google Calendar API pro vytvoření API klíče. Pro vytvoření projektu a povolení API používám Google Cloud Console.

Soubor [main.py](https://github.com/davidracin/Calendar_automatization/blob/master/main.py) vytvoří událost v google kalendáři. První krok při spuštění je authorizace google účtu a uložení informací pro další přihlašovaní bez autorizace. Poté se zeptá na název události, popisek, datum zahájení, ukončení, čas zahájení, ukončení, kdy se má událost opakovat, kolikrát se má opakovat. Potom vygeneruje ID události.

Soubor [delete_event.py](https://github.com/davidracin/Calendar_automatization/blob/master/delete_event.py) Při spuštění se zeptá na ID události a smaže událost podle toho jaké ID jste zadali.
## Úprava kódu
Požadavky pro úpravu a svůj projekt [Požadky](https://github.com/davidracin/Calendar_automatization/blob/master/requirments.txt).
