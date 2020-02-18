import os
import sys

#for each column

for lines in open('poolobject_162020.txt').readlines():
    if lines.startswith('"LUVX0"'):continue
    lines = lines.split('\t')
    #print(lines)
    scaffold=lines[1]
    position=lines[2]
    ref_allele=lines[3]
    alt_allele=lines[4]
    ancestral='-'

    #
    colorado_ref_count=lines[5]
    vancouver_ref_count=lines[6]
    oulanka_ref_count = lines[7]
    oulanka_ref_count=oulanka_ref_count.split("\n")[0]


    ###ALTERNATE ALLELE COUNT

    colorado_alt_count= 30 - int(colorado_ref_count)
    vancouver_alt_count = 30 - int(vancouver_ref_count)
    oulanka_alt_count = 30 - int(oulanka_ref_count)
    #print(alt_allele, scaffold, ref_allele, alt_allele, colorado_ref_count, colorado_alt_count, vancouver_ref_count, vancouver_alt_count)

    print("-" + ref_allele + "-" + "\t" + "-" + ancestral + "-" + "\t"+ref_allele + "\t" +str(colorado_ref_count) + "\t" +
          str(vancouver_ref_count) + "\t" + str(oulanka_ref_count) + "\t" +
          alt_allele + "\t" + str(colorado_alt_count) + "\t" + str(vancouver_alt_count) + "\t" + str(oulanka_alt_count) + "\t"+
          scaffold+"\t"+position)
