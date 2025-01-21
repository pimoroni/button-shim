import pytest


def test_setup(smbus, buttonshim):
    buttonshim.setup()

    assert buttonshim._bus.regs[buttonshim._bus.REG_CONFIG] == 0b00011111
    assert buttonshim._bus.regs[buttonshim._bus.REG_POLARITY] == 0b00000000
    assert buttonshim._bus.regs[buttonshim._bus.REG_OUTPUT] == 0b00000000


def test_set_pixel(smbus, buttonshim):
    with pytest.raises(ValueError):
        buttonshim.set_pixel("", "", "")

    with pytest.raises(ValueError):
        buttonshim.set_pixel(-1, -1, -1)

    with pytest.raises(ValueError):
        buttonshim.set_pixel(256, 256, 256)

    buttonshim.set_pixel(0, 0, 0)

    assert buttonshim._bus.regs[buttonshim._bus.REG_OUTPUT] == 0x00
