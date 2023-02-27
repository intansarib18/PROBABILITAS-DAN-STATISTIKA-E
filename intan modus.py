print("MENGHITUNG NILAI MODUS")

from collections import Counter
data = [0, 2, 2, 1, 0, 7, 1]
no = len(data)
val = Counter(data)
nilaimodus = dict(val)
modus = [i for i, v in nilaimodus.items() if v == max(list(val.values()))]  
if len(modus) == no:
    nilaiModus = "DATA TIDAK MEMILIKI MODUS"
else:
    nilaimodus = "NILAI MODUS DARI DATA NIM ADALAH : " + ', '.join(map(str, modus))
print(nilaimodus)