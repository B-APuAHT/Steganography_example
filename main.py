import struct

file = open('data/Золотое утро_s.bmp', 'rb').read()
bits = "".join([str(i % 2) for i in file[54:54 + 32]])
len_bytes = bytes([int(s, 2) for s in [bits[0:8], bits[8:16], bits[16:24], bits[24:32]]])
len_img = struct.unpack("<I", len_bytes)[0]
hidden_bits = "".join([ str( x % 2) for x in file[54 + 32:54 + 32 + len_img * 8]])
hidden_bytes = bytes([int(s, 2) for s in [hidden_bits[x*8:(x+1)*8] for x in range(len_img)]])
hidden_image = open('data/result.jpg', 'wb')
hidden_image.write(hidden_bytes)
hidden_image.close()

