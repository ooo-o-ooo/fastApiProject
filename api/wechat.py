from typing import Union
from fastapi import APIRouter
from corpwechatbot.app import AppMsgSender
app = APIRouter()
wx_msg = AppMsgSender(log_level=10)
@app.get("/text")
async def weixin():
    wx_msg.send_text("你好ni好ni好")
    return {"item_id": "text"}
@app.get("/card")
async def weixin(item_id: int, q: Union[str, None] = None):
    return {"item_id": "card", "q": q}
@app.get("/news")
async def weixin(item_id: int, q: Union[str, None] = None):
    return {"item_id": "news", "q": q}
