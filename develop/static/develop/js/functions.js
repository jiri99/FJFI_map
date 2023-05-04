/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

// $(document).ready(function() {

// 	var pressed = false;

// 	var pojmy = new Array();

// 	$(".area").each(function(i, obj) {
// 		pojmy[i] = $(this).attr("nazev");

// 		if ((pojmy[i] !== pojmy[i-1]) && ($(this).attr("no-display") !== "true")){
// 			$("#seznam-pojmu").append($(this).attr("nazev") +"<br />");
// 		}

// 		//console.log("vypisuji pojem cislo: "+i+" s nazvem "+$(this).attr("nazev"));
// 	});

// 	$('.area').click(
// 		function() {			
// 			$("#nazev").text($(this).attr("nazev"));	
// 		});

// 	$(".area").on("click", function(e){
// 		e.preventDefault();
// 		window.location = $(this).attr("href");
// 		console.log($(this).attr("href"));   			
// 	});
	
// 	$('img[usemap]').rwdImageMaps();


// 	$('img').maphilight({groupBy : 'nazev'});

// 	console.log('Maphilight!');

// });



function home() {window.location.assign("homepage.html");}

function back() {
	address = window.location.href;

	console.log(address);
	console.log(address.charAt(address.length - 1));

	if(address.charAt(address.length - 1) === "#" ) {
		this.history.go(-2);
		console.log("-- Zpět o dvě stránky --");
	} else {
		this.history.back();
		console.log("-- Zpět o jednu stránku --");
	}
}
