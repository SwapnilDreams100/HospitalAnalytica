function maps(data_new)
{
    var locations = data_new
    center_coords = data_new[0]
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: new google.maps.LatLng(center_coords['lat'],center_coords['long']),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i]['lat'], locations[i]['long']),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent('org');
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
}