########################### Template Code ################################
# Import the libraries to make HTTP requests
import requests
from pprint import pprint

# You don't need to understand how this function works for now
def get_activity(preference=None) -> dict:
    if preference is None:
        url = "http://www.boredapi.com/api/activity/"
    else:
        url = f"http://www.boredapi.com/api/activity?type={preference}"

    response = requests.get(url)
    return response.json()
########################################################################



########################### Example Code #################################
# calling get_activity without parameter
resp_dict1 = get_activity()
pprint(resp_dict1)

# calling get_activity with parameter
resp_dict2 = get_activity('music')
pprint(resp_dict2)
########################################################################
