from fastapi import FastAPI
from api import wechat
from api import users
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.models import OpenAPI

def custom_openapi():
    # 调用原始的 get_openapi 函数获取默认的 OpenAPI 对象
    openapi = get_openapi(
        title="My Custom API",
        version="1.0.0",
        description="This is a very custom API",
        # ... 其他参数
    )

    # 在这里进行自定义修改
    # 例如，添加自定义的扩展
    openapi.extensions["x-custom-extension"] = "Some custom value"
    # 或者修改现有的部分
    openapi.info.title = "你好"
    # 返回自定义的 OpenAPI 对象
    return openapi

app = FastAPI(openapi_callback=custom_openapi)




app.include_router(wechat.app,prefix="/wechat")
app.include_router(users.app,prefix="/users")
