import requests

class Client:
  def __init__(self, root_url='http://localhost:5000'):
    self.root_url = root_url
    self.access_token = None    
    
  def postcall(self, path, payload, headers):
    return requests.post(self.root_url + path, json=payload, headers=headers)

class UserAuth:
  def __init__(self, user, password, client):
    self.user = user
    self.password = password
    self.client = client
    self.path = '/auth'
    
  def gettoken(self):
    body = {"username": self.user, "password": self.password}
    headers = {'Content-Type': 'application/json'}
    resp = self.client.postcall(self.path, body, headers)
    
    if resp.status_code != 200:
      print('Raise ERROR Instead')
    
    client.access_token = 'JWT ' + resp.json()['access_token']
    
    return client.access_token 
  
if __name__ == '__main__':
  client = Client()
  UserAuth('user1', 'abcxyz', client).gettoken()