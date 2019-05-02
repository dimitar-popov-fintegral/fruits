import requests
import code.data as dt
from enum import Enum


################################################################################
class Blueprints(Enum):
    QUICKSTATS = 'http://quickstats.nass.usda.gov/api/api_GET/'
    PARAMS = 'http://quickstats.nass.usda.gov/api/get_param_values/'
    COUNTS = 'http://quickstats.nass.usda.gov/api/get_counts/'


################################################################################
def download(parameters):
    """
    Used to fetch data from QuickStats API via GET request
    :param parameters: (dict) defines GET request additional parameters see https://quickstats.nass.usda.gov/api
    :return: (requests.response)
    """
    return requests.get(url=Blueprints.QUICKSTATS.value, params=parameters)


################################################################################
def params(parameter):
    """
    Used to fetch possible parameter values
    :param parameter: (str) parameter to lookup values for
    :return: (requests.response)
    """
    parameters = {
        'param':parameter,
        'key': dt.read_quick_stats_api_key(),
    }
    return requests.get(url=Blueprints.PARAMS.value, params=parameters)


################################################################################
def count(parameters):
    """
    Used to fetch counts pertaining to data query lookup
    :param parameters: (dict) defines GET request additional parameters see https://quickstats.nass.usda.gov/api
    :return: (requests.response)
    """
    return requests.get(url=Blueprints.COUNTS.value, params=parameters)
