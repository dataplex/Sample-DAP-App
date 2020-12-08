import http.client
import mimetypes
import ssl
import base64
import os

tokenFile = os.environ['CONJUR_AUTHN_TOKEN_FILE']
lbURL     = os.environ['CONJUR_APPLIANCE_URL']
conjAcct  = os.environ['CONJUR_ACCOUNT']
secret    = os.environ['CONJUR_SECRET']

thisSessionToken = open(tokenFile,"rb").read()

encodedCred      = base64.b64encode(thisSessionToken)

print(thisSessionToken)
print(encodedCred)

print("Printing environment variables")
print(lbURL)
print(tokenFile)
print(conjAcct)
print(secret)

cleanURL = lbURL.replace("https://", "")

conn = http.client.HTTPSConnection(cleanURL, context = ssl._create_unverified_context())
payload = ''
headers = {

  'Authorization': 'Token token="' + encodedCred.decode('ascii') + '"'

}

print(headers)

conn.request("GET", "/secrets/" + conjAcct + "/variable/" + secret, payload, headers)

res = conn.getresponse()

data = res.read()

print('This secret is: ',data.decode("utf-8"))
