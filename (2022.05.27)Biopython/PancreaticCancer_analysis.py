from Bio.Data import CodonTable

record = SeqIO.read("/content/drive/MyDrive/(22.05.27)과학탐구교실/pancreatic_cancer.fasta", "fasta")
seq = record.seq

print("아미노산의 수 : ", len(seq)/3)

# CRISPR-Cas9
s, e = 0, 9 # 자르는 구간 설정 [start, end)
print("\nCRISPR-Cas9 : ", end="")
t = 0
for i in range(s, e):
  print(seq[i], end="")
  if t==2 : print(" ", end="")
  t += 1
  t %= 3
print("\n")

# 전사

# DNA = ['T', 'G', 'C', 'A']
# RNA = ['A', 'C', 'G', 'T']

print("RNA : ", end="")
for i in range(s, e) :
  if str(seq[i])=='T': print('A', end="")
  elif str(seq[i])=='G': print('C', end="")
  elif str(seq[i])=='C': print('G', end="")
  elif str(seq[i])=='A': print('T', end="")
print("\n")

print(CodonTable.unambiguous_dna_by_name['Standard'])
