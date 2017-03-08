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
        if my_config is None:
            self.__write_config()
        else:
            print(my_config.read())

    # Write Wi-Fi config(SSID/PASS)
    def __write_config(self):
        my_config = open("conf")
        my_input = input("Enter Data: ")
        my_config.write(my_input)

    # Runs DATBOI
    def run(self):
        self.__read_config("config")
        Socket()