import requests, json

class Api_Website:
    def __init__(self):
        pass

    def get_invite_code(self):
        return str(requests.get("https://campaign.revolt.chat/api/revolt.chat", allow_redirects= True).url).split('?code=')[1].strip().split('\n')[0]
    
    def create_account(self, invite: str, email: str, password: str, captcha_key: str):
        r = requests.post("https://api.revolt.chat/auth/account/create", headers= {'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}, json={"email": email, "password": password, "invite": invite,"captcha": captcha_key})
        
        if r.status_code != 204:
            print(f"[-] Error: {r.text}")
            return False
        else:
            return True

    def verify_account(self, verif_url: str):
        r = requests.post(verif_url)
        #print(r.status_code, r.text)
    
    def get_token(self, captcha_key: str, email: str, password: str):
        r = requests.post("https://api.revolt.chat/auth/session/login", headers= {'content-type': 'application/json'}, json={"email": email,"password": password,"captcha": captcha_key,"friendly_name":"chrome on Windows 10"})
        #print('token:', r.status_code, r.text)

        if r.status_code == 200:
            return json.loads(r.text)['token']
    
    def complete(self, username: str, token: str):
        r = requests.post("https://api.revolt.chat/onboard/complete", headers= {'content-type': 'application/json', 'x-session-token': token}, json={"username": username})
        #print(r.status_code, r.text)

    def join_server(self, invite: str, token: str):
        r = requests.post(f"https://api.revolt.chat/invites/{invite}", headers= {'content-type': 'application/json', 'x-session-token': token})