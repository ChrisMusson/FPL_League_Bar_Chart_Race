import aiohttp
import asyncio
import pandas as pd


async def fetch(session, url, headers=None):
    async with session.get(url, headers=headers) as resp:
        assert resp.status == 200
        return await resp.json()


async def get_data(league_id):

    async with aiohttp.ClientSession() as session:
        headers = {"User-Agent": "https://github.com/ChrisMusson/FPL_League_Bar_Chart_Race"}
        url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
        
        data = await fetch(session, url, headers)
        users = data["standings"]["results"]

        user_data = {}
        for user in users:
            user_data[user["entry"]] = user["player_name"].title()

        all_dataframes = []
        for user_id in user_data.keys():
            url = f"https://fantasy.premierleague.com/api/entry/{user_id}/history/"
            json_data = await fetch(session, url, headers)

            dataframe = pd.DataFrame(json_data["current"], columns=["total_points"])
            dataframe = dataframe.rename(columns={"total_points": user_data[user_id]})
            all_dataframes.append(dataframe)

        data = pd.concat(all_dataframes, axis=1)
    return data
