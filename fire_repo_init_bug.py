from pathlib import Path
import fire

class SomethingLikeGit:

  dirname = ".something_like_git"

  @classmethod
  def init(cls, path=None):
    path = Path(path or Path.cwd())
    path = path / cls.dirname
    print("Initializing at", path)
    path.mkdir(exist_ok=True)
    print("Done.")

  def __init__(self, path=None):
    path = Path(path or Path.cwd())
    for parent in (path, *path.parents):
      self.path = parent / self.dirname
      if self.path.exists():
        break
    else:
      raise FileNotFoundError(path)

class CLI:

    def init(self, path=None):
        return SomethingLikeGit.init(path)

    def repo(self, path=None):
        return SomethingLikeGit(path)

if __name__ == "__main__":
  fire.Fire(CLI)