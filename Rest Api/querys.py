def mappings():
    mapping={
            "mappings" : {
            "properties" :{
                "firstname" : {
                "type" : "text",
                "fields" : {
                    "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                    }
                }
                },
                "lastname": {
                "type":"text",
                "fields" : {
                    "keyword":{
                    "type": "keyword",
                    "ignore_above":256
                    }
                }
                },
                "password" : {
                "type" : "text",
                "fields" : {
                    "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                    }
                }
                },
                "user" : {
                "type" : "text",
                "fields" : {
                    "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                    }
                }
                },
                "total_price": {
                "type": "long"
                },
                "depositpaid":{
                "type":"boolean"
                },
                "additionalneeds": {
                "type": "text",
                "fields": {
                    "keyword":{
                    "type": "keyword",
                    "ignore_above":256
                    }
                }
                },
                "token":{
                "type": "text",
                "fields": {
                    "keyword":{
                    "type": "keyword",
                    "ignore_above":256
                    }
                }
                },
                "bookingdates":{
                    "properties":{
                        "checkin":{"type":"date"},
                        "checkout":{"type":"date"}
                    }
                }
            }   
        }
    }
    return mapping

def search_user(user, psw):
    query = {
        "query":{
            "bool":{
                "must":[
                    {"match":{"user":user}},
                    {"match":{"password":psw}}
                ]
            }
        }
    }
    return query

def insert_data(name, lastn, usr, psd):
    e = {
        "firstname":name,
        "lastname":lastn,
        "user": usr,
        "password":psd,
        "totalprice": 111,
        "depositpaid": False
    }
    return e

def update(token, chi, cho, add):
    body = {"doc":{
                "bookingdates":{
                "checkin":chi,
                "checkout":cho,
                },
                "token":token,
                "additionalneeds":add,
                "depositpaid": False
                }
            }
    return body

def search(id):
    query = {
        "query":{
            "bool":{
                "must":[
                    {"match":{"_id":id}}
                ]
            }
        }
    }
    return query

def search_book(tkn, usr):
    query = {
        "query":{
            "bool":{
                "must":[
                    {"match":{"user":usr}},
                    {"match":{"token":tkn}}
                ]
            }
        }
    }
    return query
    
def update_dates(chi, cho):
    body = {"doc":{
            "bookingdates":{
            "checkin":chi,
            "checkout":cho,
            }
            }
        }
    return body

def update_pay():
    body = {"doc":{
            "depositpaid":True
            }
        }
    return body