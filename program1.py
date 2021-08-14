import csv
import statistics as st
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    n_num = fileData[i][1]
    newData.append(float(n_num)) 

mean = st.mean(newData)
print(mean)

median = st.median(newData)
print(median)

mode = st.mode(newData)
print(mode)