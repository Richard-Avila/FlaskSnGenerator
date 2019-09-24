import datetime
import re
import time
class SerialNumberGenerator(object):

    #initiate our class variable lastUsed which will represent the last serial number to be generated
    def __init__(self):
        self.lastUsed = 0
        self.lastUsed = self.getLastUsedSerialNumber()

    #this method will generate a single serial number
    def generateSerialNumber(self):
        # This sleep will prevent the client recieving two of the same serial number
        time.sleep(.01)
        # We are using time to generate the serial number because time does not repeat
        possibleSN = str(datetime.datetime.now())
        # This regular expression assists us remove some unwanted formatting from the datetime call
        possibleSN = re.sub('[-:.]', '', possibleSN)
        # Take out the white space
        possibleSN = possibleSN.replace(" ", "")
        # we then cut of some of the tail end and the first two digits in the four digit year.
        # *quick note* because we now have a two digit year, a serial number will not repeat for 100 years
        possibleSN = possibleSN[:16]
        return possibleSN[2:]
        
    # This method's purpose is provide an extra check whether a generated serial number is an original and has no chance of being a duplicate
    def getNewSerialNumber(self):
        # generate a serial number
        currentSerialNumber = self.generateSerialNumber()
        # enter a while loop that verifies that the serial number that is about to be issued is newer than the last used serial number
        while(int(currentSerialNumber) <= int(self.lastUsed)):
            # if it is not newer then we generate another serial number
            currentSerialNumber = self.generateSerialNumber()
        # Update the last used serial number
        self.lastUsed = currentSerialNumber
        self.updateLastUsedSerialNumber(currentSerialNumber)
        # We can now return the serial number
        return currentSerialNumber

    # This method will return as many serial numbers as the client passed in as a parameter (desiredCount)
    def getNewSerialNumberRange(self, desiredCount):
        # Initialize a list
        serialNumberList = []
        # This for loop iterates (desiredCount) times
        for x in range(int(desiredCount)):
            # We initialize a serialNumber and assign it the value of the return of our getNewSerialNumber method
            serialNumber = self.getNewSerialNumber()
            # Add the serial number to the list
            serialNumberList.append(serialNumber)
        # And finally we return the requested range of serial numbers
        return serialNumberList

    # This method updates the text file with the last used serial number
    def updateLastUsedSerialNumber(self, serialNumber):
        file = open('LastUsedSN.txt', 'w')
        file.write(str(serialNumber))
        file.close()
        
    # This method reads the text file and retrieves the last used serial number
    def getLastUsedSerialNumber(self):
        file = open('LastUsedSN.txt', 'r')
        serialNumber = file.readline()
        return serialNumber