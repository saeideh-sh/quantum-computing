#!/usr/bin/python

print """
-------------------------------------------------------------------------------------------------------
Problem Statement:
    Setup an initial prepared state and compute the fourier transform on it.
-------------------------------------------------------------------------------------------------------
"""

import qclib
import numpy as np

nqbits = 8

try:
	# setup an initial state to try out QFT
	initstate = [None]*(2**nqbits)
	p = 0
	stsz = 2**nqbits
	for i in range(stsz):
		if (i % (stsz/8)) == 0:
			initstate[i] = 1
		else:
			initstate[i] = 0
		p += np.absolute(initstate[i])**2
	initstate = np.transpose(np.matrix(initstate,dtype=complex))/np.sqrt(p)

	# Start the Quantum Computer Simulator
	q = qclib.qcsim(nqbits,initstate=initstate, qtrace=True)

	# Perform QFT
	qftgate = q.QFT(nqbits)
	q.qgate(qftgate, list(reversed(range(nqbits))))

except qclib.QClibError,ex:
	print ex.args
