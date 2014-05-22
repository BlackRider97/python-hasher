import sys
import smhasher

random_str = "random_str_"
for num in range (0,100):
        new_str = random_str + str(num)
        val = abs(smhasher.murmur3_x64_64(new_str,0x1234ABCD)) % 4
        print val
