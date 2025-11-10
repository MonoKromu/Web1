from datetime import datetime

import schedule


def run_kukushka():
    hour = datetime.now().hour
    repeats = hour % 12
    if repeats == 0:
        repeats = 12
    print(("Ку " * repeats))


schedule.every(1).hour.at(":00").do(run_kukushka)
while True:
    schedule.run_pending()
