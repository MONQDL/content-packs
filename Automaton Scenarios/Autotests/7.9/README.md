# Базовые сценарии обработки отчетов автоматического тестирования

## Сценарий обработки Allure отчетов

[Autotest Builds Parser](Autotest%20Builds%20Parser.txt)

Тип сценария: `BuildProcessor`

Сценарий анализирует поступающие на вход Allure отчеты, формирует метрики и отправляет результаты в маршрутный узел формирования Сигналов

> Является базовым примером реализации сценария парсинга отчетов

## Сценарий формирования сигналов на основании полученных данных из Allure отчета

[Autotest Signal Processor](Autotest%20Signal%20Processor.txt)

Тип сценария: `SignalProcessor`

Сценарий обрабатывает сформированные парсером данные прохождения автоматических тестов.

> Является базовым примером реализации сценария формирования сигналов по отчетам прохождения автотестов.
