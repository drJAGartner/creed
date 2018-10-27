import soundfile as sf
import sounddevice as sd
from time import sleep
import argparse

def do_round(data, fs, work, rest):
    sd.play(data, fs, blocking=True)
    sleep(work)
    sd.play(data, fs, blocking=True)
    sleep(rest)


def intervals(work, rest, max_intervals):
    num_intervals = 0
    data, fs = sf.read("/System/Library/Sounds/Basso.aiff")

    while max_intervals==-1 or num_intervals < max_intervals:
        num_intervals += 1
        print("Interval", num_intervals)
        do_round(data, fs, work, rest)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Alternating")
    parser.add_argument('work', type=int, help='Time in seconds for work period')
    parser.add_argument('rest', type=int, help='Time in seconds for rest period')
    parser.add_argument('intervals', type=int, help='Number of rounds, -1 for no limit')

    args = parser.parse_args()
    intervals(args.work, args.rest, args.intervals)
