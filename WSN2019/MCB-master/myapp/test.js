var mysql = require('mysql');
var express = require('express');
var app = express();

var con = mysql.createConnection({
  host: "localhost",
  user: "tuananh",
  password: "abc13579",
  database: "wordpress"
});

var data = {};
app.set('view engine', 'ejs');
app.listen(3000);
var i = 1;
//while(i == 1){


con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM datasensor where id = (select max(id) from datasensor)", function (err, result, fields) {
    if (err) throw err;
    //console.log(result[0]);
    data = result[0];
    console.log(data);
    app.get('/', function(req, res){
        // var result = {
        //     id: 1,
        //     SensorID: 'Sensor1',
        //     Temp: 21,
        //     Hum: 86,
        //     Light: 932,
        //     Dust: 104,
        //     Time: '26-Mar-2019 23:08:52' };
        res.render('profile', {result: data});
    });
  });
});






// app.get('/', function(req, res){
//     res.sendFile(__dirname + '/index.html');
// });

app.get('/contact', function(req, res){
    res.send('this is the contact page');
});




//}