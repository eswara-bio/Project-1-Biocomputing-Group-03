# Biocomputing (BE623) — Project 1

## Project Overview

This project involves retrieval, processing, translation, and comparison of nucleotide and protein sequences obtained from the NCBI database. Three genes representing different biological categories were analysed.

## Steps Performed
1. Selected one gene from each assigned category.
2. Searched the NCBI Nucleotide database for the selected gene.
3. Refined the search to obtain the human RefSeq mRNA record.
4. Downloaded the mRNA sequence in FASTA format.
5. Downloaded the  GenBank and recorded the accession, organism, CDS coordinates, and protein ID.
6. Used the protein ID to retrieve the corresponding deposited protein sequence in FASTA format.
7. Extracted FASTA header lines from the downloaded files.
8. Extracted the CDS from the mRNA sequence using the GenBank CDS coordinates.
9. Checked the CDS length and its divisibility by 3.
10. Translated the CDS using the appropriate genetic code.
11. Compared the translated protein sequence with the deposited protein sequence.
12. Identified if any, first mismatch, where applicable and cross-checked the translation using Biopython.
13. Developed a Python pipeline to perform the analysis for all three genes.
14. Generated a single summary table containing the results for all three genes.

## Commands and tools used

| Purpose                         |  Command                    |
| ------------------------------- | ----------------------------|
| Retrieve NCBI sequences         | NCBI E-utilities / `efetch` |
| Extract FASTA headers           | `grep`                      |
| Sequence processing             | Python (.py)                |
| Protein translation cross-check | Biopython                   |
| Python environment              | miniconda3 (conda)          |
| Coding                          | Jupyter Notebook            |
 

## Team members and respective gene

| Team Member      | Category            | Gene   |
| -----------      | -----------------   | ------ |
| Eswara G R       | Selenoprotein (A)   | SEPHS2 |
| Srajan Dehariya  | Mitochondrial (B)   | MT-ND3 |
| Balapravena A S  | Nuclear control (C) | PPIB   |

Note: The complete gene piple line is in scripts/gene_pipeline.py, while the script processes all three genes and generates output in results/summary_table.csv
