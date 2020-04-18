import socket
from _thread import *
import threading 
  
players=0
questions=-1
sub=0
score1=0
score2=0
print_lock = threading.Lock() 
def threaded(c1,addr1,c2,addr2): 
    global players
    global questions
    global sub
    global score1
    global score2
    knowAns=1
    replydummy='replydummy'
    dum=1
    while True:
        if(players==2):
            message1=c1.recv(1024).decode('ascii').split(' ')
            message2=c2.recv(1024).decode('ascii').split(' ')
            if(message1[0]=='Ready!' and message2[0]=='Ready!' and questions==-1):
                c1.send('Lets Start!')
                c2.send('Lets Start!')
                questions+=1
            if(message1[0]=='ok' and message2[0]=='ok' and questions==0):
                message='Q1 : What is the color of orange?'
                c1.send(message.encode('ascii'))
                c2.send(message.encode('ascii'))
                print("Sent Q1 successfully")
                questions+=1
            # if(message1[0]=='restrict' and restrict==0):
            #     cannot_ans_response='cannot'
            #     c2.send(cannot_ans_response.encode('ascii'))
            #     restrict+=1
            # elif(message2[0]=='restrict' and restrict==0):
            #     cannot_ans_response='cannot'
            #     c1.send(cannot_ans_response.encode('ascii'))
            #     restrict+=1
            if(message1[0]=='dummyNo' and dum==1):
                c1.send(replydummy.encode('ascii'))
                dum+=1
            if(message2[0]=='dummyNo' and dum==1):
                c2.send(replydummy.encode('ascii'))  
                dum+=1          
            if(message1[0]=='know' and knowAns==1):
                print(str(addr1[1])+' knows the answer')
                knowAns+=1
                giveAns='please ans'
                cannotGiveAns='cannot ans'
                c1.send(giveAns.encode('ascii'))
                c2.send(cannotGiveAns.encode('ascii'))
            if(message2[0]=='know' and knowAns==1):
                print(str(addr2[1])+' knows the answer')
                knowAns+=1
                giveAns='please ans'
                cannotGiveAns='cannot ans'
                c2.send(giveAns.encode('ascii'))
                c1.send(cannotGiveAns.encode('ascii'))
            if(message1[0]=='y' and sub==0):
                message1=' '.join(message1[1:])
                print('Received answer: '+message1)
                if(message1=='correct answer'):
                    correct_msg_response='Correct!'
                    c1.send(correct_msg_response.encode('ascii'))
                    score1+=1
                else:
                    wrong_msg_response='Wrong!'
                    c1.send(wrong_msg_response.encode('ascii'))
                    score1-=0.5
                sub+=1
            if(message2[0]=='y' and sub==0):
                message2=' '.join(message2[1:])
                if(message2=='correct answer'):
                    correct_msg_response='Correct!'
                    print('Sent response successfully')
                    c2.send(correct_msg_response.encode('ascii'))
                    score2+=1
                else:
                    wrong_msg_response='Wrong!'
                    c2.send(wrong_msg_response.encode('ascii'))
                    score2-=0.5
                sub+=1
            # data = c.recv(1024) 
            # if not data: 
            #     print('Bye '+str(addr[1])) 
            #     #print_lock.release() 
            #     break
            # data = data[::-1] 
            # c.send(data) 
    c1.close()
    c2.close() 
  
  
def Main():
    host = "" 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(3) 
    print("socket is listening")
    global players 
    while True:
        c1, addr1 = s.accept() 
        c2, addr2 = s.accept()
        #print_lock.acquire()
        players+=2
        print('Connected to :', addr1[0], ':', addr1[1])
        print('connected to :', addr2[0], ':', addr2[1]) 
        start_new_thread(threaded, (c1,addr1,c2,addr2)) 
    s.close() 

Main()