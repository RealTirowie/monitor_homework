#!/usr/bin/env python
# -*- coding: utf-8 -*-


# variables
login_link = "https://moodle.spengergasse.at/login/index.php"

links_dict = {
    "Datenbanken und Informationssysteme": "https://moodle.spengergasse.at/course/view.php?id=2540",
    "Betriebswirtschaft und Management": "https://moodle.spengergasse.at/course/view.php?id=1740",
    "Programmieren und Software Engineering": "https://moodle.spengergasse.at/course/view.php?id=1614",
    "Betriebswirtschaft u Management": "https://moodle.spengergasse.at/course/view.php?id=1341", 
    "Computerarchitektur und Betriebssysteme": "https://moodle.spengergasse.at/course/view.php?id=1206"
    }

#key_elements = list(links_dict.keys())

user = "<fill in>"
pwl = "<fill in>"
aufgaben = "assign"

# Mail variables
sender = "<fill in>"
pw = "<fill in>"
receiver = "<fill in>"

# create text object for mail
mail_subject = "moodle Aufgabencheck"
mail_text = "Folgendes Ergebnis:\n\n"



