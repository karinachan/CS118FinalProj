#!/usr/bin/env python2.7
# Python CGI script template 
# Import standard CGI modules
import cgi, os
import cgitb; cgitb.enable()
import datetime
from spamclass import *

# ------------------------------------------------------------------------------
# Top-level dispatch for web page request from this site

def makeListOptions(entry):
  result= ("<p> Event Name: " + entry.getName() + "</p>"
           + "<p> Event Organizer: " + entry.getEventOrg() + "</p>"
           + "<p> Date: " + entry.getDate() + "</p>"
           + "<p> Start Time: " + entry.getStartTime() + "</p>"
           + "<p> End Time: " + entry.getEndTime() + "</p>"
           + "<p> Place: " + entry.getPlace() + "</p>"
           + "<p> Event Description: " + entry.getDescript() + "</p>"
           + "<p> Contact Info: " + entry.getContact() + "</p>")
  return result

def respondToPageRequest():
  # Replace this stub by your text/HTML here

  inputs=cgi.FieldStorage()
  keys=inputs.keys()
  values= map(lambda key: {key: inputs.getvalue(key)},keys)
  
  contactinfo= inputs.getvalue('contactInfo')
  location=inputs.getvalue('loc')
  eventName=inputs.getvalue('eventName')
  eventDesc=inputs.getvalue('eventDes')
  startTime=inputs.getvalue('startTime')
  date=inputs.getvalue('date')
  eventOrg=inputs.getvalue('eventOrg')
  endTime=inputs.getvalue('endTime')

  
  #date= eventName.getdate()
  if "submit1" in inputs:
    eventName=Spam(eventName, eventOrg, date, startTime,endTime,location, eventDesc,contactinfo)
  else:
    pass
  events=""
  for filename in os.listdir("/students/spamalot/public_html/cgi-bin/finalproj/spam/"):
    events += makeListOptions(filename[:-4])

  
  
##  html = open("submit_event.html").read()
##  print(html.format(   ))  
##  html.close()
  html2= open("homepage.html").read()
  print(html2.format(eventlistings= events))

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
