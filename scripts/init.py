# init.py
# load the Driver, pass values

import pydoc

pydoc.importfile("driver.py")

from driver import Driver


DATBOI = Driver()
DATBOI.run()