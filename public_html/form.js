/*
File Name: form.js
*/

            
function validName () {
    //check if user has answered the questions with the asterisk
    
       if (document.make_form.eventName.value != "") {
          document.make_form.eventName.style.border = "2px solid #00EE00";
          document.make_form.eventName.style.backgroundColor = "white";
          document.getElementById("name_asterisk").style.visibility= "hidden";
          return true;
        } else {
          document.make_form.eventName.style.border = "2px solid red";
          document.make_form.eventName.style.backgroundColor = "#FFCCCC";
          document.getElementById("name_asterisk").style.visibility= "visible";
          alert("please provide the name of the event");
          return false;
          }
    }
    
function validOrg() {
        
        if (document.make_form.eventOrg.value != "") {
          document.make_form.eventOrg.style.border = "2px solid #00EE00";
          document.make_form.eventOrg.style.backgroundColor = "white";
          document.getElementById("org_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.eventOrg.style.border = "2px solid red";
           document.make_form.eventOrg.style.backgroundColor = "#FFCCCC";
           document.getElementById("org_asterisk").style.visibility="visible";
           alert("please provide the name of the organization")
           return false;
         }
    }

function validDate() {
        
        if (document.make_form.date.value != "") {
          document.make_form.date.style.border = "2px solid #00EE00";
          document.make_form.date.style.backgroundColor = "white";
          document.getElementById("date_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.date.style.border = "2px solid red";
           document.make_form.date.style.backgroundColor = "#FFCCCC";
           document.getElementById("date_asterisk").style.visibility="visible";
           alert("please provide the date of the event")
           return false;
         }
    }

function validBtime() {
        
        if (document.make_form.startTime.value != "") {
          document.make_form.startTime.style.border = "2px solid #00EE00";
          document.make_form.startTime.style.backgroundColor = "white";
          document.getElementById("btime_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.startTime.style.border = "2px solid red";
           document.make_form.startTime.style.backgroundColor = "#FFCCCC";
           document.getElementById("btime_asterisk").style.visibility="visible";
           alert("please provide the beginning time")
           return false;
         }
    }

function validEtime() {
        
        if (document.make_form.endTime.value != "") {
          document.make_form.endTime.style.border = "2px solid #00EE00";
          document.getElementById("etime_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.endTime.style.border = "2px solid red";
           document.make_form.endTime.style.backgroundColor = "#FFCCCC";
           document.getElementById("etime_asterisk").style.visibility="visible";
           alert("please provide the ending time")
           return false;
         }
    }

function validPlace() {
        
        if (document.make_form.loc.value != "") {
          document.make_form.loc.style.border = "2px solid #00EE00";
          document.make_form.loc.style.backgroundColor = "white";
          document.getElementById("place_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.loc.style.border = "2px solid red";
           document.make_form.loc.style.backgroundColor = "#FFCCCC";
           document.getElementById("place_asterisk").style.visibility="visible";
           alert("please provide the location")
           return false;
         }
    }

function validDesc() {
        
        if (document.make_form.eventDes.value != "") {
          document.make_form.eventDes.style.border = "2px solid #00EE00";
          document.make_form.eventDes.style.backgroundColor = "white";
          document.getElementById("desc_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.eventDes.style.border = "2px solid red";
           document.make_form.eventDes.style.backgroundColor = "#FFCCCC";
           document.getElementById("desc_asterisk").style.visibility="visible";
           alert("please provide the description")
           return false;
         }
    }

function validContact() {
        
        if (document.make_form.contactInfo.value != "") {
          document.make_form.contactInfo.style.border = "2px solid #00EE00";
          document.make_form.contactInfo.style.backgroundColor = "white";
          document.getElementById("contact_asterisk").style.visibility="hidden";
          return true;
         } else {
           document.make_form.contactInfo.style.border = "2px solid red";
           document.make_form.contactInfo.style.backgroundColor = "#FFCCCC";
           document.getElementById("contact_asterisk").style.visibility="visible";
           alert("please provide the contact")
           return false;
         }
    }

function validateForm () {
    return validName () && validOrg() && validDate() && validBtime() && validEtime() && validPlace() && validDesc() && validContact();
    }
    



function resetForm() {
      document.getElementById("name_asterisk").style.visibility="visible";
      document.getElementById("org_asterisk").style.visibility="visible";
      document.getElementById("date_asterisk").style.visibility="visible";
      document.getElementById("btime_asterisk").style.visibility="visible";
      document.getElementById("etime_asterisk").style.visibility="visible";
      document.getElementById("place_asterisk").style.visibility="visible";
      document.getElementById("desc_asterisk").style.visibility="visible";
      document.getElementById("contact_asterisk").style.visibility="visible";
      document.make_form.eventName.style.backgroundColor = "white";
      document.make_form.eventOrg.style.backgroundColor = "white";
      document.make_form.date.style.backgroundColor = "white";
      document.make_form.startTime.style.backgroundColor = "white";
      document.make_form.endTime.style.backgroundColor = "white";
      document.make_form.loc.style.backgroundColor = "white";
      document.make_form.eventDes.style.backgroundColor = "white";
      document.make_form.contactInfo.style.backgroundColor = "white";

      document.make_form.eventName.style.border = "black";
      document.make_form.eventOrg.style.border = "black";
      document.make_form.date.style.border = "black";
      document.make_form.startTime.style.border = "black";
      document.make_form.endTime.style.border = "black";
      document.make_form.loc.style.border = "black";
      document.make_form.eventDes.style.border = "black";
      document.make_form.contactInfo.style.border = "black";
      
          }
        
