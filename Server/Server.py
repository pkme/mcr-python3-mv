import socketserver, time 
import subprocess
import socket

class MyServer(socketserver.BaseRequestHandler):  


  def handle(self):  

    print ('Connected from', self.client_address)

    while True:  

      receivedData = self.request.recv(8192)
      
      receivedData = receivedData.decode()

      if not receivedData:  

        continue    

      elif receivedData == 'Hi,server':
        byt='hi,client'
        byt=byt.encode()
        self.request.sendall(byt)     

        while True:  
          print ('please wait...') 
          f = open('IN_Inter_P.txt', 'wb')  
          while True:  
            data = self.request.recv(1024)
            bytEOF = 'EOF'
            bytEOF = bytEOF.encode()
            if data == bytEOF:  
              break
            f.write(data)
            
          f.flush()  
          f.close()  
          print ('download finished') 
          break

        f = open('a2.txt', 'wb') 
        p = subprocess.Popen('./run_M_GeneAlgorMain.sh /opt/mcr/v93', stdout=subprocess.PIPE, shell=True)
        f.write(p.stdout.read())
        f.flush()  
        f.close()

        sfile = open('OUT_Res.txt', 'rb')  
        while True:  
          data = sfile.read(1024)
          if not data:
            break
          while len(data) > 0: 
            intSent = self.request.send(data)  
            data = data[intSent:]  
        sfile.flush()  
        sfile.close()

        time.sleep(3)
        byt='EOF'
        byt=byt.encode()
        self.request.sendall(byt)
        
      elif receivedData == 'bye':  
        break    
        

    self.request.close()  
    print ('Disconnected from', self.client_address ) 

  

if __name__ == '__main__':  

  print ('Server is started\nwaiting for connection...\n')
  
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
      s.connect(('8.8.8.8', 80))
      ip = s.getsockname()[0]
  finally:
      s.close()
  print (ip)
  srv = socketserver.ThreadingTCPServer((ip, 50000), MyServer)  

  srv.serve_forever()

