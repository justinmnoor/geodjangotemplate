// ENVIRONMENT VARIABLES
// ======================

var lon = -122;
var lat = 37.7;
var zoom = 9;


// MAP TILE
// =========

map = new L.map('map').setView([lat, lon], zoom);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19,
}).addTo(map);
