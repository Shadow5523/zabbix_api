# -*- coding: utf-8 -*-
import sys
sys.path.append("lib/")
from auth import *
from get_info import *
from add import *

if __name__ == "__main__":
    zabbix_server = "192.168.1.36"
    zabbix_user = "admin"
    zabbix_pass = "zabbix"

    head = {"Content-Type": "application/json-rpc"}
    
    auth_key = get_authkey(zabbix_server, zabbix_user, zabbix_pass, head)
    if auth_key == 1:
        print "Login failed!"
        exit(1)

    a = zabbix_add(auth_key, head, zabbix_server)
    g = get_info(auth_key, head, zabbix_server)

    for line in open("addnodes/hostlist.csv"):
        hostname, hostgropname, ipaddress = line.replace("\n", "").split(",")
        port = "10050"
        templateid = "10001"
        
        hostgroupid = g.get_groupid(hostgropname)

        if hostgroupid == 1:
            hostgroupid = a.add_hostgroup(hostgropname);
        
        a.add_host(hostname, hostgroupid, templateid, ipaddress, port)

        
        
