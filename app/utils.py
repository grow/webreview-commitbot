import git
import md5
import os


class Error(Exception):
  pass


class ConflictError(Error):
  pass


def get_work_dir(url):
  m = md5.new()
  m.update(url)
  ident = m.hexdigest()
  return '/tmp/workspaces/{}'.format(ident)


def clone_repo(url, branch):
  work_dir = get_work_dir(url)
  if not os.path.exists(work_dir):
    repo = git.Repo.clone_from(url, work_dir)
  else:
    repo = git.Repo(work_dir)
  try:
    repo.git.checkout(b=branch)
  except git.GitCommandError as e:
    if 'already exists' in str(e):
      repo.git.checkout(branch)
  return repo


def init_repo(url, branch):
  repo = clone_repo(url, branch)
  origin = repo.remotes.origin
  origin.fetch()
  return repo


def update(repo, branch, path, content, sha, message=None, committer=None,
           author=None):
  origin = repo.remotes.origin
  repo.create_head(branch, origin.refs.master).set_tracking_branch(origin.refs.master)
  origin.pull()
  path = os.path.join(repo.working_tree_dir, path)
  if not os.path.exists(os.path.dirname(path)):
    os.makedirs(os.path.dirname(path))
  with open(path, 'w') as f:
    f.write(content)
  repo.index.add([path])
  author = git.Actor(author.name, author.email) if author else None
  committer = git.Actor(committer.name, committer.email) if committer else None
  repo.index.commit(message, author=author, committer=committer)
  origin.push()
  repo.git.log()
  return repo.remotes.origin.url
