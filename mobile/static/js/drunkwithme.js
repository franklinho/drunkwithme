
// MENU
var menu;
 
function loaded() {
    document.addEventListener('touchmove', function(e){ e.preventDefault(); e.stopPropagation(); });
    menu = new slideInMenu('slidedownmenu', false);
}
document.addEventListener('DOMContentLoaded', loaded);

//MAP
var map;

function initialize() {

    $('#checkin').click(function(){
			    $('#checkinmodal').show();
			});
    $('#checkinmodal #closebutton').click(function(){
					      $('#checkinmodal').hide();
					      $('#checkinmodal #success').hide();
					  });

    $('#checkinmodal #checkin').click(function(){
					  var value = $('#baroption').val();
					  $.ajax({'url':'/checkin-action/'+value+'/'});
					  $('#checkinmodal #success').show();
				      });

    $('#drinkbutton').click(function(event) {
				event.preventDefault();
				$('#drinkaudio')[0].play();
				var value = $('#drinkoption').val();
				$.ajax({'url':'/drink-action/'+value+'/'});
			    });


}




google.maps.event.addDomListener(window, 'load', initialize);