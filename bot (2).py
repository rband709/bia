api_id = 3335796
api_hash = '138b992a0e672e8346d8439c3f42ea78'
token = '5088657122:AAGXARfg6sSX1p1ge876jknkrJizwH959b4'

from pyrogram import Client , filters

app = Client(
'uploader',
api_id=api_id,
api_hash=api_hash,
token=token

)

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO

)
LOGGER = logging.getLogger(__name__)

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply('Hello Fom Pyrogram!')

    app.run()