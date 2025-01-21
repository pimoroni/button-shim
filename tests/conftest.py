import pytest
import sys
import mock

class SMBus:
    REG_INPUT = 0x00
    REG_OUTPUT = 0x01
    REG_POLARITY = 0x02
    REG_CONFIG = 0x03

    def __init__(self, bus_id):
        self.regs = [0 for x in range(4)]

        self.regs[self.REG_INPUT] = 0     # 0x00: REG_INPUT
        self.regs[self.REG_OUTPUT] = 0    # 0x01: REG_OUTPUT
        self.regs[self.REG_POLARITY] = 0  # 0x02: REG_POLARITY
        self.regs[self.REG_CONFIG] = 0    # 0x03: REG_CONFIG

        self._watch_regs = {
            self.REG_INPUT: "REG_INPUT",
            self.REG_OUTPUT: "REG_OUTPUT",
            self.REG_POLARITY: "REG_POLARITY",
            self.REG_CONFIG: "REG_CONFIG"
        }

        self._watch_len = {
            self.REG_INPUT: 1,
            self.REG_OUTPUT: 1,
            self.REG_POLARITY: 1,
            self.REG_CONFIG: 1
        }

    def _debug(self, addr, reg, data):
        if reg in self._watch_regs.keys():
            name = self._watch_regs[reg]
            length = self._watch_len[reg]
            result = self.regs[reg:reg+length]
            print(f"Writing {data} to {name}: {result}")

    def write_i2c_block_data(self, addr, reg, data):
        self._debug(addr, reg, data)

        for index, value in enumerate(data):
            self.regs[reg] = value

    def write_word_data(self, addr, reg, data):
        self.regs[reg] = (data >> 8) & 0xff
        self.regs[reg + 1] = data & 0xff
        self._debug(addr, reg, data)

    def write_byte_data(self, addr, reg, data):
        self.regs[reg] = data & 0xff

        self._debug(addr, reg, data)

    def read_byte_data(self, addr, reg):
        return self.regs[reg]

    def read_word_data(self, addr, reg):
        return (self.regs[reg] << 8) | self.regs[reg + 1]


@pytest.fixture(scope="function", autouse=False)
def smbus():
    sys.modules["smbus2"] = mock.Mock()
    sys.modules["smbus2"].SMBus = SMBus
    yield sys.modules["smbus2"]
    del sys.modules["smbus2"]


@pytest.fixture(scope="function", autouse=False)
def buttonshim():
    import buttonshim
    yield buttonshim
    del sys.modules["buttonshim"]
