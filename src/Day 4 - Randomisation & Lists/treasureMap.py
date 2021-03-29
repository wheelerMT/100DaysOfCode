row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to put the treasure? ")

map[int(pos[1]) - 1][int(pos[0]) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
