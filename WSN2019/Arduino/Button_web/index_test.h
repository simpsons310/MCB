const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
  <head>
    <script>
      function sendData(led) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("LEDState").innerHTML =
                this.responseText;
            }
          };
        xhttp.open("GET", "setLED?LEDstate="+led, true);
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
              document.getElementById("ADCValue").innerHTML =
              this.responseText;
          }
        };
        xhttp.open("GET", "readADC", true);
        xhttp.send();
    }
}
</script>
  </head>
  <body>
    <div id="taskbar">
      <h1> User information here </h1>
    </div>
    <div id="display">
      <div class="menu">
        <div id = "menu_text"> <strong> MENU  </strong> </div>
        <div id = "menu_list">
          <ul class="list">
            <li> List 1 </li>
            <li> List 2 </li>
            <li> List 3 </li>
          </ul>
        </div>
        <div id = "description">
          <p> Descirption </p>
        </div>
      </div>
      <div class="data">
        <div id="led_control">
          <button type="button" onclick="sendData(1)">LED ON</button>
          <button type="button" onclick="sendData(0)">LED OFF</button><BR>
        </div>
        <div id="ADC_value">
          ADC Value is : <span id="ADCValue">0</span><br>
            LED State is : <span id="LEDState">NA</span>
      </div>
    </div>
  </body>
</html>
)=====";
