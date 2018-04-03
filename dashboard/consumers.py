from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer



# class CoinPriceConsumer(WebsocketConsumer):
#     """ Coin Price Change Consumer """
#
#
#     def connect(self):
#         # print(self.scope)
#         print("connection made")
#         self.accept()
#
#     def disconnect(self, code):
#         print("disconnect call")
#
#
#     def receive(self, text_data=None, bytes_data=None):
#         print("data recevie")
#         print(text_data)

class CoinPriceConsumer(AsyncJsonWebsocketConsumer):
    """ async web scoket consumer """
    pass

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        await test(user=1, data=text_data)
        print(text_data)
        import json
        await self.send(json.dumps({'user':"data send to the user"}))
        await self.close()

async def test(user=None, data=None):
    import time
    print(user, data)
    time.sleep(10)
    return "test"

