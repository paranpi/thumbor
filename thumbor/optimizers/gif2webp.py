#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

import os
import subprocess

from thumbor.optimizers import BaseOptimizer


class Optimizer(BaseOptimizer):

    def should_run(self, image_extension, buffer):
        return 'gif' in image_extension and self.context.config.AUTO_WEBP

    def optimize(self, buffer, input_file, output_file):
        command = [
            self.context.config.GIF2WEBP_PATH,
            '-mixed',
            'quiet',
            input_file,
            "-o",
            output_file
        ]
        with open(os.devnull) as null:
            subprocess.call(command, stdin=null)
        self.context.request.format = "webp"
