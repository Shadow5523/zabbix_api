# -*- coding: utf-8 -*-
import json
import urllib2

class zabbix_add:
    def __init__(self, auth_key, head, zabbix_server):
        self.auth_key = auth_key
        self.head = head
        self.zabbix_server = zabbix_server




    def add_host(self, hostname, hostgroupid, templateid, ipaddress, port):
        url = "http://" + self.zabbix_server + "/zabbix/api_jsonrpc.php"
        pdata = json.dumps({"jsonrpc" : 2.0,
                            "method" : "host.create",
                            "params" : {
                                "host" : hostname,
                                "interfaces" : [{
                                    "type" : 1,
                                    "main" : 1,
                                    "useip" : 1,
                                    "ip" : ipaddress,
                                    "dns" : "",
                                    "port" : port
                                }],
                                "groups" : [{
                                    "groupid" : hostgroupid
                                }],
                                "hostgroupid" : [{
                                    "templateid" : templateid
                                }],
                                },
                            "auth" : self.auth_key,
                            "id" : 1
                            })

        result = urllib2.urlopen(urllib2.Request(url, pdata, self.head)).read()
        print json.loads(result)



    def add_hostgroup(self, hostgroupname):
        url = "http://" + self.zabbix_server + "/zabbix/api_jsonrpc.php"
        pdata = json.dumps({"jsonrpc": "2.0",
                            "method": "hostgroup.create",
                            "params": {
                                "name": hostgroupname
                            },
                            "auth": self.auth_key,
                            "id": 1
                            })

        result = urllib2.urlopen(urllib2.Request(url, pdata, self.head)).read()
        return json.loads(result)["result"]["groupids"][0]
