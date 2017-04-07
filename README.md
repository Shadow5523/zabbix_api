# zabbix_api

##このスクリプトの説明  
csvファイルに記述されているノードをzabbixに自動登録してくれるスクリプトです。  
大量に登録する必要があるときに便利です。



##csv ファイルの記述方法  
以下の構文で記述してください。
存在しないホストグループが指定されると自動でグループを作成します。
```
ホスト名,ホストグループ名,IPアドレス,機器タイプ
```
機器タイプは以下のいずれかを入れてください。  
1."L2Switch" or "L3Switch" or "Router"  
 テンプレート "Template SNMP Device"が適用されます。

2."Windows"  
 テンプレート"Template OS Windows"が適用されます。

3."Linux"  
 テンプレート"Template OS Linux"が適用されます。

※ 監視するノード側でエージェントの設定を正常に適用しないとアイテム取得に失敗します。
※ 機器タイプは上記いずれか以外のものが追加、もしくは入力されていないとエラーとなります。



##使用方法  
1.main.pyから見て"addnodes/hostlist.csv"に登録したいホストを記述します。  
　(ファイルの構文は上記を参照)

2.main.pyをpythonコマンドを用いて実行します。
```
[root@shadow:zabbix-api]# python main.py -s 192.168.1.36 -u admin -p zabbix
```
-s : サーバのIP又はドメイン名を指定します。  
-u : zabbixユーザのユーザ名を指定します。  
-p : zabbixユーザのパスワードを指定します。  