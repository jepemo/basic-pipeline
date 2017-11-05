#!/usr/bin/env python3

import sys
sys.path.append('../')
from bpipe import pipe



pipe(range(0,5)) \
	.peek() \
	.next(lambda x: x+1) \
	.peek() \
	.run()