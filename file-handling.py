from os import closerange


f = open("test.txt", "w")

f.write('''New File
    Hello Everyonw,




comming from file-handling.py
''')


f.close()
