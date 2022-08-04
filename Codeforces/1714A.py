###
# Solution: this is a cycled smallest distance question
# step 1: transfer time string into timestamp (60 * hour + minute)
# step 2: calculate the time interval between current time and alarm clock time (note that clock time must be no beform current time, as the time is a cycle of timestamps length 60 * 24 = 1440, so we just to calculate (clock_timestamp + 1440 - current_timestamp) % 1440 to get the time interval
# step 3: find the smallest distance alarm clock, to take the mininum time interval as we need
#
###

def get_alarm_min(target, alarms, MAX_VALUE = 60 * 24):
    deltas = [(n - target + MAX_VALUE) % MAX_VALUE for n in alarms] # step 2
    return min(deltas) # step 3


t = int(input())
for _ in range(t):
    n, H, M = input().split()
    n, H, M = int(n), int(H), int(M)
    target = H * 60 + M # step 1
    alarms = []
    for __ in range(n):
        h, m = input().split()
        h, m = int(h), int(m)
        alarms.append(h * 60 + m) # # step 1
    time_min = get_alarm_min(target, alarms)
    print(f'{time_min//60} {time_min%60}')

