import asyncio

import websockets


async def lesten():
    url = "wss://eu-swarm-gvivaro.betconstruct.com"
    async with websockets.connect(url) as ws:
        data = '{"command":"request_session","params":{"language":"eng","site_id":1},"rid":"112"}'
        await ws.send(data)
        data1 = '{"command":"get","params":{"source":"betting","what":{"sport":["id","name","alias","order"],' \
                '"competition":["id","order","name","info"],"region":["id","name","alias","order"],"game":' \
                '[["id","start_ts","team1_name","team2_name","team1_id","team2_id","team1_reg_name",' \
                '"team2_reg_name","type","info","text_info","markets_count","is_blocked","stats","video_provider",' \
                '"is_stat_available","show_type","game_external_id","team1_external_id","team2_external_id","is_itf"]],' \
                '"market":["base","type","name","express_id","id"],"event":[]},"where":{"game":{"type":1},' \
                '"sport":{"type":{"@ne":1},"id":{"@nin":[181]}},"market":{"display_key":"WINNER","display_sub_key":"' \
                'MATCH"}},"subscribe":true},"rid":"165026806988614"}'
        print(await ws.recv())
        await ws.send(data1)
        while True:
            msg = await ws.recv()
            print(msg)


asyncio.run(lesten())
