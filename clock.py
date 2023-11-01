#!/usr/bin/env python3
import argparse, datetime, random, time
import pytz
from mastodon import Mastodon
parser = argparse.ArgumentParser(description="run Crontime")
parser.add_argument("host", help="Host", type=str)
parser.add_argument("token", help="Token", type=str)
args = parser.parse_args()

class chatbot:
    def __init__(self,host="",token=""):
        self.host = Mastodon(
            access_token = token,
            api_base_url = host
        )
        print("Run: __init__()")
    def push(self,now_time):
        time_str = now_time.strftime("%Y-%m-%d %H:%M:%S %z")
        hour_int = int(now_time.strftime("%H"))
        run_hour_int = hour_int
        print(f"Bot.push({time_str})")

        small_msg = "woof~"
        large_msg = "WOOF!!!!!! WOOF!!!!!!\n"
        ear_list = ["V{}V","▼{}▼","U{}U","◖{}◗","(V{})","(▼{})","(U{})","(◖{})","({}V)","({}▼)","({}U)","({}◗)"]
        face_list = [" ● ᴥ ● "," ・ ᴥ ・ "," ´ ꓃ ` "," ^ ｪ ^ "," ⚆ ᴥ ⚆ ","´• ﻌ •`"," ❍ᴥ❍ "]

        emoji_msg = ""
        if hour_int == 0:
            woof_msg = F"[12AM midnight]\n"
        elif hour_int == 12:
            run_hour_int = run_hour_int - 12
            woof_msg = F"[12PM noon]\n{large_msg}"
        elif hour_int > 12:
            run_hour_int = hour_int - 12
            woof_msg = F"[{run_hour_int}PM]\n{large_msg}"
        else:
            woof_msg = F"[{hour_int}AM]\n"
        while run_hour_int > 0:
            run_hour_int = run_hour_int - 4
            if run_hour_int > 0:
                woof_msg = woof_msg + small_msg * 4 + "\n"
            else:
                woof_msg = woof_msg + small_msg * (4 + run_hour_int)
        now_str = now_time.strftime("%Y-%m-%d")
        random.seed(now_str)
        magic_int = random.choice(range(8,23))
        print(F"Magic number: {magic_int}")
        if hour_int == 0:
            self.host.status_post(woof_msg+F"\nMagic number: {magic_int}", visibility="public", spoiler_text="Magic are finding their way today! Woof!")
        elif hour_int == magic_int:
            self.host.status_post(woof_msg, visibility="public", spoiler_text=emoji_msg)
        else:
            self.host.status_post(woof_msg, visibility="public")

Bot = chatbot(host=args.host,token=args.token)
run = True
while run:
    now_time = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
    time_str = now_time.strftime("%Y-%m-%d %H:%M:%S %z")
    min_str = now_time.strftime("%M")
    sec_int = int(now_time.strftime("%S"))
    if min_str == "00":
        print(time_str)
        Bot.push(now_time=now_time)
        run = False
    elif sec_int < 50 and sec_int > 10:
        print(f"[{time_str}] Countdown... +60s")
        time.sleep(60)
    else:
        print(f"[{time_str}] Countdown... +10s")
        time.sleep(10)
