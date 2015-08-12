from . import services
from . import utils
from protorpc.wsgi import service
import webapp2
import subprocess

MESSAGES = '/tmp/messages.txt'


class HelloHandler(webapp2.RequestHandler):
  def get(self):
    msg = 'hello %s!\n' % self.request.headers.get('X-AppEngine-Country', 'world')
    with open(MESSAGES, 'a') as f:
      f.write(msg)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(msg)


class MessagesHandler(webapp2.RequestHandler):
  def get(self):
    with open(MESSAGES, 'r') as f:
      for msg in f:
        self.response.out.write(msg)


class TriggerHandler(webapp2.RequestHandler):
  def get(self):
    repo = utils.clone_repo('https://github.com/grow/growsdk.org.git', 'master')
    try:
      cmd = ['grow', 'build', repo.working_dir]
      output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
      self.response.out.write('<pre>%s</pre>' % e.output)
      self.response.set_status(500)
    else:
      self.response.out.write('<pre>%s</pre>' % output)

test_app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/messages', MessagesHandler),
    ('/trigger', TriggerHandler),
], debug=True)


api_app = service.service_mappings((
    ('/_api/contents.*', services.ContentsService),
))
