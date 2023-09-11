#!/usr/bin/env python3
import time
import datetime
import pytz
run = True
while run:
    now_time = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
    time_str = now_time.strftime("%Y-%m-%d %H:%M:%S %z")
    min_str = now_time.strftime("%M")
    sec_int = int(now_time.strftime("%S"))
    if min_str == "00":
        print(time_str)
        run = False
    elif sec_int < 50 and sec_int > 10:
        print(f"[{time_str}] Countdown... +60s")
        time.sleep(60)
    else:
        print(f"[{time_str}] Countdown... +10s")
        time.sleep(10)
