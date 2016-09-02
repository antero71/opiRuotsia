def readFile(tiedostonNimi):
    file = open(tiedostonNimi,"r")
    lines = file.readlines()
    file.close()
    return lines
