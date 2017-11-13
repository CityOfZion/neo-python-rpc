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
                "http://13.59.52.94:8080",
                "http://18.220.214.143:8080",
                "http://13.58.198.112:8080",
                "http://13.59.14.206:8080",
                "http://18.216.9.7:8080"
            ]
        )

    def setup_testnet(self):
        self.setup(
            [
                "http://18.221.221.195:8880",
                "http://18.221.139.152:8880",
                "http://52.15.48.60:8880",
                "http://18.221.0.152:8880",
                "http://52.14.184.44:8880"
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
