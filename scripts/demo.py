import pandas as pd
from Bio.Seq import Seq

seq = Seq("ATGCGTACGTAGCTAGCTAGCTA")
print("Original sequence:      ", seq)
print("Reverse complement:     ", seq.reverse_complement())

df = pd.DataFrame(
    {
        "gene": ["BRCA1", "TP53", "EGFR"],
        "expression": [12.3, 45.6, 7.8],
    }
)
print(df)
