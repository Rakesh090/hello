from csv import writer,reader

#writer function
def write1():
    f= open('result.csv','w')
    wfile=writer(f)
    #f.write('rakesh')
    row_list=[]
    wfile.writerow(['Sno.','Name','H','E','P','C','M'])
    for i in range(1,11):
        name=input('Enter your name')
        h=input('Enter your sub no=')
        e=input('Enter your sub no=')
        p=input('Enter your sub no=')
        c=input('Enter your sub no=')
        m=input('Enter your sub no=')
        wfile.writerow([i,name,h,e,p,c,m])

        
#reader function
#def readr():
f= open('result.csv','r')
rfile=reader(f)
result=[]
for line in rfile:
    result.append(line)
    
#result_pre=[]
#make result_pre.csv file and append name and percentage
f=open('result_pre.csv','w')
pre_file=writer(f)
for i in range(1,len(result)):
    name=result[i][1]
    h=int(result[i][2])
    e=int(result[i][3])
    p=int(result[i][4])
    c=int(result[i][5])
    m=int(result[i][6])
    pre=((h+e+p+c+m)*100)/500
    pre_file.writerow([i,name,pre])
f.close()
    
    
#Read result_pre.csv file 
f= open('result_pre.csv','r')
rfile=reader(f)
result_pre=[]
for line in rfile:
    result_pre.append(line)

#Find topper from result_pre.csv file 
max=result_pre[0][2]
min=result_pre[0][2]
topper=[]
lscore=[]
for i in range(0,len(result_pre)):
    # Cheak topper list
    if result_pre[i][2]>max:
        max=result_pre[i][2]
        topper=[i]
    elif max==result_pre[i][2]:
        topper.append(i)
    # Cheak low Scorer list
    elif result_pre[i][2]<min:
        min=result_pre[i][2]
        lscore=[i]
    elif min==result_pre[i][2]:
        lscore.append(i)

#topper append line
for i in topper:
    result_pre[i].append('Topper')
for i in lscore:
    result_pre[i].append('LowScorer')
f= open('result_pre.csv','w')
for x in result_pre:
    f.write(','.join(map(str,x))+'\n')
    
    
#Find subject topper list and low Scorer

f=open('result.csv','r')
rfile=reader(f)
result=[]
for line in rfile:
    result.append(line)

max=0
topper=[]
sub=[]


for i in range(2,len(result[0])):
    for j in range(1,len(result)):
        if int(result[j][i])>max:
            max=int(result[j][i])
            topper=[j]
        elif int(result[j][i])==max:
            topper.append(j)
            sub.append(i)
print(topper)
print(sub)
