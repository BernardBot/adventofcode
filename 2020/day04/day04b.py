f = open("inputb.txt").read()

req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

c = 0
for p in f.split("\n\n"):
    fields = dict(x.split(":") for x in p.split())

    if not fields.keys() >= req_fields:
        continue
    
    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        continue

    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        continue

    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        continue
    
    hgt = fields["hgt"]
    if hgt.endswith("cm"):
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            continue
    elif hgt.endswith("in"):
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            continue
    else:
        continue
    
    hcl = fields["hcl"]
    if hcl.startswith("#") and len(hcl) == 7:
        hcl = hcl[1:]
        if set(hcl) > set("0123456789abcdef"):
            continue
    else:
        continue

    ecl = fields["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    pid = fields["pid"]
    if len(pid) != 9 or not pid.isdigit():
        continue

    c += 1

print(c)
