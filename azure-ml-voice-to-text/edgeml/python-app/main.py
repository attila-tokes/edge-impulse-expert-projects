import os
import sys, getopt
import signal
import time
import contextlib
import time

from edgeml import *
from audio import *
from cloudml import *

def signal_handler(sig, frame):
    sys.exit(0)

# Terminal colors / formatting
FMT_PURPLE = '\033[95m'
FMT_GREEN = '\033[96m'
FMT_BOLD = '\033[1m'
FMT_END = '\033[0m'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

    edgeML = EdgeML()
    audio = Audio()
    cloudML = CloudML()

    while True:

      # Detect the LISTEN keyword using EdgeImpulse
      print()
      print("Waiting for %s%sLISTEN%s keyword..." % (FMT_PURPLE, FMT_BOLD, FMT_END))
      edgeML.wait_for_keyword();
      print()
      print("%s%sLISTEN%s keyword detected!"% (FMT_PURPLE, FMT_BOLD, FMT_END))

      # Record audio (max 30 sec)
      print()
      print("Recording audio (30 sec max): ", end="", flush=True);
      voice = audio.record(30)
      print()

      # ClouldML Voice to Text
      print()
      print("Sending voice to cloud...")
      text = cloudML.voice_to_text(voice)
      print()
      print("Result: %s%s%s%s" % (FMT_GREEN, FMT_BOLD, text, FMT_END))
      print()
      print()

      # Wait a bit
      time.sleep(1)


if __name__ == '__main__':
    main(sys.argv[1:])
