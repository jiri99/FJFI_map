/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function() {

	var pressed = false;

	var pojmy = new Array();

	$(".area").each(function(i, obj) {
		pojmy[i] = $(this).attr("nazev");

		if ((pojmy[i] !== pojmy[i-1]) && ($(this).attr("no-display") !== "true")){
			$("#seznam-pojmu").append($(this).attr("nazev") +"<br />");
		}

		//console.log("vypisuji pojem cislo: "+i+" s nazvem "+$(this).attr("nazev"));
	});

	$('.area').click(
		function() {			
			$("#nazev").text($(this).attr("nazev"));	
		});

	$(".area").on("click", function(e){
		e.preventDefault();
		window.location = $(this).attr("href");
		console.log($(this).attr("href"));   			
	});
	
	$('img[usemap]').rwdImageMaps();


	$('img').maphilight({groupBy : 'nazev'});

	console.log('Maphilight!');

});



function domu() {window.location.assign("index.html");}

function zpet() {
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


$(function() {
    $('.map').maphilight();
    $('#sval1link').mouseover(function(e) {
        $('#sval1').mouseover();
    }).mouseout(function(e) {
            $('#sval1').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval2link').mouseover(function(e) {
        $('#sval2').mouseover();
    }).mouseout(function(e) {
            $('#sval2').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval3link').mouseover(function(e) {
        $('#sval3').mouseover();
    }).mouseout(function(e) {
            $('#sval3').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval4link').mouseover(function(e) {
        $('#sval4').mouseover();
    }).mouseout(function(e) {
            $('#sval4').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval5link').mouseover(function(e) {
        $('#sval5').mouseover();
    }).mouseout(function(e) {
            $('#sval5').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval6link').mouseover(function(e) {
        $('#sval6').mouseover();
    }).mouseout(function(e) {
            $('#sval6').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval7link').mouseover(function(e) {
        $('#sval7').mouseover();
    }).mouseout(function(e) {
            $('#sval7').mouseout();
    }).click(function(e) { e.preventDefault(); });
});

$(function() {
    $('.map').maphilight();
    $('#sval8link').mouseover(function(e) {
        $('#sval8').mouseover();
    }).mouseout(function(e) {
            $('#sval8').mouseout();
    }).click(function(e) { e.preventDefault(); });
});


