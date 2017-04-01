# -*- coding: utf-8 -*-
import json
import urllib2

class get_info:
    def __init__(self, auth_key, head, zabbix_server):
        self.auth_key = auth_key
        self.head = head
        self.zabbix_server = zabbix_server


        
    def get_groupid(self, hostgropname):
        url = "http://" + self.zabbix_server + "/zabbix/api_jsonrpc.php"
        pdata = json.dumps({"jsonrpc" : 2.0,
                            "method" : "hostgroup.get",
                            "params" : {
                                "output" : "extend",
                                "filter" : {
                                    "name" : hostgropname
                                    }
                                },
                            "auth" : self.auth_key,
                            "id": 1
                        })

        result = urllib2.urlopen(urllib2.Request(url, pdata, self.head)).read()

        try:
            return json.loads(result)['result'][0]['groupid']

        except:
            return 1
        
