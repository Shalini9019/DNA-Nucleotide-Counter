\# DNA Nucleotide Counter



A beginner bioinformatics project written in Python to count the nucleotides A, T, G, and C in a DNA sequence.



\## Data Source



The DNA sequence used in this project was obtained from NCBI in FASTA format.



\- Organism: \*Escherichia coli\*

\- NCBI accession: J01636.1

\- Description: \*E. coli\* lactose operon with lacI, lacZ, lacY and lacA genes

\- Sequence length: 7,477 nucleotides



\## Results



The Python script counted each nucleotide in the 7,477-nucleotide DNA sequence.



| Nucleotide | Count |

|------------|------:|

| A | 1,739 |

| T | 1,743 |

| G | 2,004 |

| C | 1,991 |

| \*\*Total\*\* | \*\*7,477\*\* |



The sum of A, T, G, and C equals the total sequence length, confirming that the nucleotide counts are consistent.



\## How It Works



The program:



1\. Opens the FASTA file containing the DNA sequence.

2\. Reads the sequence into Python.

3\. Removes the FASTA header.

4\. Removes line breaks from the DNA sequence.

5\. Counts the occurrences of A, T, G, and C.

6\. Calculates the total sequence length.

7\. Checks that the nucleotide counts add up to the total length.



\## Requirements



\- Python 3

\- A computer with a terminal or PowerShell



\## How to Run



1\. Download or clone this repository.

2\. Make sure `dna\_counter.py` and `sequence.fasta` are in the same folder.

3\. Open PowerShell or a terminal in the project folder.

4\. Run:



```bash

python dna\_counter.py



\## Skills Used



\- Python programming

\- Reading FASTA files

\- DNA sequence processing

\- String manipulation

\- Nucleotide counting

\- Basic data validation

\- Introduction to bioinformatics

