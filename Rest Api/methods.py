
def send_data(result):
    """Send data about the user in query

    :param result: User information in database
    :type result: list
    :return: Necessary data about user
    :rtype: list
    """
    name = ''
    lastname =''
    token = ''
    chi = ''
    cho = ''
    price=''
    add = ''
    paid =''
    for doc in result['hits']['hits']:
        name = doc['_source']['firstname']
    for doc in result['hits']['hits']:
        lastname = doc['_source']['lastname']
    for doc in result['hits']['hits']:
        token = doc['_source']['token']
    for doc in result['hits']['hits']:
        chi = doc['_source']['bookingdates']['checkin']
    for doc in result['hits']['hits']:
        cho = doc['_source']['bookingdates']['checkout']
    for doc in result['hits']['hits']:
        price = doc['_source']['totalprice']
    for doc in result['hits']['hits']:
        add = doc['_source']['additionalneeds']
    for doc in result['hits']['hits']:
        paid = doc['_source']['depositpaid']
    data = [name, lastname, token, chi, cho, price, add, paid]
    return data

def validate_credentials(result):
    """Validate that user credential are correct

    :param result: User credential
    :type result: list
    :return: User credential in database
    :rtype: list
    """
    usr=''
    psw=''
    for doc in result['hits']['hits']:
        usr = doc['_source']['user']
    for doc in result['hits']['hits']:
        psw = doc['_source']['password']
    cred = [usr, psw]
    return cred
    