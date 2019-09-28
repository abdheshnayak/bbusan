import os
os.system('clear')
try:
    import urllib.request
except:
    print('installing components: urllib')
    os.system('pip install urllib')
    import urllib.request
try:
    import sqlite3 as sq
except:
    print('installing component: sqlite3')
    os.system('pip install sqlite3')
    import sqlite3 as sq
try:
    import requests
except:
    print('installing component: requests')
    os.system('pip insall requests')
    import requests

st=''
def ex(str1,st):
    #print(str1)
    f=open("DATA/temp.py",'w')
    f.write(str1);
    f.close()
    #print("lskdflajseifa")
    os.system('python DATA/temp.py')

def internet_on():
    try:
        urllib.request.urlopen('http://google.com',timeout=1)
        return True
    except Exception as e:
        print ('\nI have facing Dificult To connect With Server\n\nPlease Report This Error To Adimin: ',e)
    except urllib.request.URLError as err:
        return False

print("\nWelcome Sir I am Bbusan. I am Always Ready To Help You..?")
while(st!='exit' and st!='close' and st!='bye'):
    flt='''import sqlite3\ncon1 = sqlite3.connect('DATA/fault.db')\ncon1.execute("INSERT INTO FAULT (CMD) VALUES ('''
    if(os.path.exists('DATA/query.db') and st!='update'):
        conn = sq.connect('DATA/query.db')
        cursor = conn.execute("SELECT PRG_CMD,CMD,NOT_CMD,NAME,IDD from INF")
        #flt='''import sqlite3\ncon1 = sqlite3.connect('f/DATAault.db')\ncon1.execute("INSERT INTO FAULT (CMD) VALUES ('''
        st=input('\nBBUSAN\nPlease Say My Task: ')
        sts=st.lower()
        if('?' in st):
            sts=sts.replace('?','')

        f1=open('DATA/tempdata.txt','w')
        f1.write(st)
        f1.close()
        temp=sts.split()
        flag=0
        cnt=len(temp)
        cursor = conn.execute("SELECT PRG_CMD,CMD,NOT_CMD,NAME,IDD from INF")
        for row in cursor:
            if(cnt>3):
                if sts in row[1] and sts not in row[2]:
                    ex(row[0],sts)
                    flag=1
                    break
            else:
                if temp[0] in row[1] and temp[0] not in row[2]:
                    ex(row[0],sts)
                    flag=1
                    break

        if flag==0:
            print("I Have To Dificult To UnderStand You??\n\n Please Use Help Manual=>=> By Just Typing 'Help'")
            if(os.path.exists('DATA/fault.db')):
                flt=flt+"'"+st+"'"+')")\ncon1.commit()\ncon1.close()'
                ex(flt,sts)
            else:
                fltt='''import sqlite3\ncon1 = sqlite3.connect('DATA/fault.db')\ncon1.execute("CREATE TABLE FAULT (CMD CHAR(50))")\ncon1.close()'''
                ex(fltt,sts)
    else:
        if(internet_on()==True):
            if(os.path.exists('DATA/query.db')):
                pass
            else:
                os.system('mkdir DATA')
            print('\tUpdating',end='\r')
            if(st=='update'):
                os.system('rm DATA/query.db')
            else:
                fltt='''import sqlite3\ncon1 = sqlite3.connect('DATA/fault.db')\ncon1.execute("CREATE TABLE FAULT (CMD CHAR(50))")\ncon1.close()'''
                ex(fltt,st)
            print("\n\n\tconnected\n\nPlease Wait Few Seconds While I Am Being Updating\n\n\n")
            conn = sq.connect('DATA/query.db')
            crt='''import sqlite3\nconn=sqlite3.connect('DATA/query.db')\nconn.execute("CREATE TABLE INF (PRG_CMD CHAR(400),CMD CHAR(300),NOT_CMD CHAR(300),NAME CHAR(20) PRIMARY KEY,IDD NUMBER)")\nconn.close()'''
            ex(crt,st)
            conn.close()
            # api-endpoint
            URL = "https://api-euwest.graphcms.com/v1/cjuelu4vk15dq01dqmsvwkc9y/master"

            # location given here

            # defining a params dict for the parameters to be sent to the API
            PARAMS = {'query':'query{datas{prgCmd,cmd,notCmd,name,idd}}'}
            try:
                r = requests.post(url = URL, params = PARAMS)
                r.raise_for_status()
            except r.codes as e:  # This is the correct syntax
                print ("e")
                pass

            # extracting data in json format
            data = r.json()
            #print(data)
            n=len(data['data']['datas'])
            for i in range(n):
                insrt='''import sqlite3\ncon1 = sqlite3.connect('DATA/query.db')\ncon1.execute(''\'INSERT INTO INF (PRG_CMD,CMD,NOT_CMD,NAME,IDD) VALUES ('''+'"'+data['data']['datas'][i]['prgCmd']+'"'+','+'"'+data['data']['datas'][i]['cmd']+'"'+','+'"'+data['data']['datas'][i]['notCmd']+'"'+','+'"'+data['data']['datas'][i]['name']+'"'+','+str(data['data']['datas'][i]['idd'])+")''')\ncon1.commit()\ncon1.close()"
                ex(insrt,st)
                x=round(((i+1)/n)*80)
                print('Updating ',x,' % Completed',end='\r')
                # print(data['data']['helloes'][i]['command'])

            conf=sq.connect('DATA/fault.db')
            URL = "https://api-euwest.graphcms.com/v1/cjue3w4uu0cez01dqr98ahjjk/master"
            cursor = conf.execute("SELECT CMD from FAULT")
            j=0
            for row in cursor:
            #        print(row[0])
                j+=j
                x=80+(j-(j/0.6))
                x=round(x)
                print('\rUpdating ',x,' % Completed',end='\r')
                PARAMS = {'query':'mutation{createHello(data:{command:"'+row[0]+'"}){id command}}'}
                try:
                    r = requests.post(url = URL, params = PARAMS)
                    r.raise_for_status()
                except r.codes as e:  # This is the correct syntax
                    print ("Error Occuered Please Contact To Admin")
                    pass
            fltt='''import sqlite3\nimport os\nos.system('rm DATA/fault.db')\ncon1 = sqlite3.connect('DATA/fault.db')\ncon1.execute("CREATE TABLE FAULT (CMD CHAR(50))")\ncon1.close()'''
            ex(fltt,st)
            print('\rUpdating 100 % Completed\n')
            print("Now I Am Up To Date")
        else:
            print("Please Check Your Connection")
        st=''
