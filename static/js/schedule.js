/*
CREATED BY NICK FELKER
THIS WILL MAKE IT EASY TO EDIT/UPDATE THE SCHEDULE AS WE 
CONTINUE TO GET CLOSER TO THE EVENT

*****
The schedule is in a JSON array containing JSON objects for each day.
{
   DAY > [ 
        {
            event: Name of the event on the schedule
            start_time: Start of the event
            end_time: End of the event, optional
            description: A longer description of said event
        }   
   ]
}
*****
*/

schedule = {
    saturday: [{         
        event: "Registation",
        start_time: "11:00a",
        end_time: "1:00p",
        description: "Check-in at Rowan Hall, mingle, and get swag. Snacks will be available."
    }, {
        event: "Introduction Ceremony",
        start_time: "1:00p",
        end_time: "2:00p",
        description: "Head to the auditorium. There will be overflow in the atrium."
    }, {
        event: "Begin Hacking",
        start_time: "2:00p",
        description: "Start building cool things. Check out our various technical sessions."
    }, {
        event: "Dinner",
        start_time: "8:00p",
        end_time: "9:00p",
        description: "Brought to you by Gourmet Dining"
    }], sunday: [{
        event: "Midnight Snack",
        start_time: "12:00a",
        end_time: "1:00a",
        description: "It's a free-for-all"
    }, {
        event: "Late-Night Snack",
        start_time: "4:00a",
        end_time: "5:00a",
        description: "Here's something small to get you through the night."
    }, {
        event: "Breakfast",
        start_time: "8:00a",
        end_time: "9:00a",
        description: "Brought to you by Gourmet Dining"
    }, {
        event: "Lunch",
        start_time: "12:00p",
        end_time: "1:00p",
        description: "Lunch is brought to you by Gourmet Dining"
    }, {
        event: "<b>Project Submissions Due!</b>",
        start_time: "2:00p",
        description: "Please make sure your submissions are done on time."
    }, {
        event: "Presentations",
        start_time: "2:30p",
        end_time: "3:30p",
        description: "Now's the time to present your project to everyone. Judges will be watching."
    }, {
        event: "Closing Ceremony",
        start_time: "4:00p",
        end_time: "5:00p",
        description: "Keynote, final demos, and winners announced. We will learn who wore it better."
    }, {
        event: "Clean-Up",
        start_time: "5:00p",
        description: "Clean up. Put everything back. Return hardware to the hardware lab. Say good-bye to your friends."
    }]
};

function postSchedule() {
    var out = "";
    for(i in schedule) {
        day = schedule[i];
        out += '<div class="day '+i+'">';
        out += '<h1>'+i+'</h1>';
        for(index=0;index<day.length;index++) {
            event = day[index];  
            out += '<h2>'+event.event+'<span>'+(event.start_time || "");
            if(event.end_time)
                out += '&ndash;'+event.end_time;
            out += "</span></h2>";
            out += "<p>"+event.description+"</p>";
        }
        out += "</div>";
    }
    
    document.getElementById('schedule').innerHTML = out;
} 