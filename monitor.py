#! /usr/bin/python

from datetime import datetime
import time
import psutil


def get_net_percent(pnet, nnet):
    received = nnet.bytes_recv - pnet.bytes_recv
    sent = nnet.bytes_sent - nnet.bytes_sent
    return [received, sent]


def get_dist_percent(pdisk, ndisk):
    read_bytes = ndisk.read_bytes - pdisk.read_bytes
    write_bytes = ndisk.write_bytes - pdisk.write_bytes
    return [read_bytes, write_bytes]


def log(pdisk, pnet):
    ndisk = psutil.disk_io_counters()
    nnet = psutil.net_io_counters()
    disk_counters = get_dist_percent(pdisk, ndisk)
    net_counters = get_net_percent(pnet, nnet)
    cpu_percents = psutil.cpu_percent(0.5, True)
    mem_percent = [psutil.phymem_usage().percent]

    dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    params = [dt]
    params.extend(cpu_percents)
    params.extend(mem_percent)
    params.extend(disk_counters)
    params.extend(net_counters)

    line = ','.join([str(x) for x in params])
    with open('monitor.csv', 'a') as f:
        f.write(line + '\n')
    print line
    return ndisk, nnet


def main():
    print ','.join(['time', 'cpu0', 'cpu1', 'cpu2', 'cpu3', 'mem', 'disk_read', 'disk_write', 'net_recv', 'net_write'])
    pdisk = psutil.disk_io_counters()
    pnet = psutil.net_io_counters()
    while True:
        pdisk, pnet = log(pdisk, pnet)
        # cpu_percent sleeps for 0.5 + this 0.5 = 1
        time.sleep(0.5)

if __name__ == "__main__":
    main()
