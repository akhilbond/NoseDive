var express = require('express')
var bodyParser = require('body-parser')
var path = require('path')
var fs = require('fs')
var multer = require('multer')
var logger = require("morgan");

//set an instance for express
var app = express()

// Run Morgan for Logging
app.use(logger("dev"));
//Serve static content for the app from the "public" directory in the application directory.
app.use(express.static("public"));

var storage = multer.diskStorage({
	destination: function(req, file, callback) {
		callback(null, './public/uploads')
	},
	filename: function(req, file, callback) {
		console.log(file)
		callback(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname))
	}
})

app.post('/upload', function(req, res) {
	var upload = multer({
		storage: storage
	}).single('userFile')
	upload(req, res, function(err) {
		if(err){
			throw err
		}
		res.end('File is uploaded')
	})
})
// BodyParser makes it possible for our server to interpret data sent to it.
// The code below is pretty standard.
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.text());
// app.use(bodyParser.json({ type: "application/vnd.api+json" }));

// Sets an initial port. We"ll use this later in our listener
var PORT= process.env.PORT || 8080;

app.get('/', function(req,res){
	res.sendFile(path.join(__dirname,'/public/main-sign-in.html'))
})

app.get('/upload', function(req, res){
	res.sendFile(path.join(__dirname,"/public/loggedIn.html"))
})

app.post("/register", function(req, res){	
	//object(key value pairs)
	console.log(req.body)
	
	userValues = []
	for(var key in req.body){
		userValues.push(key + ":" + req.body[key])
	}
	userValues.push('\n')

	console.log(userValues)

	//put only values into an array for easy processing on python's end
	userData = __dirname + '/public/userData.txt';

	fs.appendFile("public/userData.txt", userValues, function(err){
		if(err){
			throw err
		}
		console.log("the data was appended the file!")
		res.redirect('/upload')
	})

})

app.listen(PORT, function() {
  console.log("App listening on PORT: " + PORT);
});
