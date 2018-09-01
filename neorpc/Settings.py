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
                "https://seed1.cityofzion.io:443",
                "https://seed2.cityofzion.io:443",
                "https://seed3.cityofzion.io:443",
                "https://seed4.cityofzion.io:443",
                "https://seed5.cityofzion.io:443"
            ]
        )

    def setup_testnet(self):
        self.setup(
            [
                "https://test1.cityofzion.io:443",
                "https://test2.cityofzion.io:443",
                "https://test3.cityofzion.io:443",
                "https://test4.cityofzion.io:443",
                "https://test5.cityofzion.io:443"
            ]
        )

    def setup_privnet(self):
        """ Load settings from the privnet JSON config file """
        self.setup(
            [
                "http://127.0.0.1:30333"
            ]
        )


# Settings instance used by external modules
settings = SettingsHolder()

# Load testnet settings as default
settings.setup_testnet()
