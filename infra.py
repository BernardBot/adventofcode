import os
import sys

def build_year(year):
    os.mkdir(year)
    os.chdir(year)

    for i in range(1, 26):
        day = "day" + str(i).zfill(2)
        os.mkdir(day)
        os.chdir(day)
        os.system(f"touch {day}a.py {day}b.py")
        os.system("touch inputa.txt inputb.txt")
        os.chdir("..")

if __name__ == "__main__":
    build_year(sys.argv[1])