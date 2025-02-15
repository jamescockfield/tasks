# Django Channels consumer
class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.room_group_name = 'tasks'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
