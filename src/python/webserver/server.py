import argparse
import json
import logging
# import subprocess
import sys
import traceback

from flask import Flask
from flask import render_template
# from flask import request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/gallery")
def gallery():
    try:
        return render_template('gallery.html'), 200
    except:
        logger.error(traceback.format_exc())
        return json.dumps(
            {"error": "Sorry, something bad happened with your request."}), 500


# @app.route("/", methods=['GET', 'POST'])
# def run_listener():
#     if request.method == 'POST':
#         listener_command = ["python",
#                             "listener.py",
#                             "--hashtags"]
#         for h in request.form["hashtags"]:
#             listener_command.append(h)

#         proc = subprocess.Popen(listener_command,
#                                 shell=False,
#                                 stdin=None,
#                                 stdout=None,
#                                 stderr=None,
#                                 close_fds=True)
#     else:
#         return render_template('index.html')


class ServerParser(argparse.ArgumentParser):
    def error(self, message):
        link = "https://github.com/patillacode/twallery"
        sys.stderr.write('error: {0}\n'.format(message))
        self.print_help()
        sys.stderr.write('\nPlease check the README or go to {0}\n\n'.format(
            link))
        sys.exit(2)


if __name__ == '__main__':

    try:
        parser = ServerParser()
        parser.add_argument("--host",
                            default="127.0.0.1",
                            help="IP to run on [default: 127.0.0.1]")
        parser.add_argument("--port",
                            default=8080,
                            type=int,
                            help="port to listen to [default: 8080")
        args = parser.parse_args()

        app.run(host=args.host, port=args.port)

    except SystemExit:
        logger.info("Farewell!")
    except:
        logger.error(traceback.format_exc())
