from pathlib import Path 

class Site:
    
    def __init__(self,source,dest):
        self._source = Path(source)
        self._dest = Path(dest)

    
    def create_dir(self,path):
        directory = Path(self._dest + "/" + path.relative_to(self._source))
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self._dest.mkdir(parents=True, exist_ok=True)
        for chkpath in self._source.rglob("*"):
            if chkpath.is_dir:
                Site.create_dir(self, chkpath)