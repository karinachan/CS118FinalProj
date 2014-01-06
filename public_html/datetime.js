
function showDate()
{
	var now = new Date();
	
/*** CREATE AN ARRAY AND ASSIGN VALUES TO IT ***/

// create an Array object named "days," which holds values of different days
	var days = new Array('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');

// create an Array object called "months," which holds values of different months	
	var months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');
	var date = now.getDate();

	
	tnow=new Date();
	thour=now.getHours();
	tmin=now.getMinutes();
	tsec=now.getSeconds();	
	
	       
    if (tmin<=9) { tmin="0"+tmin; }   /*use a "0" in front of single digit minutes and seconds */
	if (tsec<=9) { tsec="0"+tsec; }
	
    var hour_display = thour;
	var ampm = "AM"; 
	
    if (thour == 0) {   /* midnight */
       hour_display = 12;
       } else if (thour == 12) {  /* noon */
       ampm = "PM"; 
       } else if (thour > 12) {
       hour_display = thour - 12;
       ampm = "PM"; 
       }

	if (hour_display<10) {
		hour_display="0"+hour_display;   /*use a "0" in front of single digit hour */
	   }
	   
	today = days[now.getDay()] + ", " + date + " " + months[now.getMonth()] + ", " 
	+ (now.getFullYear()) + "<br>" + hour_display + ":" + tmin +":"+ tsec + ampm;
	document.getElementById("dateDiv").innerHTML = today;
    
	   }

/*** SPECIFY INTERVALS OF CALLING A FUNCTION ***/

//calls showDate() function every 1000 millisecond, (which equals 1 second); 
// showDate() function updates every second;

setInterval("showDate()", 1000);  

