#!/usr/bin/env python
# -*- coding: utf-8 -*-


class VergleichAufgaben:

    def compare_it(self, key_name, resultP):
        # Program to read the entire file (absolute path) using read() function
        try:
            with open(f"aufgaben_links/{key_name}.txt", "r") as file:
                content = file.read()
                resultF = content.split(",")
                print(resultF)
                file.close()
        except:
            resultF = ""
        # compare last list with new items on page
        new = set(resultP) - set(resultF)
        # return new element link
        return new

    def write_new_list(self, key_name, resultP):
        result_prep = []
        x=1
        while x <= len(resultP):
            result_prep.append(resultP[x-1]+",")
            x=x+1
        lastel = result_prep[len(result_prep)-1][ : -1]
        result_prep.pop()
        result_prep.append(lastel)
        # Program to write multiple lines to text file using writelines() function
        with open(f"aufgaben_links/{key_name}.txt", "w") as file:
            file.writelines(result_prep)
            file.close()
        return True


def main():
    # create name and list opbject
    key_name = "Datenbanken und Informationssysteme"
    resultP = ['https://moodle.spengergasse.at/mod/assign/view.php?id=111318', 'https://moodle.spengergasse.at/mod/assign/view.php?id=114535', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95583', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95585', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95586', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95591', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95592', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95593', 'https://moodle.spengergasse.at/mod/assign/view.php?id=95596', 'https://moodle.spengergasse.at/mod/assign/view.php?id=96918', 'https://moodle.spengergasse.at/mod/assign/view.php?id=97775', 'https://moodle.spengergasse.at/mod/assign/view.php?id=101028', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98170', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98173', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98174', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98177', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98178', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98181', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98182', 'https://moodle.spengergasse.at/mod/assign/view.php?id=98196', 'https://moodle.spengergasse.at/mod/assign/view.php?id=106392', 'https://moodle.spengergasse.at/mod/assign/view.php?id=106391', 'https://moodle.spengergasse.at/mod/assign/view.php?id=106393', 'https://moodle.spengergasse.at/mod/assign/view.php?id=106394', 'https://moodle.spengergasse.at/mod/assign/view.php?id=106395', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105297', 'https://moodle.spengergasse.at/mod/assign/view.php?id=107410', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105303', 'https://moodle.spengergasse.at/mod/assign/view.php?id=107408', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105299', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105304', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105306', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105307', 'https://moodle.spengergasse.at/mod/assign/view.php?id=115272', 'https://moodle.spengergasse.at/mod/assign/view.php?id=105310', 'https://moodle.spengergasse.at/mod/assign/view.php?id=111865', 'https://moodle.spengergasse.at/mod/assign/view.php?id=116093', 'https://moodle.spengergasse.at/mod/assign/view.php?id=116365', 'https://moodle.spengergasse.at/mod/assign/view.php?id=116623', 'https://moodle.spengergasse.at/mod/assign/view.php?id=111318', 'https://moodle.spengergasse.at/mod/assign/view.php?id=114535']
    # run program
    vg = VergleichAufgaben()
    compare_items = vg.compare_it(key_name, resultP)
    # check if set is empty or invert to check if it is with content
    if len(compare_items) == 0:
        print("no new element")

    print(compare_items)
    # update list with new results for next run
    write_items = vg.write_new_list(key_name, resultP)



if __name__=="__main__":
    main()





