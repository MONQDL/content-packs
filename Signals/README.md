# Сценарии обработки (дедупликации) событий для Monq версии 7+ 

[Zabbix Webhook Processor](Zabbix%20Webhook%20Signal%20Processor.txt)

Сценарий обработки событий из Zabbix, полученных через Zabbix Webhook

[Zabbix Default Processor](Zabbix%20Default%20Signal%20Processor.txt)

Сценарий обработки событий из Zabbix, полученных через стандартный поток данных с шаблоном Zabbix Default

[SCOM Default Processor](SCOM%20Signals%20processor.txt)

Фильтрация событий в сценарии производится по названию потока (прим. SCOM).

Сценарий перед созданием сигнала, пробует найти КЕ с меткой ScomObjectPath == <поле ObjectPath в первичном событии>

Если КЕ с такой меткой не будет найдена - Сигнал будет создан без привязки КЕ.
