# Monq Automaton Scenarios

Примеры сценариев автоматизации Monq (в формате `base64`)

## CMDB Autobuild

Базовые примеры сценариев автопостроения РСМ

| Наименование                                    | Раздел                                 | Актуальная версия |
|-------------------------------------------------|----------------------------------------|-------------------|
| Сценарии автопостроения групп и узлов из Zabbix | [Zabbix](./CMDB%20Autobuild/Zabbix/)   | 7.8               |
| Сценарии автопостроения топологии  vCenter      | [vCenter](./CMDB%20Autobuild/vCenter/) | 7.4               |

## Metrics Thresholds

Базовые [примеры](Metrics%20Thresholds/) сценариев привязки порогов к КЕ и формирования сигналов на основе срабатывания порогов по метрикам

## Signals

Примеры сценариев дедупликации и корреляции событий в Monq

### Zabbix

Сценарии обработки событий из системы мониторинга Zabbix

#### Для потока данных по шаблону Zabbix default

[Zabbix Default Processor](./Signals/Zabbix%20Default%20Signal%20Processor.txt)

#### Для потока данных по шаблону Default Template

> В Zabbix должна быть настроена отправка событий в виде [WebHook](https://docs.monqlab.com/current/ru/solutions/integrations/#%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-zabbix-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D1%83-webhook)

[Zabbix Webhook Processor](./Signals/Zabbix%20Webhook%20Signal%20Processor.txt)

### SCOM

Сценарий обработки событий из системы мониторинга SCOM (System Center Operations Manager)

[SCOM Signal Processor](./Signals/SCOM%20Signals%20processor.txt)

