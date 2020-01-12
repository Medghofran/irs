import math
import sys
from bitstring import Bits, BitStream


def getBin(value: int):
    """Converts the given integer into string bit representation."""
    brep = "{0:b}".format(value)
    return brep


def gammaEncode(value: int):
    """applied the gamma encoding scheme."""
    # preliminary testing against the value of the parameter
    if value == 0:
        return 0
    elif value == 1:
        return 10
    else:
        # get the binary representation of the value in hand
        b = getBin(value)
        gamma = ["1" for x in range(len(b))]
        gamma = "".join(gamma)
        gamma += "0"
        gamma += b[1:]
        bits = Bits(bin=gamma)
        writeTofile("tst.bin", rawData=bits)


def gapEncode(data):
    result = []
    # ensure that data is sorted according to the doc id i.e; (the first element in the tuple)
    data = sorted(data, key=lambda x: x[0])
    result.append(data[0])
    for item in data[1:]:
        encoded = (item[0]-result[-1][0], item[1])
        result.append(encoded)
        pass
    return result


def writeTofile(filepath: str, rawData: Bits):
    with open(filepath, "wb") as fp:
        rawData.tofile(fp)


def convertToBytes(value: int) -> bytes:
    return value.to_bytes((value.bit_length() + 7) // 8, 'big')


if __name__ == "__main__":
    gammaEncode(10000)
    with open("test.bin", "wb")as f:
        f.write(convertToBytes(10000))
    list = [(1, 3), (3, 5), (5, 4), (6, 5)]
    print(gapEncode(list))
