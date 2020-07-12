# Externship-covid19-Delivery

Sorry sir, Actually I am choosen hard problem but, I am not able to complete "prediction part using goverment dataset with tensorflow" due to bad innternt connective mine training was not completed but till "medium" I am completed everything. So, I hope you will consider. 

Description About Project:

frontend: HTML, CSS, Javascript
Backend: Django
Database: sqllite3
for google map i used "mapbox" if u want to run this map on ur system u have to use your access token key, and this key you will get after registering on "mapbox"
Ex :-  index.html  (line no 187-195 but we have to change only token key)
       <script>
       mapboxgl.accessToken = 'pk.eyJ1Ijoic2hpdmFtMTIiLCJhIjoiY2tjaHE5b2FlMDdkbzJzcDVmZ2N5anZ3eSJ9.QFXyEegbx6aKOIxFRCWRCA';  ( ### you have to replace this token key with your           token key ) var map = new mapboxgl.Map({                                                                                               
       container: 'map',
       style: 'mapbox://styles/mapbox/dark-v10',
       zoom: 1,
       center: [0, 20]
       });
       </script>
       
functionality in this project:-
  --> There are three html page (index.html, analysis.html, bill.html)
  --> index.html ==> In this page u can submit your detail and make order and check covid cases on map in visual affect.
  --> bill.html ==> In this page bill will generate and there is one print button, by this button we can print the bill.
  --> analysis.html ==> In this page you can see the all order with datewise.
  --> In each page on the right top corner there is one search bar, You can use this and see older date order also by giving input date. 
       
