def Gruppenerstellung(Teilnehmerliste, maxSpieler):
    anzahlTeilnehmer = len(Teilnehmerliste)
    gruppenaufteilung = Gruppenaufteilung(anzahlTeilnehmer=anzahlTeilnehmer, maxSpieler=maxSpieler)
    return Gruppenzuweisung(Gruppenaufteilung=gruppenaufteilung, Teilnehmerliste=Teilnehmerliste)


def Gruppenaufteilung(anzahlTeilnehmer,maxSpieler):
    #Teilnehmer / maxspieler als int
    #Ausgabe Teilnehmergruppe im Format: [3,2,2]
    Teilnehmergruppe=[];
     
    if isinstance(anzahlTeilnehmer, str) or anzahlTeilnehmer <= 0:
        return "Keine erlaubte Eingabe!";
    elif anzahlTeilnehmer <= maxSpieler:
        Teilnehmergruppe.append(anzahlTeilnehmer);
    elif anzahlTeilnehmer // maxSpieler == 1:
        if anzahlTeilnehmer % 2 == 0:
            Teilnehmergruppe.append(anzahlTeilnehmer//2);
            Teilnehmergruppe.append(anzahlTeilnehmer//2);
        else:
            Teilnehmergruppe.append(anzahlTeilnehmer//2);
            Teilnehmergruppe.append(anzahlTeilnehmer//2+1);
    elif anzahlTeilnehmer % maxSpieler == 0:
        AnzahlGruppen = anzahlTeilnehmer//maxSpieler;
        MindestanzahlinGruppe = anzahlTeilnehmer//AnzahlGruppen;
        for i in range(AnzahlGruppen):
            Teilnehmergruppe.append(MindestanzahlinGruppe);
    else:
        AnzahlGruppen = anzahlTeilnehmer//maxSpieler + 1;
        MindestanzahlinGruppe = anzahlTeilnehmer//AnzahlGruppen;
        AnzahlGruppenUeberschuss = anzahlTeilnehmer % AnzahlGruppen;
        for i in range(AnzahlGruppenUeberschuss):
            Teilnehmergruppe.append(MindestanzahlinGruppe+1)
        for i in range(AnzahlGruppen-AnzahlGruppenUeberschuss):
            Teilnehmergruppe.append(MindestanzahlinGruppe);
    return Teilnehmergruppe;
 
def Gruppenzuweisung(Gruppenaufteilung, Teilnehmerliste):
    #Gruppenaufteilung im Format: [3, 2, 2]
    #Teilnehmerliste im Format: ["Name1", "Name2", "Name3"]
    #Gruppenliste Ausgabe im Format: [["Name1", "Name2"], ["Name3", "Name4"]] 
    Gruppenliste=[];
    zaehler=0;
    for i in range(len(Gruppenaufteilung)):
        Gruppenliste.append([]);
        for j in range(Gruppenaufteilung[i]):
            Gruppenliste[i].insert(j, Teilnehmerliste[zaehler]);
            zaehler+=1;
    return Gruppenliste;


#Teilnehmer=18;
#maxSpieler=4;
#Teilnehmerliste=["Markus", "Tobi", "Stefan", "Lukas", "Robert", "Thomas", "Alex", "Jo"];
#Gruppen = Gruppenaufteilung(len(Teilnehmerliste), maxSpieler);
# 
#if not isinstance(Gruppen, str):
#    Gruppenliste = Gruppenzuweisung(Gruppen, Teilnehmerliste);