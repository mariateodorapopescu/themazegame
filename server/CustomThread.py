from threading import Thread
# modificare clasa Thread care sa returneze un tip de date,
# va trebui sa returneze true / false daca agentul a gasit calea afara din labirint
class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, verbose=None):
        super().__init__(group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return