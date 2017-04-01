# -*- coding: utf-8 -*-
from optparse import OptionParser
import sys
sys.path.append("lib/")
from auth import *
from get_info import *
from add import *

if __name__ == "__main__":
    p = OptionParser()
    p.add_option("-p",
                 "--passwd",
                 type="string",
                 help="Input the zabbix server password",
                 dest="passwd")
    
    p.add_option("-s",
                 "--server",
                 type="string",
                 help="Input the zabbix server address",
                 dest="server")
    
    p.add_option("-u",
                 "--user",
                 type="string",
                 help="Input the zabbix server user name",
                 dest="user")
    
    options, args= p.parse_args()

    zabbix_pass = options.passwd
    zabbix_server = options.server
    zabbix_user = options.user
    
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

        
        
