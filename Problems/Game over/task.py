scores = input().split()
C_count = 0
I_count = 0

for ans in scores:
    C_count += 1 if ans == "C" else 0
    I_count += 1 if ans == "I" else 0

    if I_count == 3:
        print("Game over", C_count, sep="\n")
        break
else:
    print("You won", C_count, sep="\n")
