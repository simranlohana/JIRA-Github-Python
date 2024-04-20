# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://simranlohana7.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF03AllxxqXQYmbULxYfgsQ79D3-n9ZY9plcBwvdXlkEUIDmi1QtOY0f6TYSv5nW-uZ3r9aiqBgjBobqYYXyB7qxrhuuybvoc88ISI_qCVn9464U_bBnQOi6L7OKAPbVpnlhqX7adjBVgQkZ_KHKLDOba4-a_u2oMtoQioE8cRyIzs=054702FA"

    auth = HTTPBasicAuth("simranlohana7@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "SP"
        },
        "issuetype": {
            "id": "10001"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
