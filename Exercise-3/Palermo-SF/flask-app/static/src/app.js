import React from "react";
import ReactDOM from "react-dom";
import Sidebar from "./components/Sidebar";

// setting up mapbox
mapboxgl.accessToken =
  "pk.eyJ1Ijoic2ljaWxpYW40ZXZlciIsImEiOiJja2Zhc2FlbWQwejE5Mnpxc2w4cmRtaDdwIn0.wOeM_rP6W0c4sJ4HtBxcyQ";

var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/sicilian4ever/ckf2qvcu30hmd19o18x4lplfd",
  center: [13.350907, 38.121610],
  zoom: 13.64,
});

ReactDOM.render(<Sidebar map={map} />, document.getElementById("sidebar"));

function formatHTMLforMarker(props) {
  var { name, hours, address } = props;
  var html =
    '<div class="marker-title">' +
    name +
    "</div>" +
    "<h4>Operating Hours</h4>" +
    "<span>" +
    hours +
    "</span>" +
    "<h4>Address</h4>" +
    "<span>" +
    address +
    "</span>";
  return html;
}

// setup popup display on the marker
map.on("click", function (e) {
  map.featuresAt(
    e.point,
    { layer: "trucks", radius: 10, includeGeometry: true },
    function (err, features) {
      if (err || !features.length) return;

      var feature = features[0];

      new mapboxgl.Popup()
        .setLngLat(feature.geometry.coordinates)
        .setHTML(formatHTMLforMarker(feature.properties))
        .addTo(map);
    }
  );
});

map.on("click", function (e) {
  map.featuresAt(
    e.point,
    { layer: "trucks-highlight", radius: 10, includeGeometry: true },
    function (err, features) {
      if (err || !features.length) return;

      var feature = features[0];

      new mapboxgl.Popup()
        .setLngLat(feature.geometry.coordinates)
        .setHTML(formatHTMLforMarker(feature.properties))
        .addTo(map);
    }
  );
});
