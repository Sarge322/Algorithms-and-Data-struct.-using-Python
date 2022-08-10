class Printer:
    def __init__(self, print_speed):
        # list per 60 sec
        self.speed = print_speed
        # printing or idling
        self.current_task = None
        # how much time left to the end of printing
        self.time_remaining = 0
        # time in work
        self.printing_time = 0

    # time counter for current task
    def timer(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    # return availability of printer for next task if there is any
    def busy(self):
        return True if self.current_task != None else False

    # launch new print task
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.getPages() * 60 / self.speed
        self.printing_time += self.time_remaining

    def pure_work_time(self):
        return self.printing_time
