import os

path="/students/spamalot/public_html/cgi-bin/finalproj/spam/"
listfilenames= os.listdir(path)


def readSpamthing(nameoffolder, textFile):
    text = open(path + nameoffolder +"/" + textFile, 'r').readlines()
    print text

        
def writeSpamthing(nameoffolder, textFile, dataString): #Lyn put two parameters (we think we know why)
    if os.path.exists(path + str(nameoffolder))==False:
        os.mkdir(path + str(nameoffolder))

    else:
        addE = open(path + nameoffolder + "/" + textFile + ".txt", "w")
        addE.write(dataString)
        addE.close()

#---------------------------------------
files = ["name.txt", "eventOrg.txt", "date.txt", "start.txt", "end.txt", "place.txt", "descript.txt", "contact.txt"]

class Spam():

    def __init__(self, eventName, eventOrg,  date, startTime, endTime, place, description, contactInfo):
        self.name = eventName
        self.org = eventOrg
        self.date=date
        self.start= startTime
        self.end= endTime
        self.place=place
        self.descript = description
        self.contact = contactInfo

        inputs = [self.name, self.org, self.date, self.start, self.end, self.place, self.descript, self.contact]

        map(lambda textFile,info: writeSpamthing(eventName,textFile,info),files, inputs)
    
    def getName(self):
        readSpamthing(self.name, "name.txt")

    def getEventOrg(self):
        readSpamthing(self.org, "eventOrg.txt")

    def getDate(self):
        readSpamthing(self.date, "date.txt")

    def getStartTime(self):
        readSpamthing(self.start, "start.txt")

    def getEndTime(self):
        readSpamthing(self.end, "end.txt")

    def getPlace(self):
        readSpamthing(self.place, "place.txt")

    def getDescript(self):
        readSpamthing(self.descript, "descript.txt")

    def getContact(self):
         readSpamthing(self.contact, "contact.txt")

