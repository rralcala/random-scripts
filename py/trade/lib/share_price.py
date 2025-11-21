import datetime
from typing import Optional


class SharePrice:
    date: datetime.date
    open: float
    high: float
    low: float
    close: float
    volume: float
    adj_close: float

    def __str__(self):
        return (
            f"date:{self.date} open:{self.open} high:{self.close} volume:{self.volume}"
        )


def from_csv(line: str) -> Optional[SharePrice]:

    values = line.split(",")
    date_str = values[0].strip()
    ret = SharePrice()

    ret.date = datetime.date.fromisoformat(date_str)
    ret.open = float(values[1])
    ret.high = float(values[2])
    ret.low = float(values[3])
    ret.close = float(values[4])

    ret.volume = float(values[5])
    ret.adj_close = float(values[6].strip())

    return ret


if __name__ == "__main__":
    with open("../data/train/AAPL.rev.csv") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if len(line) < 10:
                continue
            share_price = from_csv(line)
            if share_price:
                print(share_price)
            else:
                print(line)
