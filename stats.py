#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool

for sched in ['hourly', 'daily' , 'weekly', 'monthly']:
    if sched == 'hourly':
        period = 'h'
    if sched == 'weekly':
        period = 'w'
    elif sched == 'daily':
        period = 'd'
    elif sched == 'monthly':
        period = 'm'
    ret = rrdtool.graph( "/path/to/webserver/dir/metrics-%s.png" %(sched), "--start", "-1%s" %(period), "--vertical-label=Num",
         '--watermark=bot',
         "-w 800",
         "DEF:m1_num=/path/to/example.rrd:msg:AVERAGE",
         "VDEF:m1_avg=m1_num,AVERAGE",
         "LINE2:m1_avg",
         "LINE1:m1_num#0000FF:msg\\r",
         "GPRINT:m1_num:AVERAGE:Avg m1\: %6.0lf ",
         "GPRINT:m1_num:MAX:Max m1\: %6.0lf \\r")
