from get_data import get_data
import bar_chart_race as bcr
import asyncio

async def main():

    with open("league_id.txt", "r") as f:
        league_id = f.read()
    
    data = await get_data(league_id)

    bcr.bar_chart_race(
        df=data, 
        filename=f"{league_id}.mp4"  
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
