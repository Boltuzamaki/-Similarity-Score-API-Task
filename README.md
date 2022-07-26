# Similarity-Score-API-Task

Note - This API is also deployed on Heroku.

Endpoint address - https://sentence-similarity-glove.herokuapp.com/similarity


### Steps to run locally 

- Clone repo using 
```
git clone https://github.com/Boltuzamaki/Similarity-Score-API-Task.git
```
- Then run on cmd
```
pip install -r requirements.txt
```
- Extract the "embedding.zip" file

- Run app.py
```
python app.py 
```
- Either use POSTMAN to POST request on params 
  - sen1
  - sen2
  
  and endpoint http://127.0.0.1:5000/similarity

Or use script 

```py
import requests

sen1 = "This is a cat."
sen2 = "This is a Dog."

url = f"http://127.0.0.1:5000/similarity?sen1={sen1}&sen2={sen2}"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers)

print(response.text)
```

### Steps to use online API which is deployed on Heroku

- Use POSTMAN to POST request on params 
  - sen1
  - sen2
 
and endpoint https://sentence-similarity-glove.herokuapp.com/similarity

or use script

```py
import requests

sen1 = "This is a cat"
sen2 = "My house is new"

url = f"https://sentence-similarity-glove.herokuapp.com/similarity?sen1={sen1}&sen2={sen2}"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers)

print(response.text)
```
