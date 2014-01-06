#Created by Karina Chan, Evelyn Lee, and Nina Broocks (05/08/13)

import os

class Spam():

    def __init__(self, eventName, eventOrg,  date, startTime, endTime, place, description, contactInfo, imagename):
        self.name = eventName
        self.org = eventOrg
        self.date=date
        self.start= startTime
        self.end= endTime
        self.place=place
        self.descript = description
        self.contact = contactInfo
        self.image= imagename
   
    def getName(self):
        return self.name

    def getEventOrg(self):
        return self.org

    def getDate(self):
        return self.date

    def getStartTime(self):
        return self.start

    def getEndTime(self):
        return self.end

    def getPlace(self):
        return self.place

    def getDescript(self):
        return self.descript

    def getContact(self):
         return self.contact

    def getImage(self):
         return self.image
