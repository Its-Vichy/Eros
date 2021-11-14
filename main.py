from module import captcha, generator, email
from colorfull import init; init()
import threading, time, random
from api import website

__INVITE__ = '6wn8M8Xy'

class Launcher:
    def __init__(self):
        self.hc_accessibility = [
            #"FjIPBZ+Rv04XoGVO/fsUejZwyiknu5yqFpzaQkROylr6Dg1nLlOgyq1exo1F23k5GPw5ycsV2TzJ4MIR+o1HGfJYyc6BWp5ZtS7JTJ84W8c3NRLj75Zt9oyuReX1P0FpZeo2OybUgxMP0lC1sZm66+50hk0wpCEnZJKS/filn35nv21fLnYi4lDWmZfiGnOlylPYyJltVEKEE1fksOVd42ERpbSSdNCoz7XJAvWPtOCTEhldQaEmFfIHgdhCQEuwgc6xmK99EQEGFgisFM0ov+LFhhbPLz8it3BKwB5AgBR4QgZhSTV2iA+nNbPRepF+YNz2UrE7TYOJO5wWu7o0RjCFYbUZZj2pAu1uCOf4tHqW5PeFom3HrcIpEDCdyH4fnxWMvFiBvgI5RWo4TOX/4fRu9QsOorHnvaQ09aImZ80WejtH0xePjALG6mc6umi9TIHdP6sIIb8pJ2GSE9GbtDwsTbdXxfftAygJQpirJ5Dp51clztQlhSjjsO1WG9LWdbVy+8MIa2x3PfxbOSSWR7I2GViP6xb0MkC4iz+OJmseCZkoE8VZJlRO65fxXFjCik4YAO6LfskDvrrFpQX4mhFT38jxXbYMFwOClJnIUrIC2p6WQHHMFOW23HRlusX59LjIrw0lSqFUkyJUgdE4kdN0Xc03ysRmPt3PVmG8NXBtqaNSZqxLIrd17xNPcArarUBOm0dMuZX67JhJ9ER0kXpV/Iwi9Lo8AjD5q6G4oZpJXsBliCaiZc5Te7VrbRT/eNx8CI1JqYhhGWGJ3dUQIMSh7VREMRVt+bQtnl5eONt1HnbGt85UfGCwhPZttupjirjb1ZexUBmq3ES8OWJjh+q85KIxVdsnxeT00c0rJl2KKPS9+4vKdim3RHMF43b82+GmcQurrJ1GKIIM6MiyODUAsn1XYFQuYVUyBNsHUKL2wC6QDvw+plSWH/yFXSrWQxilQD3B5cVmEcr9ahIjzSeAm9JJDXP/o9ASoHHYJkqDkG38fIOStQWuKTYhGf+2EHEZnHLfcj6hrIh22PsCkT/w+qUkdb9Lnc5p8g==pdJOMsoeSx+xRiJo"
            "m/pXEd7YgCeHFzTfPjdHDW/O7FW5U1z5/ih3oTmIZi1nrEHYB2FIkOXGg+3grdQC/cvECleUPMjSHZZN5gocWm5qRUHjSlU41JVGEFLQc9KzV6MVYBHvXecpKMeWadjk6HFGCUaZyTif6StTlV7mf8oa890RAWUwGOyy+fMwjXlKIwJDoetrrTuwWOibUFYUejqpPaVHOGtnARUTZf6ZewnqeaYQBmtNPPPbqyQQVEeqjg6WXmulmdNB7gc7fgJO4uQP7OrJX6AbdGvrj8LHzsQbxCuazSHJFIS1ue8z2sfG2JzsNZN7wW8MV9B138qGH/M+kyC37+JZzJws2D12n7Vh3nAIbVGWS3Q8rZcGol+E9AbPQGCSjx6skFdzaSr9GYeeh3hIqLy78S4l5Hyv5A0TH6rH45m3STVu0SMmWtGZBIxgYyj7zXTz+9iZUbYT8Sb/4oyKGufe8vcblgk6NusRxzlYJG4cN6r2qR8yxblUW1TLyggMBbP75r5sd6Fc07kQp6gmG3/znoaTFWYE/3nnH6wncBZ8Ue1ACMnSUpAyeTcpXkTvehCzYZVLYoCttQrmFqX0BTu5RG7hpV4pa0w/+rFKNlFYckW/crBmZK17m7VGsF+GWzQMoPTZFPDm1RbrpgRNj4sKolBm3/B1r6t1aE+Yh+v7tg5ssJ4BJaqlFEk1UqoorKeuPoXboM/3kanH27wlzO3mKroQfe8CmwX1i6UMWobZi4+RfzEquDeYQtnsjXrmIckWDuCLYriALpmcBpsKuA81kXJLo18GQHKc/Ih8QvZDA/bd3vuKn0AppBw9p3+yWQyrUnn5mi93byp6J9UgShe5MF0xhASJXFecJZQrFLW1RWy5ogOWS36ECeymO0O7XxbaG44+ZrGcK2DE9vvAEVoDu4zmbEB0OWoDuuNRDQ6Bm9zNtFmeYUuFH7/e62fyMn/k4ucyiag1PeehF8u5mUvlb3t3OTqnki3i56MvsbLPto/1s9KH9QOyQJoJMJv7ZKffV1lQ3mBx4PZlVwK3bvC4Di2dyyiFTAMXl04zRenUTavFbN6PeUs=FtfLw/0mzyH8d/Tz"
        ]

        self.captcha_keys = []
        self.proxy = []
    
    def get_captcha_thread(self):
        while True:
            proxy = random.choice(self.proxy)
            key = captcha.Bypass(self.hc_accessibility).get_hcaptcha_key('app.revolt.chat', '3daae85e-09ab-4ff6-9f24-e8f4f335e433', proxy)
            
            if key != False:
                self.captcha_keys.append(key)
                print(f'*> New captcha: {key[:10]}')
    
    def generation_thread(self):
        while True:
            Email = email.Email()
            WebApi = website.Api_Website()
            Generator = generator.Generator()

            # Lmao opti
            captcha_1 = None
            captcha_2 = None

            while captcha_1 == None:
                while len(self.captcha_keys) == 0:
                    time.sleep(1)

                captcha_1 = self.captcha_keys[0]
                self.captcha_keys.remove(captcha_1)
                print('-> Captcha_1:', captcha_1[:10])
            
            while captcha_2 == None:
                while len(self.captcha_keys) == 0:
                    time.sleep(1)

                captcha_2 = self.captcha_keys[0]
                self.captcha_keys.remove(captcha_2)
                print('-> Captcha_2:', captcha_2[:10])
            
            mail = None
            
            while mail == None:
                try:
                    mail = Email.get_email()
                except:
                    print(f'*-> Waiting for email')
                    time.sleep(1)
                    pass

            invite = WebApi.get_invite_code()
            password = Generator.get_password()
            username = Generator.get_username()

            print(f'Loading *-> {username} -> {mail}:{password}')
            if WebApi.create_account(invite, mail, password, captcha_1):
                code = None
                
                while code == None:
                    time.sleep(1)
                    for id in Email.get_mails_list():
                        code = Email.get_verif_code(Email.get_message(id))

                WebApi.verify_account(code)
                token = WebApi.get_token(captcha_2, mail, password)
                WebApi.complete(username, token)
                WebApi.join_server(__INVITE__, token)

                print(f'Generated *-> {username} -> {mail}:{password}')
                with open('./config/accounts.txt', 'a+') as acc_file:
                    acc_file.write(f'{mail}:{password}:{token}\n')
    
    def main(self):
        with open('./config/proxy.txt', 'r+') as proxy_file:
            for proxy in proxy_file:
                if 'socks4://' not in proxy:
                    self.proxy.append(proxy.split('\n')[0])
        
        self.proxy = list(set(self.proxy))
        print(f'{len(self.proxy)} Proxies loaded.')

        for _ in range(15):
            threading.Thread(target= self.get_captcha_thread, args=()).start()
        
        for _ in range(10):
            threading.Thread(target= self.generation_thread, args=()).start()

Launcher().main()