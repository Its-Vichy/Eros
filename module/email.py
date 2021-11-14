import requests, re

class Email:
    def __init__(self):
        self.session = requests.session()
    
    def get_email(self):
        result = self.session.get('https://www.mohmal.com/fr/create/random', allow_redirects= True).text
        return result.split('data-email="')[1].split('@')[0] + '@emailnax.com'
    
    def get_mails_list(self):
        result = self.session.get('https://www.mohmal.com/fr/inbox', allow_redirects= True).text
        return re.compile('<tr data-msg-id="(.+?)"').findall(result)

    def get_message(self, id: str):
        msg = self.session.get("https://www.mohmal.com/en/message/" + str(id), allow_redirects=True).text
        return msg

    def get_verif_code(self, content: str):
        return str("https://api.revolt.chat/auth/account/verify/" + content.split('https://app.revolt.chat/login/verify/')[1].split('Sent by Revolt.')[0]).split('<')[0]