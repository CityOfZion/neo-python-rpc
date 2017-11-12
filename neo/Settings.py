"""
These are the core network and system settings. For user-preferences, take a
look at `UserPreferences.py`.

The settings are dynamically configurable, for instance to set them depending
on CLI arguments. By default these are the testnet settings, but you can
reconfigure them by calling the `setup(..)` methods.
"""
import json
import os

# Create am absolute references to the project root folder. Used for
# specifying the various filenames.
dir_current = os.path.dirname(os.path.abspath(__file__))
dir_project_root = os.path.abspath(os.path.join(dir_current, ".."))


# The protocol json files are always in the project root
FILENAME_SETTINGS_MAINNET = os.path.join(dir_project_root, 'protocol.mainnet.json')
FILENAME_SETTINGS_TESTNET = os.path.join(dir_project_root, 'protocol.testnet.json')
FILENAME_SETTINGS_PRIVNET = os.path.join(dir_project_root, 'protocol.privnet.json')


class SettingsHolder:
    """
    This class holds all the settings. Needs to be setup with one of the
    `setup` methods before using it.
    """
    RPC_LIST = None

    # Setup methods
    def setup(self, config_file):
        """ Load settings from a JSON config file """
        with open(config_file) as data_file:
            data = json.load(data_file)

        config = data['ProtocolConfiguration']
        self.RPC_LIST = config['RPCList']

    def setup_mainnet(self):
        """ Load settings from the mainnet JSON config file """
        self.setup(FILENAME_SETTINGS_MAINNET)

    def setup_testnet(self):
        """ Load settings from the testnet JSON config file """
        self.setup(FILENAME_SETTINGS_TESTNET)

    def setup_privnet(self):
        """ Load settings from the privnet JSON config file """
        self.setup(FILENAME_SETTINGS_PRIVNET)


# Settings instance used by external modules
settings = SettingsHolder()

# Load testnet settings as default
settings.setup_testnet()
