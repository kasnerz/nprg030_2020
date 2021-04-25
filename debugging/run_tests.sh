PROGRAM="vypln_nazev_programu.py"
SLOZKA_S_TESTY="testy"

for FILE in "$SLOZKA_S_TESTY"/*.in; do
    echo $FILE

    python3 ./$PROGRAM <$FILE >vystup.txt

    diff vystup.txt ${FILE/in/out}
done