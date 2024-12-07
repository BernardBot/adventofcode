seats = open("inputa.txt").readlines()
width = len(seats[0]) - 1
height= len(seats)

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
        a = x + i
        b = y + j
        while True:
            if a < 0 or b < 0 or a >= height or b >= width:
                break
            if seats[a][b] == 'L':
                break
            if seats[a][b] == "#":
                c += 1
                break
            a += i
            b += j
    
    if seat == "L" and c == 0:
        return "#"
    if seat == "#" and c >= 5:
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