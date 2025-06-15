import threading
import time

class BackgroundProcess(threading.Thread):
    def __init__(self, clock, nursery):
        super().__init__()
        self.clock = clock
        self.nursery = nursery
        self.playing = True
        self._stop_event = threading.Event()

    def run(self):
        while self.playing:
            try:
                self.update()
                self._stop_event.wait(timeout=180)  # 180 seconds = 3 minutes
            except Exception:
                pass

    def update(self):
        for duck in self.nursery.DuckArray:
            if duck is None:
                break
            if duck.SF.SatiationScore > 0:
                duck.SF.SatiationScore += duck.SF.SatiationRate
            else:
                duck.SF.SatiationScore = 0

    def stop(self):
        self._stop_event.set()