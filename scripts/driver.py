# driver.py
# runs -- OH SHIT HERE COME DATBOI

from sock import Socket

class Driver:
    def __init__(self):
        print("Topkek, m'lady")

    #Wi-Fi Kill Switch
    def order_66(self):
        print("It will be done my lord.")

    # Read Wi-Fi config (SSID/PASS)
    def __read_config(self, conf):
        my_config = open(conf)
        print(my_config.read())

    # Runs DATBOI
    def run(self):
        self.__read_config("config")
        Socket()