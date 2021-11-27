f = open("inputa.txt").read()

req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

c = 0
for p in f.split("\n\n"):
    fields = set(x.split(":")[0] for x in p.split())

    if req_fields <= fields:
        c += 1

print(c)
