import pandas as pd
import csv
import re
import string


list = pd.read_csv('/cusustomerlist.csv',engine='python')

## Proper case and remove common endings
##removal_list = [" Llc"," L.l.c."," L.p.","Inc."," Limited$"," Lp$"," Co."," L.t.d."," Ltd."," Ltd$"," Llc$"," Lp$"]
##removal_list = [" Llc"," L.l.c."," L.p.","Inc."," Limited$"," Lp$"," Co."," L.t.d."," Ltd."," Ltd$"," Llc$"," Lp$"]
 ##for r in removal_list:                 
                    ##list.loc[i ,'LEGAL_NAME']= re.sub( r, '', list.loc[i ,'LEGAL_NAME'])
##for r in removal_list:                 
                    ##list.loc[i ,'LEGAL_NAME']= re.sub( r, '', list.loc[i ,'LEGAL_NAME'])
               ##list.loc[i ,'LEGAL_NAME'] = string.capwords(list.loc[i ,'LEGAL_NAME']) USE fnmatch.filter Case is no longer important                    
def rmv(rq,l):
    result = re.sub(str('\s' + rq +'$'),'', l)
    return result
for s in list.loc[i ,'LEGAL_NAME']:
     for q in [" Llc"," L.l.c."," L.p.","Inc."," Limited$"," Lp$"," Co.", " Ltd."," Ltd$"," Llc$"," Lp$"]:   
            try:
                rmv(rq = q , l = s)

for i in range(0,list.shape[0]):
    list.loc[i ,'LEGAL_NAME'] = list.loc[i ,'LEGAL_NAME'].strip()
               
               ## Wildcard for . to make better pattern. . should be removed in the EE list
for t in [".","-"]:
    list.loc[i ,'LEGAL_NAME'] = list.loc[i ,'LEGAL_NAME'].replace(t,"*")
for q in ["(",")",","]:
    list.loc[i ,'LEGAL_NAME'] = list.loc[i ,'LEGAL_NAME'].replace(q,"")

myEE= pd.read_csv('/Entilitylist.csv',engine='python')

for i in range(0,myEE.shape[0]):
               myEE.loc[i,'EntityName'] = myEE.loc[i,'EntityName'].strip()
               ##for r in removal_list:                 
                    ##myEE.loc[i,'EntityName']= re.sub( r, '', myEE.loc[i,'EntityName'])
               ##list.loc[i ,'LEGAL_NAME'] = string.capwords(list.loc[i ,'LEGAL_NAME'])
               for q in ["(",")",",",".","-"]:
                    myEE.loc[i,'EntityName'] = myEE.loc[i,'EntityName'].replace(q,"")

for i in list.loc[:,'LEGAL_NAME']:
    inputstr=i
    count = len(re.findall(r'\w+', inputstr))
    if count < 3:
         sub = i
    elif count <5:
         words = inputstr.split()
         secondwords = iter(words)
         next(secondwords)
         sub0=[' '.join((first, second)) for first, second in zip(words, secondwords)]
         sub2 = sub0
         for i in sub0:
                   if i.lower() in frequent_substring_list:
                        sub2.remove(i)     
         sub=[i]
       
         for i in sub2[:2]:
                    sub.append(i)           
    else:
         sub1=[]
         long=i.split()
         for w in range(0, len(long)-2) :
                long1=[' '.join((long[w],long[w+1],long[w+2]))]
                sub1.append(long1)
         sub=[i,"*"+i[3:-6].strip()+"*"]
         for i in sub1[:3]:
                    sub.append(i)

    print(sub)     
   
###frequent_substring_list is list created to show the substring frequency. 
###From my experimentation, if the TF(term frquency) of one substring is more than 5 times, we cannot use this part to do fuzzy matching####
        

cw=open("/outcome.csv",'w',encoding='utf-8')
cw_csv = csv.writer(cw)
output = []
for i in list.loc[:,'LEGAL_NAME']:
    inputstr=i
    count = len(re.findall(r'\w+', inputstr))
    if count < 3:
         sub = i
    elif count <5:
         words = inputstr.split()
         secondwords = iter(words)
         next(secondwords)
         sub0=[' '.join((first, second)) for first, second in zip(words, secondwords)]
         sub2= [sub0.remove(i) if i.lower() in frequent_substring_list]
         sub=[i]
         for i in sub2[:2]:
                    sub.append(i)           
    else:
         sub1=[]
         long=i.split()
         for w in range(0, len(long)-2) :
                long1=[' '.join((long[w],long[w+1],long[w+2]))]
                sub1.append(long1)
         sub=[i,"*"+i[3:-6]+"*"]
         for i in sub1[:3]:
                sub.append(i)   
   

   
    if count>=5:
        matching = fnmatch.filter(myEE.loc[:,'EntityName'], sub[0])
        matching.append(fnmatch.filter(myEE.loc[:,'EntityName'], sub[1]))
    else:       
         matching = fnmatch.filter(myEE.loc[:,'EntityName'], sub[0])   
         if len(matching)>0:
               current=set(matching[:4])
         else:
               current=set()
               for pattern in sub:
                    pattern=pattern.replace("*","")
                    for entity in myEE.loc[:,'EntityName']:
                         if pattern.lower() in entity.lower():
                                 if len(matching) < 4:   
                                       current.add(entity)
                                       
    ##cw.write('\t'.join([str(x) for x in current ])+'\n')
    print(current)
    output.append(current)
cw_csv.writerows(output)
cw.close()

for i in list.loc[:,'LEGAL_NAME']:
    inputstr=i
    count = len(re.findall(r'\w+', inputstr))
    if count < 3:
         sub = i
    elif count <5:
         words = inputstr.split()
         secondwords = iter(words)
         next(secondwords)
         sub0=[' '.join((first, second)) for first, second in zip(words, secondwords)]
         sub2=sub0
         for i in sub0:
                   if i.lower() in frequent_substring_list:
                       sub2.remove(i)     
         sub=[i]
         for i in sub2[:2]:
                    sub.append(i)           
    else:
         sub1=[]
         long=i.split()
         for w in range(0, len(long)-2) :
                long1=[' '.join((long[w],long[w+1],long[w+2]))]
                sub1.append(long1)
         sub=[i,"*"+i[3:-6]+"*"]
         for i in sub1[:3]:
                sub.append(i)   
    print(sub)




   