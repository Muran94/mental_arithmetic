import time

class TimerController:
    @classmethod
    def start_timer(cls):
        cls.start_time = time.time()

    @classmethod
    def get_result_time(cls):
        result_time = time.time() - cls.start_time
        return "%0.2f秒" % result_time
