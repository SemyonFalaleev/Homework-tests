import requests

def vote(votes):
    return max(votes, key = lambda e: votes.count(e))

def discriminant(a, b, c):
    result = b**2 - 4*a*c
    return result

def solution(a, b, c):
    d_ = discriminant(a, b, c)
    if d_ < 0:
        result = None
    elif d_ == 0:
        result = -b/(2*a)
    elif d_ > 0:
        x1 = (-b + d_**0.5)/(2*a)
        x2 = (-b - d_**0.5)/(2*a)
        result =[x1, x2]
    return result

def check_age(age: int):
    if age >= 18 :
        result = True
    else:
        result = False

    return result

class YandexDiskApi():
    def __init__(self, token):
        self.token = token
        self.url_ya_disk = "https://cloud-api.yandex.net"
    
    def create_folder(self, path: str, fields=None):
        params = {
            'path': path,
            'fields': fields
        }
        headers = {
            'Authorization': self.token
        }
        metod_url = "/v1/disk/resources"
        response = requests.put(f"{self.url_ya_disk}{metod_url}", params=params, headers=headers)
        return response.status_code
