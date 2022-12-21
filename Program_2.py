#counts the number of times a protein sequence repeats any amino acid and returns the results as a dictionary.

def count_amino_acids(protein_sequence):
    amino_acid_counts = {}
    for amino_acid in protein_sequence:
        if amino_acid in amino_acid_counts:
            amino_acid_counts[amino_acid] += 1
        else:
            amino_acid_counts[amino_acid] = 1
    return amino_acid_counts

protein = "MAFSAEDVLKEYDRRRRMEALLLSLYYPNDRKLLDYKEWSPPRVQVECPKAPVEWNNPPSEKGLIVGHFSGIKYKGEKAQASEVDVNKMCCWVSKFKDAMRRYQGIQTCKIPGKVLSDLDMKHLKK"
print(count_amino_acids(protein))