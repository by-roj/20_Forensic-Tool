# Reference : https://limjunyoung.tistory.com/29

import socket

for port in range(20, 30):
      try:
        s = socket.socket() # socket 객체 생성
        print("[+] Attempting to connect to 127.0.0.1:" + str(port))
        s.connect(('127.0.0.1', port))  # 서버와 연결을 설정
        #s.send("Port scan"\ \n") # 해당 포트의 서버로 데이터 전송
        banner = s.recv(1024) # 해당 포트의 서비스로부터 buffer_size만큼의 response 받아옴
        if banner:
            print("     [+] Port " + str(port)+" open: " + banner.decode(), end='')
        elif banner==b'':
            print("     [+] Port " + str(port)+" open: No Service!")
        s.close() # 서버와의 연결 닫음
      except: pass