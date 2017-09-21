#!/usr/bin/python

import subprocess
import json
import os.path

def dl(server, match):
    ret = subprocess.call(["rsync", "-r", server + ":/root/mapc/tournament/replays/" + match + "-Sim1", "./replays/"])
    assert ret == 0
    ret = subprocess.call(["rsync", "-r", server + ":/root/mapc/tournament/replays/" + match + "-Sim2", "./replays/"])
    assert ret == 0
    ret = subprocess.call(["rsync", "-r", server + ":/root/mapc/tournament/replays/" + match + "-Sim3", "./replays/"])
    assert ret == 0

    def n(number):
        return "{:,}".format(number).replace(",", " ")

    def nobreak(s):
        return s.replace(" ", "&nbsp;").replace("-", "&#8209;")

    result = []
    score_a = 0
    score_b = 0
    for sim in ["-Sim1", "-Sim2", "-Sim3"]:
        with open(os.path.join("replays", match + sim, "995.json")) as f:
            o = json.load(f)["999"]["teams"]
            if not result:
                result.append("{} vs. {}".format(nobreak(o[0]["name"]), nobreak(o[1]["name"])))

            if o[0]["money"] == o[1]["money"]:
                assert False # draw not implemented
            elif o[0]["money"] > o[1]["money"]:
                col = "**{}** : {}".format(n(o[0]["money"]), n(o[1]["money"]))
                score_a += 3 if o[0]["money"] > 50000 else 2
            else:
                col = "{} : **{}**".format(n(o[0]["money"]), n(o[1]["money"]))
                score_b += 3 if o[1]["money"] > 50000 else 2

            result.append("[{}]({})".format(nobreak(col), "/2017/replays/?" + match + sim))

    result.append("{} : {}".format(score_a, score_b))

    print(" | ".join(result))

# Tuesday
#dl("ac1", "2017-09-19-14-03-51-2017-MAPC")
#dl("ac2", "2017-09-19-14-03-31-2017-MAPC")
#dl("ac1", "2017-09-19-16-05-45-2017-MAPC") # Flisvos vs Chameleon
#dl("ac2", "2017-09-19-16-06-33-2017-MAPC") # Jason-DTU vs TUBDAI
#dl("ac1", "2017-09-19-19-13-55-2017-MAPC") # Flisvos vs lampe
#dl("ac2", "2017-09-19-18-01-57-2017-MAPC") # BusyBeaver vs. SMART-JaCaMo

# Wednesday
#dl("ac1", "2017-09-20-14-03-58-2017-MAPC") # Jason-DTU vs Chameleon
#dl("ac2", "2017-09-20-14-10-25-2017-MAPC") # lampe vs TUBDAI
#dl("ac1", "2017-09-20-16-01-19-2017-MAPC") # Flisvos vs Jason-DTU
#dl("ac2", "2017-09-20-17-29-42-2017-MAPC") # BusyBeaver vs TUBDAI

# Thursday
#dl("ac1", "2017-09-21-14-03-40-2017-MAPC") # BusyBeaver vs Chameleon
#dl("ac2", "2017-09-21-14-33-07-2017-MAPC") # Jason-DTU vs. JaCaMo
#dl("ac1", "2017-09-21-16-08-30-2017-MAPC") # TUBDAI vs. Chameleon
#dl("ac2", "2017-09-21-15-41-13-2017-MAPC") # lampe vs. Jason-DTU
#dl("ac1", "2017-09-21-18-07-25-2017-MAPC")
#dl("ac2", "2017-09-21-17-59-54-2017-MAPC")
