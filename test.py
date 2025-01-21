import mock
import sys

REG_INPUT = 0x00
REG_OUTPUT = 0x01
REG_POLARITY = 0x02
REG_CONFIG = 0x03

regs = [0 for x in range(4)]

class SMBus:
    def __init__(self, bus_id):
        global regs

        regs[REG_INPUT] = 0 # 0x00: REG_INPUT
        regs[REG_OUTPUT] = 0 # 0x01: REG_OUTPUT
        regs[REG_POLARITY] = 0 # 0x02: REG_POLARITY
        regs[REG_CONFIG] = 0 # 0x03: REG_CONFIG

        self._watch_regs = {
            REG_INPUT: 'REG_INPUT',
            REG_OUTPUT: 'REG_OUTPUT',
            REG_POLARITY: 'REG_POLARITY',
            REG_CONFIG: 'REG_CONFIG'
        }

        self._watch_len = {
            REG_INPUT: 1,
            REG_OUTPUT: 1,
            REG_POLARITY: 1,
            REG_CONFIG: 1
        }

    def _debug(self, addr, reg, data):
        global regs

        if reg in self._watch_regs.keys():
            name = self._watch_regs[reg]
            length = self._watch_len[reg]
            result = regs[reg:reg+length]
            print("Writing {data} to {name}: {result}".format(
                data=data, addr=addr, reg=reg, name=name, result=result))

    def write_i2c_block_data(self, addr, reg, data):
        global regs

        self._debug(addr, reg, data)

        for index, value in enumerate(data):
            regs[reg] = value

    def write_word_data(self, addr, reg, data):
        global regs

        regs[reg] = (data >> 8) & 0xff
        regs[reg + 1] = data & 0xff
        self._debug(addr, reg, data)

    def write_byte_data(self, addr, reg, data):
        global regs

        regs[reg] = data & 0xff

        self._debug(addr, reg, data)

    def read_byte_data(self, addr, reg):
        global regs

        return regs[reg]

    def read_word_data(self, addr, reg):
        global regs

        return (regs[reg] << 8) | regs[reg + 1]


def i2c_assert(action, expect, message):
    action()
    assert expect(), message

def assert_raises(action, expect, message):
    try:
        action()
    except expect:
        return

    print(message)
    sys.exit(1)


smbus = mock.Mock()
smbus.SMBus = SMBus

sys.modules['smbus'] = smbus
sys.path.insert(0, ".")

import buttonshim

@buttonshim.on_press(buttonshim.BUTTON_A)
def press(button, state):
    pass

assert regs[REG_CONFIG] == 31, "REG_CONFIG should be set to 31"
assert regs[REG_POLARITY] == 0, "REG_POLARITY should be set to 0"
assert regs[REG_OUTPUT] == 0, "REG_OUTPUT should be set to 0"

assert_raises(lambda: buttonshim.set_pixel("", "", ""),
              ValueError, "set_pixel does not raise ValueError if r/g/b not int")

assert_raises(lambda: buttonshim.set_pixel(-1, -1, -1),
              ValueError, "set_pixel does not raise ValueError if r/g/b < -1")

assert_raises(lambda: buttonshim.set_pixel(256, 256, 256),
              ValueError, "set_pixel does not raise ValueError if r/g/b > 255")

i2c_assert(lambda: buttonshim.set_pixel(0, 0, 0),
           lambda: regs[REG_OUTPUT] == 00,
           "REG_OUTPUT should equal 0")
