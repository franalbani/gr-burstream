#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Francisco Albani.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
from gnuradio import gr
import pmt
from threading import Lock

class burstreamer_c(gr.sync_block):
    """
    docstring for block burstreamer_c
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name=self.__class__.__name__,
            in_sig=None,
            out_sig=[np.complex64])

        self.ready_samples = np.empty((0, ))

        self.message_port_register_in(pmt.intern('pdus'))
        self.set_msg_handler(pmt.intern('pdus'), self.pdu_handler)
        self.ready_samples_lock = Lock()

    def pdu_handler(self, pdu):
        cdr = pmt.cdr(pdu)
        new_samples = pmt.to_python(cdr)
        with self.ready_samples_lock:
            self.ready_samples = np.concatenate((self.ready_samples, new_samples))

    def work(self, input_items, output_items):
        out = output_items[0]

        with self.ready_samples_lock:
            n_demanded = len(out)
            n_ready = len(self.ready_samples)

            n_zeros = max(0, n_demanded - n_ready)
            zeros = np.zeros(n_zeros)

            n_consumed = min(n_ready, n_demanded)

            samples = self.ready_samples[0:n_consumed]

            out[0:n_consumed] = samples
            out[n_consumed:] = zeros

            self.ready_samples = self.ready_samples[n_consumed:]

        return n_demanded
