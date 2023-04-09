import aiohttp
import asyncio
from fpl import FPL
import pandas as pd
import datetime as dt


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    top_perforemence = sorted(
        players, key = lambda x: x.goals_scored+x.assists+x.total_points,reverse=True)

    data = []
    for player in top_perforemence:
        goals = player.goals_scored
        assists = player.assists
        points = player.total_points
        timestamp = pd.to_datetime(dt.datetime.now())
        data.append([player.web_name, player.now_cost / 10, goals, assists,points,timestamp])

    columns = ["Player", "£", "G", "A","P","Timestamp"]
    df = pd.DataFrame(data, columns=columns)

    return df.sort_values(by="P",ascending=False,ignore_index=True)

df = asyncio.run(main())

