Mininote
========

**Mininote** is a web service that provides a convenient JSON REST API for work with notes.


For using Mininote you should start MongoDB instance.


#API Reference


###Register new user

**Request**: POST /user

**Request body**:
```json
{
	"username": "String",
	"password": "String"
}
```

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": "None"
}
```

* Length of username and password should be no more than 20 characters

*cURL example request*: `curl -i -X POST -H "Content-Type: application/json" -d '{"username":"username","password":"password"}' http://localhost:5000/api/user`



###Get list of user's notes

**Request**: GET /notes

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": [{
	"note_id": "String",
	"subject": "String",
	"creation_time": "Integral",
	"modification_time": "Integral"
	},]
}
```

* Service use Basic HTTP Auth; every request must contains username and password
* If user has not any notes, service return empty list

*cURL example request*: `curl -i -u username:password http://localhost:5000/api/notes`


###Get one note

**Request**: GET /notes/<note_id>

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": {
	"note_id": "String",
	"subject": "String",
	"body": "String",
	"creation_time": "Integral",
	"modification_time": "Integral"
	}
}
```

* Service use Basic HTTP Auth; every request must contains username and password

*cURL example request*: `curl -i -u username:password http://localhost:5000/api/notes/<note_id>`


###Make note

**Request**: POST /notes

**Request body**:
```json
{
	"subject": "String",
	"body": "String"
}
```

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": "None"
}
```

* Service use Basic HTTP Auth; every request must contains username and password

*cURL example request*: `curl -i -u username:password -X POST -H "Content-Type: application/json" -d '{"subject":"Hello world","body":"Lorem ipsum"}' http://localhost:5000/api/notes`


###Edit note

**Request**: PUT /notes/<note_id>

**Request body**:
```json
{
	"subject": "String",
	"body": "String"
}
```

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": "None"
}
```

* Service use Basic HTTP Auth; every request must contains username and password
* Send an empty subject or body fielf if you do not need to change it

*cURL example request*: `curl -i -u username:password -X PUT -H "Content-Type: application/json" -d '{"subject":"","body":"Dolor sit amet"}' http://localhost:5000/api/notes/<note_id>`


###Delete note

**Request**: DELETE /notes/<note_id>

**Response**:
```json
{
	"success": "Boolean",
	"message": "String",
	"data": "None"
}
```

* Service use Basic HTTP Auth; every request must contains username and password

*cURL example request*: `curl -i -u username:password -X DELETE -H "Content-Type: application/json" http://localhost:5000/api/notes/<note_id>`