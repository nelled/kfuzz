import threading


class ThreadWrapper(threading.Thread):
    def __init__(self, q, manager):
        self.manager = manager
        self.q = q
        threading.Thread.__init__(self)

    def run(self):
        while True:
            current_executor = self.q.get()
            current_executor.do_execute()
            print(current_executor)
            if not current_executor.execution_successful:

                self.manager.results.append(current_executor)

            self.q.task_done()
