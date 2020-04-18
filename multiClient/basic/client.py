import socket 

def Main(): 
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port))  
    start=0
    questions=1
    sub=1
    dummy='dummy'
    while True:
        if(start==0):
            message='Ready!' 
            s.send(message.encode('ascii')) 
            start+=1
        data = s.recv(1024).decode('ascii').split(' ') 
        if(start==1):
            print('Received from the server : '+ str(data[0] + " "+str(data[1]))) 
            message='ok'
            s.send(message.encode('ascii'))
            start+=1
        if(data[0]=='Q1' and questions==1 and sub==1):
            data=' '.join(data)
            print(data)
            reply=raw_input('\nDo you know the correct answer for it?(y or n): ')
            if(str(reply)=='y'):
                know='know'
                sub+=1
                #restrictOther='restrict'
                s.send(know.encode('ascii'))
            elif(str(reply)=='n'):
                # dontKnow='dontKnow'
                # s.send(dontKnow.encode('asccii'))
                dummyNo='dummyNo'
                s.send(dummyNo.encode('ascii'))
                print('Wait for next question')
                sub+=2
                questions+=1
            #     restrict_other='restrict'
            #     s.send(restrict_other.encode('ascii'))
            #     if data[0]!='cannot':
            #         answer=raw_input('\nGive your answer : ')  #raw_input stores as string, so again don't convert it into a string
            #         answer='y '+answer
            #         s.send(answer.encode('ascii'))
            # elif(str(reply)=='n'):
            #     print('wait for next question!')
        
        # if(data[0]=='cannot'):
        #     print('You lost chance to answer this question') 
        if(data[0]=='replydummy'):
            s.send(dummy.encode('ascii'))
        if(data[0]=='please' and data[1]=='ans' and sub==2):
            answer=raw_input('\nGive your answer : ')  #raw_input stores as string, so again don't convert it into a string
            answer='y '+answer
            s.send(answer.encode('ascii'))
            print('\nSent your answer for verification!')
            sub+=1
        elif(data[0]=='cannot' and data[1]=='ans' and sub==2):
            print('You are late!! You lost chance to answer this question') 
            print('Wait for next question..')
            s.send(dummy.encode('ascii'))
            sub+=1
        if(data[0]=='Correct!' and sub==3):
            print('Correct Answer!!')
            sub+=1
        elif(data[0]=='Wrong!' and sub==3):
            print('Wrong Answer!!')
            sub+=1
        # ans = input('\nDo you want to continue(y/n) :') 
        # if ans == 'y': 
        #     continue
        # else: 
        #     break
    s.close()

Main()