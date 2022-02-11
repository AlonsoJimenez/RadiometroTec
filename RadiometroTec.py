import csv
import csv
from serial import Serial

csvMemory = []

nameFile = ""
com = ''
def creaArchivo():
    global nameFile
    nameFile = input("Digite el nombre del archivo csv a crear: ")
    crearCom()

def crearCom():
    global com
    com = input("Digite la entrada COM en la que se introducirá el radiometro (1-10):")
    
    com = int(com)
    startStop()
    
    

def startStop():
    global csvMemory
    global com
    arduino = Serial('COM'+ str(com), 9600)
    try:
        print("Presione ctrl + c para detener el programa y guardar la información")
        while(True):
            line1 = arduino.readline()
            line1 = (line1.decode('UTF-8'))
            line2 = arduino.readline()
            line2 = (line2.decode('UTF-8'))
            csvMemory += [[str(line1), str(line2)]]
    except KeyboardInterrupt:
        arduino.close()
        csvWriting()    

    except:
        print("Error de entrada COM")




def csvWriting():
    global nameFile
    csvFile = open(nameFile, 'w', encoding = 'UTF8', newline = '') 
    writer = csv.writer(csvFile)
    writer.writerow(['Longitud de onda (nm)', 'Intensidad (W/cm^2)'])
    for line in csvMemory:
        writer.writerow(line)
    csvFile.close()

creaArchivo()