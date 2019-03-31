const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
<body>

<div id="demo">
<h1 style="position:relative;height: 60px;width:100%;background-color: lightblue;"> <span style="left: 50px; font-weight:bold;">Wireless Sensor Network 2019</h1>
</div>
<div style="top">
<button type="button" onclick="sendData()">LED</button><BR>
</div>
<div>
	Humidity Value is : <span id="hum">1</span><br>
  Temperature Value is : <span id="temp">1</span><br>
  Light 1 Value is : <span id="light1">1</span><br>
  Light 2 Value is : <span id="light2">1</span><br>
  Dust Value is : <span id="dust">0</span><br>
  LED State is : <span id="LEDState">NA</span>
</div>

<script>
var state = "";
function sendData() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("LEDState").innerHTML = this.responseText;
      state = this.responseText;
    }
  };
  xhttp.open("GET", "setLED?LEDstate="+state, true);
  xhttp.send();
}
setInterval(function() {
  // Call a function repetatively with 2 Second interval
  getData();
}, 2000); //2000mSeconds update rate

function getData() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var s = this.responseText;
        var temp = ""; 
        var data = [];
        var j = 0;
        for (var i = 0; i < s.length; i++){
          if(s[i] == "#"){
            data[j] = temp;
            temp = "";
            j++;
          }else{
            temp = temp + s[i];
          }
        }
        document.getElementById("hum").innerHTML = data[0];
        document.getElementById("temp").innerHTML = data[1];
        document.getElementById("light1").innerHTML = data[2];
        document.getElementById("light2").innerHTML = data[3];
        document.getElementById("dust").innerHTML = data[4];
      }
    };
    xhttp.open("GET", "/data", true);
    xhttp.send();
}
</script>
</body>
</html>
)=====";
