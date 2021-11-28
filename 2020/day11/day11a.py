seats = open("inputa.txt").readlines()
width = len(seats[0]) - 1
height= len(seats)

print(width, height)

neighbors = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1,1),
]
def update_seat(x, y, seats):
    seat = seats[x][y]

    c = 0

    for i, j in neighbors:
        if x + i < 0 or y + j < 0 or x + i >= height or y + j >= width:
            continue
        # print(x + i, y + j)
        # print(len(seats), len(seats[0]))
        # print(len(seats[x + i]))
        # print(seats[x + i])
        c += seats[x + i][y + j] == "#"
    
    if seat == "L" and c == 0:
        return "#"
    if seat == "#" and c >= 4:
        return "L"
    else:
        return seat

def update(seats):
    new_seats = []
    for i in range(height):
        new_seats.append([])
        for j in range(width):
            new_seats[i].append(update_seat(i, j, seats))
    return new_seats


new_seats = update(seats)
while seats != new_seats:
    seats = new_seats
    new_seats = update(seats)

print("\n".join(map(lambda s: "".join(s), new_seats)).count("#"))