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