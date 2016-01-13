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
    answer: "All undergraduate, graduate, and high school students from any school are welcome. If you are under 18, we’ll need a parental consent form."
}, {
    question: "How will you decide between applicants?",
    answer: "Participants will be chosen randomly by a lottery. Everyone is welcome to apply. Rowan students are guaranteed admittance (but you still need to register!)"
}, {
    question: "Why, then, do you need my resume?",
    answer: "Uploading your resume is optional. If you are admitted, it will be passed on to sponsors. They are not linked to the application process, which is random."
}, {
    question: "How much is this going to cost me?",
    answer: "ProfHacks is entirely free: the food, drinks, escape room, and epic swag are free of charge!."
}, {
    question: "How do I get there?",
    answer: "You could try <a href='http://uber.com'>Uber</a>"
}, {
    question: "What about team sizes?",
    answer: "Teams can have up to four people. Having a team before arriving is not necessary. You'll be able to have a fun team-forming event before hacking begins."
}, {
    question: "What should I bring?",
    answer: "You should bring your student id, laptop, phone, chargers, and stuff for sleeping.<br>If you are under 18, a parental consent form should be brought too.<br>Do NOT bring weapons. Don't be that person."}, {
    question: "I have a question that's not answered here; what should I do?",
    answer: 'We’re here for you! Send us an email at <a href="mailto:team@profhacks.com">team@profhacks.com</a> or feel free to reach out to us on <a href="http://twitter.com/profhackathon">Twitter</a>'
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