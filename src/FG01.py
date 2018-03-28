# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:48:40 2018

FG 001
"""
import tensorflow as tf
import numpy as np

a = tf.constant( [10] )
b = tf.constant( [20] )
c = tf.add( a, b )

with tf.Session() as sess:
    result = sess.run( c )
    print( 'output: ', result )
