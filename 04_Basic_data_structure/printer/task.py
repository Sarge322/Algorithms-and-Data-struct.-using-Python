import random


class Task:
    def __init__(self, time):
        # time of task creation and placed in queue
        self.timestamp = time
        # amounth of pages_to_print
        self.pages = random.randrange(1, 21)

    # get creation task time
    def getStamp(self):
        return self.timestamp

    # get num of pages
    def getPages(self):
        return self.pages

    # time spend in queue before start printing
    def waitTime(self, current):
        return current - self.timestamp
