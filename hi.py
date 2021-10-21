rsidGenotype = {}

print(rsidGenotype)

#print(rsidGenotype.get('rs9283150'))

lines = []
with open('genome.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    if count>=21:
        stop = False
        tabs = 0
        rsid = ""
        genotype = ""
        for i in line: 
            if i == " " or i =="\t":
                stop = True
                if i == "\t":
                    tabs+=1
            if tabs==3:
                stop = False
            if stop==False and tabs<3:
                rsid += i
            if stop==False and tabs>=3:
                genotype += i
        if genotype[0]=="\t":
            genotype=genotype[1:-1]
        rsidGenotype[str(rsid)]= str(genotype)    
        #print(f'line {count}: {line}')
        #rsidGenotype['rs548049170']= 'TT'

import csv

pharmIdGen = []

with open("var_pheno_ann.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    counter = 0
    for line in tsv_file:
        counter+=1
        if counter>1:
            pharmIdGen.append([line[1], line[3], line[6], line[9]])

#print(pharmIdGen[0:10])
print("pharma list length:", len(pharmIdGen))



#it = rsidGenotype.get('rs9283150')
#itt = rsidGenotype['rs9283150']
#print("itt:", itt)

problematic = []

print(pharmIdGen[:10])

for x in pharmIdGen:
    id = x[0]
    geno = x[-1]
    significant = x[-2]
    myGeno = rsidGenotype.get(id)
    if geno == myGeno and significant=='yes': # for normal 2 letter allele
        problematic.append(x[1:-2])
    """ if len(geno)==1 and significant=='yes' and geno in myGeno: # for single letter allele
        problematic.append(x[1:-2])
    if "+" in geno:
        myAlleles = geno.split(" + ") """
    

        
print("\n\n\nproblematic:", problematic)

""" 
print("count:", count) 

first_n_pairs = list(rsidGenotype.items())[631976:631983] # [:5] = first 5;   [631976:631983] = last 7

# for key,value in first_n_pairs:
#     print(key, ':', value)

print("length of dict:", len(rsidGenotype)) 

#print(rsidGenotype)
#print(rsidGenotype.get('rs9283150'))

""" 


