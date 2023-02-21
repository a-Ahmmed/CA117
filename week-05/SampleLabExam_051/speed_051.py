#!/usr/bin/env python3

import sys

time_dist, speeds, i = [line.split() for line in sys.stdin], [], 1

while i < len(time_dist):
    ctime = int(time_dist[i][0]) - int(time_dist[i - 1][0])
    cdist = int(time_dist[i][1]) - int(time_dist[i - 1][1])
    speeds.append(cdist // ctime)
    i += 1

print(max(speeds))