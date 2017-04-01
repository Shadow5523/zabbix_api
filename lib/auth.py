# -*- coding: utf-8 -*-
import json
import urllib2

def get_authkey(zabbix_server, zabbix_user, zabbix_pass, head):
    url = "http://" + zabbix_server + "/zabbix/api_jsonrpc.php"

    pdata = json.dumps({"jsonrpc" : "2.0",
                            "method" : "user.login",
                            "params" : {
                                "user" : zabbix_user,
                                "password" : zabbix_pass},
                            "auth" : None,
                            "id" : 1})

    result = urllib2.urlopen(urllib2.Request(url, pdata, head)).read()

    try:
        return json.loads(result)['result']

    except:
        return 1
