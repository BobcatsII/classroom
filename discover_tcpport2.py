#!/usr/bin/python
import os
import json
import commands

data = {}
port_list = []
command = "netstat -ntlp|grep tcp|awk '{print $4}'|awk -F':' '{print $NF}'| sort -nr| uniq"
str1 = commands.getoutput(command)
ports = str1.split('\n')
for port in ports:
    port_dict = {}
    port_dict['{#TCP_PORT}'] = port 
    command2 = "netstat -ntlp|grep ':%s '|awk '{print $7}'|awk -F'/' '{print $NF}'|uniq" %port
    str2 = commands.getoutput(command2)
    if str2 != 'java':
        procs = str2.split('\n')
        for proc in procs:
            port_dict.setdefault('{#TCP_PROC}', proc)
            port_list.append(port_dict)
    elif str2 == 'java':
        listdir1 = os.listdir('/usr/local/tomcat')
        for i in listdir1:
            if i == '0':
                listdir2 = os.listdir('/usr/local/tomcat/%s' %i)
                command3 = "netstat -ntlp|grep ':%s '|awk '{print $7}'|awk -F'/' '{print $1}'|uniq" %port
                pid1 = commands.getoutput(command3)
                for j in listdir2:
                    command5 = "ps aux |grep ' %s '|grep -v grep" %pid1
                    str4 = commands.getoutput(command5)
                    if j in str4:
                        port_dict.setdefault('{#TCP_PROC}', j)
                        port_list.append(port_dict)
            elif i != '1' and i != '0':
                command4 = "netstat -ntlp|grep ':%s '|awk '{print $7}'|awk -F'/' '{print $1}'|uniq" %port
                pid2 = commands.getoutput(command4)
                command6 = "ps aux |grep ' %s '|grep -v grep" %pid2
                str5 = commands.getoutput(command6)
                if i in str5:
                    port_dict.setdefault('{#TCP_PROC}', i)
                    port_list.append(port_dict)


        listdir3 = os.listdir('/usr/local')
        listdir3.remove('tomcat')
        for k in listdir3:
            if len(k) > 3 and k != 'jdk1.8' and k != 'admin*' and k != "clr-service" :
                lst = []
                lst.insert(0, k)
                lst1 = str(lst[0]).split(',')
                for m in lst1:
                    command7 = "netstat -ntlp|grep ':%s '|awk '{print $7}'|awk -F'/' '{print $1}'|uniq" %port
                    pid3 = commands.getoutput(command7)
                    command8 = "ps aux |grep ' %s '|grep -v grep" %pid3
                    str8 = commands.getoutput(command8)
                    if m in str8:
                        port_dict.setdefault('{#TCP_PROC}', k)
                        port_list.append(port_dict)
        
data['data'] = port_list
jsonStr = json.dumps(data, sort_keys=True, indent=4)
print jsonStr
