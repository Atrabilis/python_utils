import requests
import time

def get_mac_vendor(mac_addresses):
    """
    Retrieve the manufacturer name associated with the provided MAC addresses.

    :param mac_addresses: A list of MAC addresses.
    :type mac_addresses: list[str]
    :return: A list of manufacturer names corresponding to the MAC addresses.
    :rtype: list[str]
    """
    vendors_list = []
    for mac_address in mac_addresses:
        url = f"https://api.macvendors.com/{mac_address}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            vendors_list.append(response.text)
        except requests.exceptions.HTTPError as e:
            print(e)
        finally:
            time.sleep(1)
    return vendors_list
