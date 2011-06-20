# coding=utf-8

import argparse
import sys

from time import sleep

def main():
    parser = argparse.ArgumentParser(description='A timer for high-intensity interval training.')
    parser.add_argument('warm_up', type=int, help='Time in seconds for warm-up.')
    parser.add_argument('high', type=int, help='Time in seconds for high-intensity exercise.')
    parser.add_argument('normal', type=int, help='Time in seconds for normal-intensity excercise.')
    parser.add_argument('reps', type=int, help='Number of repetitions of high/normal excersie.')
    parser.add_argument('cool_down', type=int, help='Time in seconds for cool-down.')
    parser.add_argument('-d', '--delay', required=False, default=10, type=int, help='Delay before starting routine.')
    args = parser.parse_args()
    
    total = 0
    print('Starting routine in %d seconds...' % args.delay)
    sleep(args.delay)
    
    print('\aWarm-up (%d seconds)...' % args.warm_up)
    total += args.warm_up
    sleep(args.warm_up)
    
    for rep in range(1, args.reps + 1):
        print('\a\a\aHigh-intensity rep %d (%d seconds)...' % (rep, args.high))
        total += args.high
        sleep(args.high)
        
        print('\a\aNormal-intensity (%d seconds)...'% args.normal)
        total += args.normal
        sleep(args.normal)
        
    print('\aCool-down (%d seconds)...' % args.cool_down)
    total += args.cool_down
    sleep(args.cool_down)
    
    print('\aRountine complete (total %d seconds).' % total)
    sys.exit(0)
    
if __name__ == '__main__':
    main()
