#!/usr/bin/env python
import argparse
import sys
import logging
import traceback

from models import Tracker

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))

# add the handler to the root logger
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)


class TrackParser(argparse.ArgumentParser):
    """ Custom arguments parser """
    def error(self, message):
        """
            Custom error output method

            Args:
                message (str): message to be displayed
        """
        link = "https://github.com/patillacode/twallery"
        sys.stderr.write('\nerror: {0}\n\n'.format(message))
        self.print_help()
        sys.stderr.write('\nPlease check the README or go to {0}\n\n'.format(
            link))
        sys.exit(2)

if __name__ == '__main__':

    try:
        parser = TrackParser()
        mandatory = parser.add_argument_group("mandatory arguments")
        mandatory.add_argument('--hashtags',
                               required=True,
                               nargs='*',
                               help="")

        args = parser.parse_args()
        # Create Tracker with given hashtags
        tracker = Tracker(args.hashtags)
        stream = tracker.authenticate()
        # Capture data by the keywords
        stream.filter(track=tracker.hashtags)

    except (KeyboardInterrupt, SystemExit):
        logging.debug("Farewell my friend!")

    except:
        logging.error(traceback.format_exc())
