import time, multiprocessing

class Loading:

    chars = ["/", "-", "\\", "|", "/", "-", "\\", "|"]

    def _load(self, t=0.2, msg="loading "):
        print(msg, end='')
        while True:
            for char in self.chars:
                print(f"{char}    ", end='', flush=True)
                time.sleep(t)
                print("\b"*5, end='', flush=True)
    
    def start(self, msg, time=0.2):
        self._t = multiprocessing.Process(target=self._load, args=(time, msg))
        self._t.start()

    def stop(self):
        self._t.terminate()

if __name__ == '__main__':
    load = Loading()
    load.start("loading stuff ")
    time.sleep(5)
    load.stop()