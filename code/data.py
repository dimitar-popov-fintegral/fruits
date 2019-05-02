import os

################################################################################
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')


################################################################################
def data_store():
    """Returns the path to the store"""
    return os.path.join(BASE_DIR, 'store')


################################################################################
def read_quick_stats_api_key():
    """Reads the QuickStats API key from non-versioned file"""
    api_key_file = os.path.join(data_store(), 'secrets', 'quick_stats_api_key')
    assert os.path.isfile(api_key_file),\
        'missing QuickStats API key file, check ./store/secrets/ folder'
    with open(api_key_file) as keyfile:
        return keyfile.read()


################################################################################
