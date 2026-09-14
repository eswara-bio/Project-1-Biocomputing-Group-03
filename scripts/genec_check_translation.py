from Bio.Seq import Seq

with open("results/genec_cds.txt","r") as fh:
     cds = fh.read().strip()
s = Seq(cds)
print(s.translate())
