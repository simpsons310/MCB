var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "tuananh",
    password: "abc13579",
    database: "wordpress"
  });
  
var data = {};

con.connect();

/* GET users listing. */

router.get('/room1', function(req, res){
    
    if(req.query.token == "abcxyz"){
      con.query("SELECT * FROM room1 where id = (select max(id) from room1)", function (err, result, fields) {
          if (err) throw err;
          con.query("SELECT temp FROM room1 where temp = (select max(temp) from room1)", function (err, maxtemp, fields) {
            if (err) throw err;
            con.query("SELECT hum FROM room1 where hum = (select max(hum) from room1)", function (err, maxhum, fields) {
              if (err) throw err;
              con.query("SELECT light FROM room1 where light = (select max(light) from room1)", function (err, maxlight, fields) {
                if (err) throw err;
                con.query("SELECT dust FROM room1 where dust = (select max(dust) from room1)", function (err, maxdust, fields) {
                  if (err) throw err;
                  con.query("SELECT temp FROM room1 where temp = (select min(temp) from room1)", function (err, mintemp, fields) {
                    if (err) throw err;
                    con.query("SELECT hum FROM room1 where hum = (select min(hum) from room1)", function (err, minhum, fields) {
                      if (err) throw err;
                      con.query("SELECT light FROM room1 where light = (select min(light) from room1)", function (err, minlight, fields) {
                        if (err) throw err;
                        con.query("SELECT dust FROM room1 where dust = (select min(dust) from room1)", function (err, mindust, fields) {
                          if (err) throw err;
                          con.query("SELECT  AVG(temp) AS avgtemp FROM room1", function (err, avgtemp, fields) {
                            if (err) throw err;
                            con.query("SELECT  AVG(hum) AS avghum FROM room1", function (err, avghum, fields) {
                              if (err) throw err;
                              con.query("SELECT  AVG(light) AS avglight FROM room1", function (err, avglight, fields) {
                                if (err) throw err;
                                con.query("SELECT  AVG(dust) AS avgdust FROM room1", function (err, avgdust, fields) {
                                  if (err) throw err;
                                  var a = {result: result[0], 
                                          maxtemp: maxtemp[0], maxhum: maxhum[0], maxlight: maxlight[0], maxdust: maxdust[0],
                                          mintemp: mintemp[0], minhum: minhum[0], minlight: minlight[0], mindust: mindust[0],
                                          avgtemp: avgtemp[0], avghum: avghum[0], avglight: avglight[0], avgdust: avgdust[0]
                                        };
                                        res.json(a);
                                });
                              });
                            });
                          });
                        });
                      });
                    });
                  });
                });
              });
            });
          });
      });
    }
    else {
      res.json({message: "failed"});
    }
});
router.get('/room2', function(req, res){
  if(req.query.token == "abcxyz"){
    con.query("SELECT * FROM room2 where id = (select max(id) from room2)", function (err, result, fields) {
      if (err) throw err;
      con.query("SELECT temp FROM room2 where temp = (select max(temp) from room2)", function (err, maxtemp, fields) {
        if (err) throw err;
        con.query("SELECT hum FROM room2 where hum = (select max(hum) from room2)", function (err, maxhum, fields) {
          if (err) throw err;
          con.query("SELECT light FROM room2 where light = (select max(light) from room2)", function (err, maxlight, fields) {
            if (err) throw err;
            con.query("SELECT dust FROM room2 where dust = (select max(dust) from room2)", function (err, maxdust, fields) {
              if (err) throw err;
              con.query("SELECT temp FROM room2 where temp = (select min(temp) from room2)", function (err, mintemp, fields) {
                if (err) throw err;
                con.query("SELECT hum FROM room2 where hum = (select min(hum) from room2)", function (err, minhum, fields) {
                  if (err) throw err;
                  con.query("SELECT light FROM room2 where light = (select min(light) from room2)", function (err, minlight, fields) {
                    if (err) throw err;
                    con.query("SELECT dust FROM room2 where dust = (select min(dust) from room2)", function (err, mindust, fields) {
                      if (err) throw err;
                      con.query("SELECT  AVG(temp) AS avgtemp FROM room2", function (err, avgtemp, fields) {
                        if (err) throw err;
                        con.query("SELECT  AVG(hum) AS avghum FROM room2", function (err, avghum, fields) {
                          if (err) throw err;
                          con.query("SELECT  AVG(light) AS avglight FROM room2", function (err, avglight, fields) {
                            if (err) throw err;
                            con.query("SELECT  AVG(dust) AS avgdust FROM room2", function (err, avgdust, fields) {
                              if (err) throw err;
                              var a = {result: result[0], 
                                      maxtemp: maxtemp[0], maxhum: maxhum[0], maxlight: maxlight[0], maxdust: maxdust[0],
                                      mintemp: mintemp[0], minhum: minhum[0], minlight: minlight[0], mindust: mindust[0],
                                      avgtemp: avgtemp[0], avghum: avghum[0], avglight: avglight[0], avgdust: avgdust[0]
                                    };
                                    res.json(a);
                            });
                          });
                        });
                      });
                    });
                  });
                });
              });
            });
          });
        });
      });
  });
}
else {
  res.json({message: "failed"});
}
});

router.get('/room3', function(req, res){
  if(req.query.token == "abcxyz"){
    con.query("SELECT * FROM room3 where id = (select max(id) from room3)", function (err, result, fields) {
      if (err) throw err;
      con.query("SELECT temp FROM room3 where temp = (select max(temp) from room3)", function (err, maxtemp, fields) {
        if (err) throw err;
        con.query("SELECT hum FROM room3 where hum = (select max(hum) from room3)", function (err, maxhum, fields) {
          if (err) throw err;
          con.query("SELECT light FROM room3 where light = (select max(light) from room3)", function (err, maxlight, fields) {
            if (err) throw err;
            con.query("SELECT dust FROM room3 where dust = (select max(dust) from room3)", function (err, maxdust, fields) {
              if (err) throw err;
              con.query("SELECT temp FROM room3 where temp = (select min(temp) from room3)", function (err, mintemp, fields) {
                if (err) throw err;
                con.query("SELECT hum FROM room3 where hum = (select min(hum) from room3)", function (err, minhum, fields) {
                  if (err) throw err;
                  con.query("SELECT light FROM room3 where light = (select min(light) from room3)", function (err, minlight, fields) {
                    if (err) throw err;
                    con.query("SELECT dust FROM room3 where dust = (select min(dust) from room3)", function (err, mindust, fields) {
                      if (err) throw err;
                      con.query("SELECT  AVG(temp) AS avgtemp FROM room3", function (err, avgtemp, fields) {
                        if (err) throw err;
                        con.query("SELECT  AVG(hum) AS avghum FROM room3", function (err, avghum, fields) {
                          if (err) throw err;
                          con.query("SELECT  AVG(light) AS avglight FROM room3", function (err, avglight, fields) {
                            if (err) throw err;
                            con.query("SELECT  AVG(dust) AS avgdust FROM room3", function (err, avgdust, fields) {
                              if (err) throw err;
                              var a = {result: result[0], lastResult: result[1], 
                                      	maxtemp: maxtemp[0], maxhum: maxhum[0], maxlight: maxlight[0], maxdust: maxdust[0],
                                      	mintemp: mintemp[0], minhum: minhum[0], minlight: minlight[0], mindust: mindust[0],
                                      	avgtemp: avgtemp[0], avghum: avghum[0], avglight: avglight[0], avgdust: avgdust[0]
                                    };
                                    res.json(a);
                            });
                          });
                        });
                      });
                    });
                  });
                });
              });
            });
          });
        });
      });
  });
}
else {
  res.json({message: "failed"});
}
});

router.get('/room4', function(req, res){
if(req.query.token == "abcxyz"){
    con.query("SELECT * FROM room4 where id = (select max(id) from room4)", function (err, result, fields) {
      if (err) throw err;
      con.query("SELECT temp FROM room4 where temp = (select max(temp) from room4)", function (err, maxtemp, fields) {
        if (err) throw err;
        con.query("SELECT hum FROM room4 where hum = (select max(hum) from room4)", function (err, maxhum, fields) {
          if (err) throw err;
          con.query("SELECT light FROM room4 where light = (select max(light) from room4)", function (err, maxlight, fields) {
            if (err) throw err;
            con.query("SELECT dust FROM room4 where dust = (select max(dust) from room4)", function (err, maxdust, fields) {
              if (err) throw err;
              con.query("SELECT temp FROM room4 where temp = (select min(temp) from room4)", function (err, mintemp, fields) {
                if (err) throw err;
                con.query("SELECT hum FROM room4 where hum = (select min(hum) from room4)", function (err, minhum, fields) {
                  if (err) throw err;
                  con.query("SELECT light FROM room4 where light = (select min(light) from room4)", function (err, minlight, fields) {
                    if (err) throw err;
                    con.query("SELECT dust FROM room4 where dust = (select min(dust) from room4)", function (err, mindust, fields) {
                      if (err) throw err;
                      con.query("SELECT  AVG(temp) AS avgtemp FROM room4", function (err, avgtemp, fields) {
                        if (err) throw err;
                        con.query("SELECT  AVG(hum) AS avghum FROM room4", function (err, avghum, fields) {
                          if (err) throw err;
                          con.query("SELECT  AVG(light) AS avglight FROM room4", function (err, avglight, fields) {
                            if (err) throw err;
                            con.query("SELECT  AVG(dust) AS avgdust FROM room4", function (err, avgdust, fields) {
                              if (err) throw err;
                              var a = {result: result[0], 
                                      maxtemp: maxtemp[0], maxhum: maxhum[0], maxlight: maxlight[0], maxdust: maxdust[0],
                                      mintemp: mintemp[0], minhum: minhum[0], minlight: minlight[0], mindust: mindust[0],
                                      avgtemp: avgtemp[0], avghum: avghum[0], avglight: avglight[0], avgdust: avgdust[0]
                                    };
                                    res.json(a);
                            });
                          });
                        });
                      });
                    });
                  });
                });
              });
            });
          });
        });
      });
  });
}
else {
  res.json({message: "failed"});
}
});

router.post('/led1', function(req, res){
if(req.body.token == "abcxyz"){
  con.query(`insert into sttled1(led1,time) values(${req.body.signal},now())`, function (err, result, fields) {
      if (err) throw err;
      res.json(result[0]);
  });
}
else {
  res.json({message: "failed"});
}
});

router.post('/led2', function(req, res){
  if(req.body.token == "abcxyz"){
  con.query(`insert into sttled2(led2,time) values(${req.body.signal},now())`, function (err, result, fields) {
      if (err) throw err;
      res.json(result[0]);
  });
}
else {
  res.json({message: "failed"});
}
});

router.post('/controlled1', function(req, res){
if(req.body.token == "abcxyz"){
  con.query(`insert into controlled1(led1,time) values(${req.body.pwm},now())`, function (err, result, fields) {
      if (err) throw err;
      res.json({
        message: "success",
        data: result[0]
      });
  });
}
else {
  res.json({message: "failed"});
}
});

router.post('/controlled2', function(req, res){
  if(req.body.token == "abcxyz"){
  con.query(`insert into controlled2(led2,time) values(${req.body.pwm},now())`, function (err, result, fields) {
      if (err) throw err;
      res.json(result[0]);
  });
}
else {
  res.json({message: "failed"});
}
});

router.post('/login', function(req, res){
  if(req.body.user == "vutuananh" && req.body.pass == "abc13579"){
      res.json({status: 'success', token: 'abcxyz'});
  }
  else {
    res.json({status: 'failed'});
  }
});

module.exports = router;
