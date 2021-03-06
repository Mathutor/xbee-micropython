# Copyright (c) 2019, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import network
import time

# TODO: replace with the target mobile number.
NUMBER = "+18779123444"
MESSAGE = "MicroPython on XBee Cellular is the best!"


print(" +----------------------------------+")
print(" | XBee MicroPython Send SMS Sample |")
print(" +----------------------------------+\n")

cellular = network.Cellular()

print("Waiting for the module to be connected to the cellular network...")

# Before sending the SMS, wait until the module is connected to the cellular network.
while not cellular.isconnected():
    time.sleep(1)

print("Sending SMS to %s >> %s" % (NUMBER, MESSAGE))

try:
    cellular.sms_send(NUMBER, MESSAGE)
    print("Message sent successfully")
except Exception as e:
    print("Send failure: %s" % str(e))
