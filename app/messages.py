from protorpc import messages


class ActorMessage(messages.Message):
  name = messages.StringField(1)
  email = messages.StringField(2)


class UpdateRequest(messages.Message):
  url = messages.StringField(1)
  branch = messages.StringField(2)
  path = messages.StringField(3)
  content = messages.StringField(4)
  sha = messages.StringField(5)
  message = messages.StringField(6)
  committer = messages.MessageField(ActorMessage, 7)
  author = messages.MessageField(ActorMessage, 8)


class UpdateResponse(messages.Message):
  pass
