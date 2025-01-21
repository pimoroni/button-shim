[![Build Status](https://github.com/pimoroni/button-shim/actions/workflows/test.yml/badge.svg)](https://github.com/pimoroni/button-shim/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/button-shim/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/button-shim?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/buttonshim.svg)](https://pypi.python.org/pypi/buttonshim)
[![Python Versions](https://img.shields.io/pypi/pyversions/buttonshim.svg)](https://pypi.python.org/pypi/buttonshim)

https://shop.pimoroni.com/products/button-shim

Five tactile push buttons and one super-bright RGB LED indicator, ideal for adding extra input and visual notifications to your Raspberry Pi alongside most other HATs and pHATs!

# Installing

We'd recommend using this library with Raspberry Pi OS Bookworm or later. It requires Python ≥3.7.

## Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get you up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the commands exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
git clone https://github.com/pimoroni/button-shim
cd button-shim
./install.sh
```

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

## Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you can install the development version like so:

```bash
git clone https://github.com/pimoroni/button-shim
cd button-shim
./install.sh --unstable
```

## Install stable library from PyPi and configure manually

* Set up a virtual environment: `python3 -m venv --system-site-packages $HOME/.virtualenvs/pimoroni`
* Switch to the virtual environment: `source ~/.virtualenvs/pimoroni/bin/activate`
* Install the library: `pip install buttonshim`

In some cases you may need to us `sudo` or install pip with: `sudo apt install python3-pip`.

This will not make any configuration changes, so you may also need to enable:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

Some of the examples have additional dependencies. You can install them with:

```bash
pip install -r requirements-examples.txt
```

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/button-shim
* Function reference - http://docs.pimoroni.com/buttonshim/
* GPIO Pinout - https://pinout.xyz/pinout/button_shim
* Get help - http://forums.pimoroni.com/c/support

## Unofficial / Third-party libraries

* Go library by Tom Mitchell - https://github.com/tomnz/button-shim-go
