import asyncio

import aiohttp
from flags import BASE_URL, main, save_flag, show


async def get_flag(cc):
    url = f'{BASE_URL}/{cc}/{cc}.gif'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            image = await resp.read()
    return image


async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, f'{cc.lower()}.gif')
    return cc


async def download_many(cc_list):
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    res = await asyncio.gather(*to_do)
    return len(res)


def main_sync():
    result = asyncio.run(download_many(['BR', 'US', 'FR', 'DE']))  # Exemplo de chamadas
    print(f'Downloaded {result} flags.')


if __name__ == '__main__':
    main(download_many)
