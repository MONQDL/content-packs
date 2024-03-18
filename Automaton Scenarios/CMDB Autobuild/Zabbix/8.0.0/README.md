# Changelog

* обновлены условия запуска сценария, теперь сценарий запускается при условии, что: 
  * в первичном событии имеется объект `source.ZabbixHosts` и он не равен `null`
  * в первичном событии имеется поле `source.BuildCMDB` и равно `true`
  
> [Справка](https://docs.monq.ru/docs/get-started/quick-guide/connect-data-stream) по настройке Потока данных для получения топологии Zabbix.