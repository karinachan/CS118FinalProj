#!/usr/bin/env python2.7
# Python CGI script template 
# Import standard CGI modules
# Created by Karina Chan, Evelyn Lee, and Nina Broocks (05/08/13)

import cgi, os
import cgitb; cgitb.enable()
import datetime
from newspamclass import *
import pickledb

serverImageDir = "/students/spamalot/public_html/cgi-bin/finalproj/spamimages/" # Name of server image directory
webImageDir = "http://cs.wellesley.edu/~spamalot/cgi-bin/finalproj/spamimages/" # Name of HTTP image directory

# ------------------------------------------------------------------------------
# Top-level dispatch for web page request from this site

def makeListOptions(entry):
  result= ("<div class='grid'><p> <span style='font-size: 28px; color: pink;'> " + entry.getName() + "</span></p>"
           + "<table border='0'><tr><td width='300px'><p> <strong><em>Event Organizer: </strong></em>" + entry.getEventOrg() + "</p>"
           + "<p> <strong><em>Date: </strong></em>" + entry.getDate() + "</p>"
           + "<p> <strong><em>Start Time: </strong></em>" + entry.getStartTime() + "</p>"
           + "<p> <strong><em>End Time: </strong></em>" + entry.getEndTime() + "</p>"
           + "<p> <strong><em>Place: </strong></em>" + entry.getPlace() + "</p>"
           + "<p> <strong><em>Event Description: </strong></em>" + entry.getDescript() + "</p>"
           + "<p> <strong><em>Contact Info: </strong></em>" + entry.getContact() + "</p></td>"
           + '<td><p> <a href="'+ entry.getImage() + '"> <img src="' + entry.getImage() + '" alt="SPAM"> </a></p></td></tr></table></div><br>"')
  return result

def respondToPageRequest():
  
  spamdb = pickledb.open('testSpamDB6', 'c')
  inputs=cgi.FieldStorage()
  keys=inputs.keys()

  request= inputs.getvalue('request','')
  
  if request == "submit":
    contactinfo= inputs.getvalue('contactInfo')
    location=inputs.getvalue('loc')
    eventName=inputs.getvalue('eventName')
    eventDesc=inputs.getvalue('eventDes')
    startTime=inputs.getvalue('startTime')
    date=inputs.getvalue('date')
    eventOrg=inputs.getvalue('eventOrg')
    endTime=inputs.getvalue('endTime')

    fileitem = inputs["uploadedFile"] # Specified file entity to upload
    remoteFilename = fileitem.filename # Name of file chosen by user on her computer
    if remoteFilename == '': # No file was specified for upload
        filename= webImageDir+ "spam.gif"
    else: # User specified file to upload
        nowtime = datetime.datetime.now() # The current time, used as timestamp name for file
        timestamp = nowtime.isoformat('-') # String for current time
                                           # use '-' to separate year/month/day and hour/minute/second
        # Split filename into base & extension (e.g., .png, .jpg, etc.)
        (remoteBase,remoteExtension) = os.path.splitext(remoteFilename) 
        remoteFile = fileitem.file
        size = fileSize(remoteFile)
        localFilename = serverImageDir + timestamp + remoteExtension # Full pathname to local image file
        with open(localFilename, 'wb') as localFile: # open local file for writing
            localFile.write(remoteFile.read()) # Copy remote file to local file 
        os.chmod(localFilename, 0644) # Ensure file is world readable
        # Warning: nothing checks that the uploaded file is actually an image file!
        # The above code allows uploading *any* file!
        filename= webImageDir+ timestamp+ remoteExtension
    event = Spam(eventName, eventOrg, date, startTime,endTime,location, eventDesc,contactinfo,filename)
    pickledb.storeValue(spamdb, eventName, event)   

  #del spamdb["EVELYN IS COOL"] #this can be used to take out whatever object is not working (due to None or something) Also can be used to delete an unwanted event.
  
  objects= pickledb.items(spamdb)
  sortedDateObjectTuple= sorted(map(lambda obj: (obj[1].getDate(),obj), objects))
  sortedObject= map(lambda (date,spam): spam, sortedDateObjectTuple) #this is still a tuple.    

  if request=="Search":
    keysearch= inputs.getvalue('keysearch')
    if keysearch!=None:
      sortedObject=filter(lambda obj: keysearch.lower() in (obj[1].getName()).lower(), sortedObject)
     
  listofevents=""
  
  for spamObject in sortedObject:
      listofevents += makeListOptions(spamObject[1])
     
  
  html= open("homepage.html", 'r').read()
  print(html.format(eventlistings= listofevents, imageDivsGoHere=generateImageDivs(serverImageDir,webImageDir)))
  pickledb.close(spamdb)

#-------Helper Functions---

# Generate HTML list of DIVs, one per image in images subdirectory
def generateImageDivs(linuxDir,webDir):
    imageNames = os.listdir(linuxDir)
    imageNames.sort() # sort image names alphabetically
    divStrings = map(lambda imageName: makeImageDiv(imageName, webDir), imageNames)
    allDivStrings = "\n".join(divStrings)
    return allDivStrings

# Make an HTML DIV for a single image (given its filename and web directory, i.e., http://cs.wellesley.edu/...)
def makeImageDiv(filename, webDir):
    return ('<div class="imageDiv">\n'
            + '  <img src="' + webDir + filename + '">\n'
            + '  <div class="imageFilename"><a href="' + webDir + filename + '">' + filename + '</a></div>\n'
            + '  <form method="post" action="imageUpload.cgi" name="deleteForm_' + filename + '">\n'
            + '    <input type="hidden" name="fileToDelete" value="' + filename + '">\n'
            + '    <input type="submit" name="request" value="Delete">\n'
            + '  </form>\n'
            + '</div>')

# Helper functions for determining file size
def fileSize (file):                                                                                                                    
    file.seek(0,2) # put file pointer at end of file                                                                                      
    size = file.tell()                                                                                                                    
    file.seek(0,0) # put file pointer at beginning of file                                                                                
    return size                                                                                                                           
                                                                                                                                        
def fileSizeInKB (size):                                                                                                                
    return (size*100 // 1024)/ float(100) 
# ------------------------------------------------------------------------------
# Standard template for debuggable web server
def main():
  print("Content-Type: text/html\n") # Print the HTML header
  try:
    # Invoke the page request handler to print the rest of the page
    respondToPageRequest()
  except:
    print("<hr><h1>A Python Error occurred!</h1>")
    cgi.print_exception()

# Start the whole shebang
main()
