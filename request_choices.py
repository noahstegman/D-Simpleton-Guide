import requests, requests_cache, random


requests_cache.install_cache(cache_name='dsg_cache', backend='sqlite', expire_after=600)

def get_top_and_bottom():
    test = requests.get("https://api.themeparks.wiki/v1/entity/bfc89fd6-314d-44b4-b89e-df1a89cf991e/live").json()
    rides = []
    for ride in test["liveData"]:
        if "queue" in ride:
            if "STANDBY" in ride["queue"]:
                    r = {"name": ride["name"], 
                        "wait": ride["queue"]["STANDBY"]["waitTime"]}
                    rides.append(r)
    zeroed_ride = []
    for w in rides:
        if w["wait"] == None:
            w["wait"] = 0
            zeroed_ride.append(w)
        else:
            w["wait"] = int(w["wait"])
            zeroed_ride.append(w)
            
    zeroed_ride = sorted(zeroed_ride, key=lambda x: x["wait"], reverse=True)

    no_wait = []
    for r in zeroed_ride:
        if r["wait"] == 0:
            no_wait.append(r)

    return random.choice(no_wait), zeroed_ride[0]
#bfc89fd6-314d-44b4-b89e-df1a89cf991e