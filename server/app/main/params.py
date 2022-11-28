from marshmallow import fields

 
CreateNotification = {
    "text" : fields.String(required=True),
    "url" : fields.String(missing="#")
}
