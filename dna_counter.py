# Read the DNA sequence from the FASTA file
with open("sequence.fasta", "r") as file:
     sequence = file.read()

# Remove the FASTA header and line breaks
sequence = sequence.split("\n", 1)[1]
sequence = sequence.replace("\n", "")

# Count the total length and each nucleotide
print("Total:", len(sequence))
print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))