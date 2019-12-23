from browser import document, html

class Application:
    def __init__(self):
        self.contents = document["pydiv"]
        turmas="NidMG1 Nid1MG1 NidTG1 Nid1TG1"\
        "Agr21MG1 Agr21MG2 Agr22MG1 Agr22MG2"\
        "Agr21TG1 Agr21TG2 Agr22TG1 Agr22TG2 Agr23TG1 Agr23TG2"\
        "Agr3MG1 Agr3MG2 Agr3TG1 Agr3TG2 Agr3TG3 Agr4MG1 Agr4MG2 Agr4TG1 Agr4TG2"\
        "Agr5MG1 Agr5MG2 Agr5MG3 Agr6MG1 Agr6MG2 Agr6MG3"
        professores= """Claudia2 Priscila Cibele Lukas Alguém Dominyke 
        Leandro Claudinha Rafael Dudu Daniel Eduardo Sabrina Karla Rebeca Fabiana
        Kelly Cristiane Giselle Rosane Ana Roxo Sol Gustavo Larissa Paulo Adriana Léo"""
        