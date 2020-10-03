import React from "react";

export default function Intro() {
  return (
    <div className="intro">
      <h3>About</h3>
      <p>
        The app is built on the back-end using Flask 
        and Elasticsearch as the search engine. The 
        front-end is done with React.
      </p>
      <p> 
        The map displayed is deployed using the Mapbox API.
      </p>
      <p>
        The data for the app is available for free in the 
        Palermo's open-data portal website.
      </p>
    </div>
  );
}
