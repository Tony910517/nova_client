import os
import time
from novaclient import client
from novaclient.v2.images import GlanceManager
from novaclient.v2.flavors import FlavorManager

# auth configuration
auth_url = "http://192.168.210.151:35357/v3"
username = 'Tony'
password = '910517'
user_domain_name = 'Default'
project_name = 'service'
project_domain_name = 'Default'
project_id ='5196c9dd32564e50a57bfa1931dbb4c3'

# 建立nova-client连接
nova = client.Client(version=2,
                     username=username,
                     password=password,
                     project_id=project_id,
                     user_domain_name=user_domain_name,
                     project_domain_name=project_domain_name,
                     auth_url=auth_url)
#print(nova.servers.list())
#print(nova.flavors.list())

GM = GlanceManager(nova)
im = GM.find_image(name_or_id='cirros')
FM = FlavorManager(nova)
fl = FM.create(name='tony.tiny', ram=512, vcpus=1, disk=1)
nova.servers.create("Tony-server", image=im, flavor=fl)
