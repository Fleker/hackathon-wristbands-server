/*
CREATED BY NICK FELKER

THIS SCRIPT WAS DEVELOPED TO MAKE IT EASY TO ADD / UPDATE
SPONSORS AND THEIR TIERS

*****
Each sponsor is an object placed in a JSON array which is placed in one of the tiers.

All of the HTML is generated automatically
tier > {
    height: max height of each logo
    sponsors: a JSON array of sponsors
}
sponsors > {
    logo: The image url for the sponsor's logo
    name: The name of the sponsor, for the image alt
    url: The website for the sponsor,
    height: A number for the logo's height, optional,
    apis: An optional array of urls that point to developer portals for a given sponsor
}
*****
*/
sponsors = {
    oak: {height: 160,
        sponsors: [{
        logo: "/static/img/sponsor-logos/rowan_ieee.png",
        name: "Rowan IEEE",
        url: "https://rowan.collegiatelink.net/organization/IEEE"
    }]},
    sapling: {height: 120,
        sponsors: []},
    seedling: {
        height: 80,
        sponsors: [{
	logo: "/static/img/sponsor-logos/plux.png",
	name: "PLUX",
	url: "http://www.plux.info"
	},{
	logo: "/static/img/sponsor-logos/bitalino.png",
	name: "BITalino",
	url: "http://www.bitalino.com"]}
}
partners = [{
       
}]

function postSponsors() {
    var out = "<h1>Thanks!</h1><p>We thank all companies and organizations that helped make this hackathon possible!</p>";
    for(i in sponsors) {
        out += "<h2 class='"+i+"'>"+i.substring(0,1).toUpperCase()+i.substring(1)+" Sponsors</h2>";
        out += "<div class='sponsor-row "+i+"'>";
        var s = sponsors[i];
        for(index=0; index<s.sponsors.length; index++) {
            sponsor = s.sponsors[index];
            var sponsor_height = ((s.height!==undefined)?"style='max-height:"+(sponsor.height || s.height)+"px'":"");
            
            out += '<a href="'+sponsor.url+'" target="_blank"><img src="'+sponsor.logo+'" alt="'+sponsor.name+'" '+sponsor_height+'></a>';
        }
        out += "</div>";
    }
    out += '<p class="center">Interested in sponsoring? <a href="/static/documents/sponsorship-doc.pdf">Learn more.</a></p>';
    document.getElementById('sponsors').innerHTML = out;
    
    postPartners();
}

function postPartners() {
    
}
