import pickle
import struct

file = open('data/Золотое утро_s.bmp', 'rb').read()
bits = "".join([str(i % 2) for i in file[54:54 + 32]])
len_bytes = bytes([int(s, 2) for s in [bits[0:8], bits[8:16], bits[16:24], bits[24:32]]])
#struct.unpack("<I", len_bytes)[0]
