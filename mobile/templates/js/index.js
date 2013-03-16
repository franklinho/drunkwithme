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

                         var activeInfoWindow;

						 {% for bar in bars %}
						 var bar{{bar.id}}content ="<div style='font-weight:bold; font-family:aria,helvetica;'>"+
                            '<p>{{bar.name}}<br>'+
                            '<a href="http://maps.google.com/maps?q={{bar.address}}&hq={{bar.name}}">{{bar.address}}</a></p>'+
                            '</div>';

                        var bar{{bar.id}}infoWindow = new google.maps.InfoWindow({
                        content: bar{{bar.id}}content
                        });

                         var pos{{bar.id}} = new google.maps.LatLng({{bar.latitude}},
											    {{bar.longitude}});
                         var pinColor = "1FC219";
                         var pinImage = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor;
						 var bar{{bar.id}} = new google.maps.Marker({
											     map: map,
											     position: pos{{bar.id}},
                                                 icon: pinImage,
											 });
                        google.maps.event.addListener(bar{{bar.id}}, 'click', function() {
                                           if ( activeInfoWindow != bar{{bar.id}}.infoWindow ) {
                                               activeInfoWindow.close();
                                           }        
                                           bar{{bar.id}}infoWindow.open(map,bar{{bar.id}});
                                           activeInfoWindow = bar{{bar.id}}infoWindow;
                                           });   

						 {% endfor %}


						 map.setCenter(pos);
						 google.maps.event.addListener(marker, 'click', function() {
                                           if ( activeInfoWindow != infowindow ) {
                                               activeInfoWindow.close();
                                           }  
                                           infowindow.open(map,marker);
                                           activeInfoWindow = infowindow;
									       });            
					     }, function() {
						 handleNoGeolocation(true);
					     });


} else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
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