import csv

col = 10
blank = 4


arr = [[""]*(col*blank) for i in range(600000)]
setting = [[""]*8 for i in range(27)]
Num = 0

for num in range(1,10):
    for i in range(0, col):
        for j in range(0, 10):
            try:
                #읽을파일
                rname= "Graph"+str(num)+"_Wave_Tshort_00" + str(i) + str(j) + ".csv"
                print(rname)
                rf = open(rname)
                Num = num
            except Exception as E:
                #파일이 없을시 종료
                print(E)
                continue
            reader = csv.reader(rf, delimiter=',')
            reader = list(reader)
            if i==0 and j==0:
                for k in range(0,27):
                    setting[k] = reader[k]
            for k in range(27, 60027):
                arr[k-27 + j*60000][i*blank +1] = reader[k][1]
f = open('Graph'+str(Num)+'_Wave_Tshort.csv', 'w', encoding='utf-8', newline='')
wf = csv.writer(f)

    
for i in range(0, 27):
    wf.writerow(setting[i])
for i in range(0, 600000):
    wf.writerow(arr[i])
