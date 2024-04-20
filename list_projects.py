# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth 
import json

url = "https://simranlohana7.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF03AllxxqXQYmbULxYfgsQ79D3-n9ZY9plcBwvdXlkEUIDmi1QtOY0f6TYSv5nW-uZ3r9aiqBgjBobqYYXyB7qxrhuuybvoc88ISI_qCVn9464U_bBnQOi6L7OKAPbVpnlhqX7adjBVgQkZ_KHKLDOba4-a_u2oMtoQioE8cRyIzs=054702FA"


auth = HTTPBasicAuth("simranlohana7@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
