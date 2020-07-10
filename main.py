from get_data import get_data
import bar_chart_race as bcr
import asyncio

async def main(filename):
    data = await get_data()
    bcr.bar_chart_race(
        df=data, 
        filename=filename  
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("test.mp4"))
