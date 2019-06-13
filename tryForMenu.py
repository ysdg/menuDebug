import sched, time

s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time())

def print_some_times():
    print(time.time())
    try:
        while 1:
            s.enter(0.1, 1, print_time)
            s.run()
    except KeyboardInterrupt:
        print(time.time())

print_some_times()