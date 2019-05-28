var express = require('express');
var router = express.Router();

router.get('/', function(req, res){
    res.render('profile');
});

// /* GET home page. */
// router.get('/', function(req, res, next) {
//   res.render('profile', { title: 'Express' });
// });

module.exports = router;
