scores = input().split()
C_count = 0
I_count = 0

for ans in scores:
    if ans == "C":
        C_count += 1
    if ans == "I":
        I_count += 1
    if I_count == 3:
        print("Game over", C_count, sep="\n")
        break
else:
    print("You won", C_count, sep="\n")
