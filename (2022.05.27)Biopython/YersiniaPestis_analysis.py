import numpy as np
import collections
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

record = SeqIO.read("/content/drive/MyDrive/(22.05.27)과학탐구교실/Yersinia_pestis.fasta", "fasta")
seq = record.seq

print("\n염기서열 : ", end="")
for s in seq :
  print(s, end="")
print("\n")

d = [0 for _ in range(5)]

for s in seq :
  if(str(s)=='A') : d[0] += 1
  elif(str(s)=='T') : d[1] += 1
  elif(str(s)=='G') : d[2] += 1
  elif(str(s)=='C') : d[3] += 1

dt = [(d[0], 'A'), (d[1], 'T'), (d[2], 'G'), (d[3], 'C')]
dt = sorted(dt, key=lambda dt : dt[0], reverse=True)

print('염기  |  염기의 수  |  포함된 비율')
for i in range(0, 4) :
  print(dt[i][1], dt[i][0], format((dt[i][0]/len(seq))*100, '.3f'), sep='          ', end='%\n')

r = str(seq)

print()
print("구아닌의 수 | 시토신의 수")
print("    ", end="")
print(r.count("G"), r.count("C"), sep="         ")
print()
print("GC contents : ", format((((r.count("G")+r.count("C"))/len(r))*100), '.3f'))
