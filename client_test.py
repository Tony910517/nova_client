from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from novaclient import client as nvclient
auth_url = "http://192.168.210.151:35357/v3"
username = 'Tony'
password = '910517'
user_domain_name = 'Default'
project_name = 'service'
project_domain_name = 'Default'
auth = v3.Password(auth_url= auth_url,
                   username=username,
                   password=password,
                   project_id ='5196c9dd32564e50a57bfa1931dbb4c3',
                   user_domain_name = user_domain_name)
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)
keystone.projects.list()







