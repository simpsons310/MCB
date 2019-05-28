var http = require('http');
var dt = require('./myfirstmodule');

//create a server object:
http.createServer(function (req, res) {
  res.writeHead(200,{'Content-Type':'text/html'});
  res.write("Date and Time:; " + dt.myDateTime());
  res.write(req.url);
  res.end();
}).listen(3000);

