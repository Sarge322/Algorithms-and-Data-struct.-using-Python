import random
from a_queue import Queues
from task import Task
from printer import Printer


# generate tasks 1 in 180sec aprox (10 students, 2 task per student in 1 hour)
def new_task(students):
    tasks = 3600 / students * 2
    num = random.randrange(1, tasks + 1)
    return True if num == tasks else False


# start sim
def simulation(num_seconds, print_speed, quantity_of_students):
    printer = Printer(print_speed)
    queue_to_print = Queues()
    # list of idle time from task to task
    waiting_time = []
    # 3600 sex emu
    for current_second in range(num_seconds):
        # check is task created every second
        if new_task(quantity_of_students):
            # create task with time of creation as param
            task = Task(current_second)
            # task to queue
            queue_to_print.enqueue(task)

        if (not printer.busy()) and (not queue_to_print.isEmpty()):
            # remove task from queue
            next_task = queue_to_print.dequeue()
            # add start time of printing in list
            waiting_time.append(next_task.waitTime(current_second))
            # start print task
            printer.start_next(next_task)

        # start of timer countdown of current task
        printer.timer()

    # after 3600 sec calc aver idle and print result ot sim, wait = idle no task time and printing time
    average_wait = sum(waiting_time) / len(waiting_time)
    work_time = printer.pure_work_time()
    print("Average wait %6.1f secs %3d tasks remaining, pure print time %d percent." % (average_wait, queue_to_print.size(), work_time/36))


# 10 try
for i in range(10):

    # 10 list/min and 1 hour
    simulation(3600, 5, 30)
