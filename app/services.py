import base64
from . import messages
from . import utils
from protorpc import remote


class ContentsService(remote.Service):

  def _decode_content(self, content):
    return content

  @remote.method(messages.UpdateRequest,
                 messages.UpdateResponse)
  def update(self, request):
    repo_dir = utils.init_repo(request.url)
    utils.update(
        repo_dir,
        path=request.path,
        content=self._decode_content(request.content),
        sha=request.sha,
        message=request.message,
        committer=request.commiter,
        author=request.author)
    resp = messages.UpdateResponse()
    return resp
