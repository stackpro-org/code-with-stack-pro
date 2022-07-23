
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name



        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))


class PrivateChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

          self.room_name = self.scope['url_route']['kwargs']['room_name']
          self.room_group_name = 'chat_%s' % self.room_name

          await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
              )
          await self.accept()
        
    async def disconnect(self, code):
        # Leave room group
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )


    # Receive message from WebSocket
    async def receive(self,text_data=None, bytes_data=None):

        sms_data=json.loads(text_data)

        sms = sms_data['message']
        img_cap = sms_data['image_caption']
        sms_type = sms_data['message_type']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username.title(),
                'message': sms,
                'message_type': sms_type,
                'image_caption': img_cap,
            })

    # Receive message from room group
    async def chat_message(self, event):
        """ exhange message here """
        message = event['message']
        username = event['username']
        image_caption = event['image_caption']
        message_type = event['message_type']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'image_caption': image_caption,
            'message_type': message_type
        }))
    


