import json
import requests
import time

from instance import config

def get_db_status(initial_search_request):
    '''
    initial_search_request = 'https://api.nal.usda.gov/ndb/search/?format=json&q=&sort=n&max=1&offset=0&api_key=DEMO_KEY'
    total_number = total number of items in usda database
    current_sr = Standard Release version of the data being reported

    Returns {'total': total_number, 'sr': current_sr}
    '''
    usda_database_check = requests.get(initial_search_request)
    check_json = usda_database_check.json()
    total_number = check_json['list']['total']
    current_sr = check_json['list']['sr']
    return {'total': total_number, 'current_sr': current_sr}


def check_dbitem_changed(NDBNO_TOTAL, current_ndbno, LAST_SR,
                         current_sr):  # can this be a wrapper?
    '''Returns True if Database has a different number of items
    '''
    if NDBNO_TOTAL != current_ndbno:
        return True
    elif LAST_SR != current_sr:
        return True
    else:
        return False


def get_ndbno(current_ndbno, search_api_request, formt, q, sort, mx,
              offset_temp, API_KEY):
    '''This returns a list of ndbno's in the usda foods database
    '''
    search_object = requests.get(search_api_request)
    search_json = search_object.json()  # convert search_object to JSON

    ndbno_list_dict = search_json['list'][
        'item']  # ndbno_list_dict is a list of dictionaries, where each dictionary is a unique food item

    ndbno_list = []

    # unpack ndbno_list_dict
    for dictionary in ndbno_list_dict:
        ndbno_list.append(dictionary['ndbno'])

    return ndbno_list


