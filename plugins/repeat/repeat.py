# coding:utf-8

from __future__ import unicode_literals

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import random
import sys
import time

import tensorflow.python.platform

import numpy as np
from six.moves import xrange
import tensorflow as tf

import data_utils as data_utils
from tensorflow.models.rnn.translate import seq2seq_model
from tensorflow.python.platform import gfile
import MeCabFuji as mf
import x_translate as trans

# don't convert to ascii in py2.7 when creating string to return



crontable = []
outputs = []
model = None
in_vocab_path = '/home/dev10635gce006/tensorflow/temp1/chat-master/datas/vocab_in.txt'
out_vocab_path = '/home/dev10635gce006/tensorflow/temp1/chat-master/datas/vocab_out.txt'
in_vocab = None
rev_out_vocab = None
_buckets = [(15, 30), (25, 60), (60, 130),(800, 1300)]

def main(_):
  print("main")


def process_message(data):
    print("process")
#    tf.app.run()
    try:
        text = trans.decode_main(data['text'])
        outputs.append([data['channel'], text])
    except Exception as e:
        print("例外args:", e.args)
        print("Unexpected error:", sys.exc_info()[0])
        import traceback
        traceback.print_exc()
        raise
    print("run end")
#    global model
#    global in_vocab
#    global rev_out_vocab
#    with tf.Session() as sess:
#        if model is None:
#            print("initilize")
#            model = trans.create_model(sess, True)
#            model.batch_size = 1
#            in_vocab, _ = data_utils.initialize_vocabulary(in_vocab_path)
#            rev_out_vocab, _ = data_utils.initialize_vocabulary(out_vocab_path)
#            print("init done.")
#        if data['channel'].startswith("D"):
#            # outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(
#            #    data['text'], data['channel'])])
#
#            text = mf.mecab(data['text'])
#            print("create output : ", text)
##            token_ids = data_utils.sentence_to_token_ids(text, in_vocab)
##
#            bucket_id = min([b for b in xrange(len(trans._buckets))
#                         if trans._buckets[b][0] > len(token_ids)])
#
#            encoder_inputs, decoder_inputs, target_weights = model.get_batch(
#                {bucket_id: [(token_ids, [])]}, bucket_id)
#
#            _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
#                                             target_weights, bucket_id, True)
#
#            output_message = [int(np.argmax(logit, axis=1)) for logit in output_logits]
#
#            if data_utils.EOS_ID in outputs:
#                output_message = output_message[:output_message.index(data_utils.EOS_ID)]
#
#            print("out :    " + " ".join([rev_out_vocab[output] for output in output_message]))
#            outputs.append([data['channel'], " ".join([rev_out_vocab[output] for output in output_message])])
  
        
