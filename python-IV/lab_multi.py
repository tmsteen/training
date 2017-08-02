#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_multi` -- Investigate multiprocessing / multithreading
=========================================

LAB_multi Learning Objective: Learn to use the multiprocessing and multithreading modules
                              to perform parallel tasks.
::

 a. Use the given command line parser that accepts the following args:
    -p --process : use multiprocessing
    -t --thread  : use threading
    -w --workers : number of workers to spawn
    -i --items   : number of work items to process

 b. In the main process, create a Queue for all the workers to use for their input work items,
    and a Queue for the workers to use to send their processed items back.  Make sure to share
    the Queue with the workers when they are created.

 c. Write a worker function.  The workers should take items from the Queue, process them,
    and put the results in the output queue.

 d. Write a function called create_workers() that creates the workers based on the
    multiprocessing or threading module as requested by the command line arguments.

 e. Write the main loop to process command line args, create the Queues, build the workers,
    start the workers, generate the work tasks, feed the work tasks to the workers, and print the
    results coming back in the results Queue.

Note: add args as necessary to the skeleton functions below
"""

# Don't change this function


def work_task(item):
    """This is the work to be done on each input item"""
    def is_prime(num):
        for j in range(2, num):
            if (num % j) == 0:
                return False
        return True

    index = 0
    check = 0
    while index < item:
        check += 1
        if is_prime(check):
            index += 1
    return check


# Don't change this function
def generate_work(num_items):
    import random
    return [random.randint(1, 2000) for x in range(num_items)]

# Add your code down here


def worker():
    """This is the thread/process main function that will implement c. above"""
    thread_id = threading.current_thread().name
    process_id = os.getpid()
    while True:
        item = q_in.get()
        q_out.put(work_task(item))
        q_in.task_done()
    pass


def create_workers(config_thread):
    """This function creates workers of the requested type and wires them into the queues,
    per step d. above"""
    if config.thread == True:
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()
    else:
        p = multiprocessing.Process(target = worker)
        p.daemon = True
        p.start()
    pass


if __name__ == "__main__":
    import argparse,queue,threading,multiprocessing,os
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--process", help="Use multiprocessing",
                       action="store_true", default=False)
    group.add_argument("-t", "--thread", help="use threading",
                       action="store_true", default=False)
    parser.add_argument("-w", "--workers", help="number of workers to spawn",
                        type=int, default=5)
    parser.add_argument("-i", "--items", help="number of items to process",
                        type=int, default=20)
    config = parser.parse_args()
    # config variable: config.process is bool saying if process was set
    # config.thread is bool saying if threading was set
    # config.workers is an integer
    # config.items is an integer

    if config.thread == True:
        q_in = queue.Queue()
        q_out = queue.Queue()

    else:
        q_in = multiprocessing.JoinableQueue(config.items+1)
        q_out = multiprocessing.JoinableQueue(config.items+1)

    work_tasks = generate_work(config.items)

    for i in range(config.workers):
        create_workers(config.thread)

    for item in work_tasks:
        q_in.put(item)

    q_in.join()
    returned_items = 0
    while returned_items < config.items:
        result = q_out.get()
        print(result)
        returned_items +=1
