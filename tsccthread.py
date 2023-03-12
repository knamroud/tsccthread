from threading import Thread
from subprocess import run
from os import remove, listdir
from os.path import exists, join, getmtime


class TSCCThread(Thread):
    '''Thread used to check and compile TypeScript files in your Python Flask/Django project'''

    def __init__(self, tspath: str, jspath: str, debug: bool = False):
        Thread.__init__(self)
        self.tsp = tspath
        self.jsp = jspath
        self.debug = debug # Defaults to False, if True the thread will check files until stopped, otherwise only one time

    def run(self):
        while True:
            for file in listdir(self.tsp):
                if file.find(".") == 0:
                    continue
                elif file.split(".")[-1] != "ts":
                    remove(join(self.tsp, file))
                    continue
                js = join(self.jsp, file.replace("ts", "js"))
                ts = join(self.tsp, file)
                if not exists(js) or getmtime(js) < getmtime(ts):
                    print(f" * Detected change in '{ts}', recompiling.")
                    run(["tsc", ts, "--outFile", js, "--module", "amd"])
            for file in listdir(self.jsp):
                if not exists(join(self.tsp, file.replace("js", "ts"))):
                    remove(join(self.jsp, file))
            if not self.debug:
                break
