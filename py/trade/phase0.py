import os

from file_read_backwards import FileReadBackwards


class Phase0:
    def __init__(self, file_path):
        self.file_path = file_path

    def reverse(self) -> str:

        new_path = "." + self.file_path.split(".")[1] + ".rev.csv"
        with FileReadBackwards(self.file_path, encoding="utf-8") as frb:
            c = 0
            with open(new_path, "w") as out:
                while True:
                    line = frb.readline().strip()
                    if not line:
                        break
                    if line[:4] == "Date" or line == "":
                        continue

                    out.write(line + os.linesep)
                    c += 1
                    print(c)
        return new_path


if __name__ == "__main__":
    print(Phase0("./data/train/AAPL.csv").reverse())
