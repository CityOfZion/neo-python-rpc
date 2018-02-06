"""

Sets up your RPC endpoints


"""


class SettingsHolder:
    """
    This class holds all the settings. Needs to be setup with one of the
    `setup` methods before using it.
    """
    RPC_LIST = None

    # Setup methods
    def setup(self, addr_list):
        """ Load settings from a JSON config file """
        self.RPC_LIST = addr_list

    def setup_mainnet(self):
        """ Load settings from the mainnet JSON config file """
        self.setup(
            [
                "http://seed1.cityofzion.io:8080",
                "http://seed2.cityofzion.io:8080",
                "http://seed3.cityofzion.io:8080",
                "http://seed4.cityofzion.io:8080",
                "http://seed5.cityofzion.io:8080"
            ]
        )

    def setup_testnet(self):
        self.setup(
            [
                "http://test1.cityofzion.io:8880",
                "http://test2.cityofzion.io:8880",
                "http://test3.cityofzion.io:8880",
                "http://test4.cityofzion.io:8880",
                "http://test5.cityofzion.io:8880"
            ]
        )

    def setup_privnet(self):
        """ Load settings from the privnet JSON config file """
        self.setup(
            [
                "127.0.0.1:20332"
            ]
        )


# Settings instance used by external modules
settings = SettingsHolder()

# Load testnet settings as default
settings.setup_testnet()
