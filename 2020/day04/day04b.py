f = open("inputb.txt").read()

def valid(fields):
    if not fields.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        return False
    
    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False
    
    hgt = fields["hgt"]
    if hgt.endswith("cm"):
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            return False
    elif hgt.endswith("in"):
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False
    
    hcl = fields["hcl"]
    if hcl.startswith("#") and len(hcl) == 7:
        hcl = hcl[1:]
        if set(hcl) > set("0123456789abcdef"):
            return False
    else:
        return False

    ecl = fields["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = fields["pid"]
    if len(pid) != 9 or not pid.isdigit():
        return False

    return True

c = 0
for p in f.split("\n\n"):
    fields = dict(x.split(":") for x in p.split())
    if valid(fields):
        c += 1

print(c)
