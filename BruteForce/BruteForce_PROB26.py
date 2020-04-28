import urllib.request
import urllib.parse

url = 'http://xcz.kr/START/prob/prob26.php'
cookie = {'Cookie' : 'PHPSESSID=p4c2tj84o9vfpvm40gtnpndtf1'}
message = 'Yh9/=-^:86/f87Y?]-@L}<_E|*1/=-Xi!"Hx865C|-}:|*DL*G_i86/f868FX(@g@-Lh|)=D}_93@_18@g9,*3YC$(@P'

def trans_data(value, url, cookie):
    post_data = {'encode' : value}
    post_data = urllib.parse.urlencode(post_data)
    post_data = post_data.encode()

    request = urllib.request.Request(url, headers=cookie)
    response = urllib.request.urlopen(request, post_data).read()
    response = response.decode()
    
    res_idx = response.index("ENCODE : ")
    res_last_idx = response.index("</font></br></br>")

    return response[res_idx + 9 : res_last_idx - 1]

def solve(flag, index):
    for bf in range(32, 127):
        value = flag + chr(bf)
        out = trans_data(value, url, cookie)

        if out == message:
            print("Flag is ", value)
            exit(1)
        
        if out.find(message[:index + 1]) > -1:
            print(value)
            solve(value, index + 2)
        elif out.find(message[:index]) > -1:
            print(value)
            solve(value, index + 1)

if __name__=="__main__":
    solve('', 1)
