
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
    var mapOptions = {
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'),
			      mapOptions);

    var leprechaun='/static/img/leprechaun7.png';
    
    var contentString ="<div style='font-weight:bold; font-family:aria,helvetica;'>"+
        '<p>Level 7: Leprechaun<br>'+
        'Carbombs Take: 7<br>'+
        'Rank: 1<br>'+
        'Bars Checked In: 8</p>'+
        '</div>';

    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });

    // Try HTML5 geolocation
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = new google.maps.LatLng(position.coords.latitude,
                                             position.coords.longitude);

            var marker = new google.maps.Marker({
		map: map,
		position: pos,
		animation:google.maps.Animation.BOUNCE,
		icon: leprechaun,
            });

            map.setCenter(pos);
            google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
            });            
        }, function() {
            handleNoGeolocation(true);
        });


    } else {
        // Browser doesn't support Geolocation
        handleNoGeolocation(false);
    }
}

function handleNoGeolocation(errorFlag) {
    if (errorFlag) {
        var content = 'Error: The Geolocation service failed.';
    } else {
        var content = 'Error: Your browser doesn\'t support geolocation.';
    }

    var options = {
        map: map,
        position: new google.maps.LatLng(37.793796,-122.410548),
        content: content
    };

    var infowindow = new google.maps.InfoWindow(options);
    map.setCenter(options.position);
}


google.maps.event.addDomListener(window, 'load', initialize);