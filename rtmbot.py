#!/usr/bin/env python
from argparse import ArgumentParser
import sys
import os
import yaml
import client

sys.path.append(os.getcwd())
sys.path.append("/home/dev10635gce006/tensorflow/temp1/chat-master")
import x_translate as trans
import tensorflow as tf

def main(_):
  print("moto main")
  trans.init_main()

  # load args with config path
  args = parse_args()
  config = yaml.load(open(args.config or 'rtmbot.conf', 'r'))
  bot = client.init(config)
  try:
      bot.start()
  except KeyboardInterrupt:
      sys.exit(0)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-c',
        '--config',
        help='Full path to config file.',
        metavar='path'
    )
    return parser.parse_args()

tf.app.run()

# load args with config path
# args = parse_args()
# config = yaml.load(open(args.config or 'rtmbot.conf', 'r'))
# bot = client.init(config)
# try:
  #   bot.start()
# except KeyboardInterrupt:
  #   sys.exit(0)
