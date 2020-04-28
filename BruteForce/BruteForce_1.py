# For 'http://xcz.kr/START/prob/prob26.php'
# Reference : 'https://gyeongje.tistory.com/314'

import urllib.request       # HTTP 요청 기능을 담은 모듈
import urllib.parse         # URL 해석, 조작 기능을 담은 모듈

url = 'http://xcz.kr/START/prob/prob26.php'
cookie = {'Cookie' : 'PHPSESSID=p4c2tj84o9vfpvm40gtnpndtf1'}    # document.cookie
msg = 'Yh9/=-^:86/f87Y?]-@L}<_E|*1/=-Xi!"Hx865C|-}:|*DL*G_i86/f868FX(@g@-Lh|)=D}_93@_18@g9,*3YC$(@P'

def submit(value):
    post_data = {'encode' : value}  # tuple
    post_data = urllib.parse.urlencode(post_data)   # tuple을 POST 방식으로 전송하기 위한 데이터로 변환
    post_data = post_data.encode()  # Unicode를 문자열로 변환

    request = urllib.request.Request(url, headers=cookie)   # URL 요청 인스턴트화
    response = urllib.request.urlopen(request, post_data).read()    # URL을 열고, 받아온 데이터를 byte형으로 반환 
    response = response.decode()    # 문자열을 Unicode로 변환
    
    res_idx = response.index("ENCODE : ")
    res_last_idx = response.index("</font></br></br>")

    return response[res_idx + 9 : res_last_idx - 1]     # ENCODE : ~ </font></br></br> 사이의 데이터

def solve(flag, index):
    for bf in range(32, 127):   # 32(SP : 공백 문자) ~ 126
        value = flag + chr(bf)
        result = submit(value)

        if result == msg:
            print("Flag is ", value)
            exit(1)
        
        if result.find(msg[: index + 1]) > -1:  # index 까지의 문자열이 같은 경우
            print(value)
            solve(value, index + 2)     # index + 1 까지의 문자열 비교
        elif result.find(msg[: index]) > -1:    # index 전까지의 문자열이 같은 경우
            print(value)
            solve(value, index + 1)     # index 까지의 문자열 비교

if __name__=="__main__":
    solve('', 1)
