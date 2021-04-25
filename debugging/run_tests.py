#!/usr/bin/env python3

import os

# TODO vyplnit název programu
muj_program = "z.klasifikator.py"
slozka_s_testy = "klasifikator"

for file in sorted(os.listdir(slozka_s_testy)):
    if file.endswith(".in"):
        file_path = os.path.join(slozka_s_testy, file) # řeší správná lomítka podle OS
        print(file_path)
        os.system(f"python3 {muj_program} <{file_path} > vystup.txt")

        with open("vystup.txt", "r") as out_program, open(file_path.replace(".in", ".out"), "r") as out_ref:
            for i, (line_program, line_ref) in enumerate(zip(out_program, out_ref)):
                if line_program != line_ref:
                    print(f"Rozdíl na řádku {i}")
                    print("+", line_program, end="")
                    print("-", line_ref,  end="")
                    print()