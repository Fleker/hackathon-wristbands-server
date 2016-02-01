 /* 
 MADE BY NICK FELKER
 
 TO EASILY EDIT / UPDATE THE FAQ, JUST MODIFY THE 
 JSON OBJECT HERE
 
 *****
 Each item is an object placed in a JSON array
 {
    question: The question
    answer: The answer
 }
 *****
 */

faq = [{
    question: "Who can attend?",
    answer: "Any high school, undergraduate and graduate students are welcomed to attend."
}, {
    question: "How will you decide between applicants?",
    answer: "Applications will be reviewed by committee and selected participants will and be notified via email.  Rowan students are guaranteed acceptance to this event, but will still need to apply."
}, {
    question: "How much is this going to cost me?",
    answer: "ProfHacks is completely free! Food, drinks, escape room and awesome swag are completely free of charge!"
}, {
    question: "How do I get there?",
    answer: "<ul><li>From Philly:<ul><li><a href='https://www.google.com/maps/dir/Philadelphia,+PA/Glassboro,+NJ/@39.8269572,-75.2712937,11z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x89c6b7d8d4b54beb:0x89f514d88c3e58c1!2m2!1d-75.1652215!2d39.9525839!1m5!1m1!1s0x89c6d7abad845dc5:0x5b768944f5f70002!2m2!1d-75.1118422!2d39.7028923!3e0'>You can drive to Glassboro by taking NJ 42 to NJ 55 to US 322 at exit 50B.</a></li><li><a href='https://www.google.com/maps/dir/Philadelphia,+PA/Glassboro,+NJ/@39.830215,-75.2794204,11z/am=t/data=!4m14!4m13!1m5!1m1!1s0x89c6b7d8d4b54beb:0x89f514d88c3e58c1!2m2!1d-75.1652215!2d39.9525839!1m5!1m1!1s0x89c6d7abad845dc5:0x5b768944f5f70002!2m2!1d-75.1118422!2d39.7028923!3e3'>You can take NJTransit bus.</a></li></ul></li><li>Outside Philly:<ul><li><a href='https://www.google.com/maps/dir/Philadelphia,+PA/Glassboro,+NJ/@39.8269572,-75.2712937,11z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x89c6b7d8d4b54beb:0x89f514d88c3e58c1!2m2!1d-75.1652215!2d39.9525839!1m5!1m1!1s0x89c6d7abad845dc5:0x5b768944f5f70002!2m2!1d-75.1118422!2d39.7028923!3e0'>Consider using US Megabus.</a></li><li><a href='https://www.google.com/maps/dir/Philadelphia,+PA/Glassboro,+NJ/@39.830215,-75.2794204,11z/am=t/data=!4m14!4m13!1m5!1m1!1s0x89c6b7d8d4b54beb:0x89f514d88c3e58c1!2m2!1d-75.1652215!2d39.9525839!1m5!1m1!1s0x89c6d7abad845dc5:0x5b768944f5f70002!2m2!1d-75.1118422!2d39.7028923!3e3'>You may also want to use Amtrak.</a></li></ul></li></ul>"
}, {
    question: "Where should I park?",
    answer: "You can park in Parking Lot D, right next to the engineering building."
}, {
    question: "What about team sizes?",
    answer: "The maximum number of people a team can have is four. Though encouraged, having a team beforehand is not necessary. If you want to form a team at ProfHacks, there will be a fun mixer beforehand to help you meet potential team members."
}, {
    question: "What should I bring?",
    answer: "You should bring some form of identification (driver’s license, school ID card, etc.), laptops, phones, chargers and sleeping gear. You will also need to sign a liability waiver and photo release form to gain admittance."
}, {
    question: "What Shouldn’t I Bring?",
    answer: "Tools such as power drills, Dremel drills and the like are prohibited. Articles such as weapons and alcohol are also prohibited. Any competitor found to be in possession of these articles will be disqualified from the competition."
}, {
    question: "I have a question that's not answered here; what should I do?",
    answer: 'We’re here for you! Send us an email at <a href="mailto:team@profhacks.com">team@profhacks.com</a> or feel free to reach out to us on <a href="http://twitter.com/profhackathon">Twitter</a>.'
}];

function postFAQs() {
    var out = "<div><h1>FAQ</h1>";
    for(i=0;i<faq.length;i++) {
        var f = faq[i];
        out += "<h2>"+f.question+"</h2>";
        out += "<p>"+f.answer+"</p>";
    }
    out += "</div>";
    document.getElementById('faq').innerHTML = out;
}