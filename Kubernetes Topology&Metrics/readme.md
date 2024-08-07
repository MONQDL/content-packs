# Зависимости плагина обнаружения и сбора метрик Monq Agent

Для корректной и полноценной работы контент-пака **"K8s Топология&Метрики"** требуется установить дополнительные компоненты обнаружения метрик кластера: [kube-state-metrics](#установка-kube-state-metrics), [metrics-server](#установка-metrics-server), [node-exporter](#установка-node-exporter).

## Установка kube-state-metrics

В каталоге `kube-state-metrics` данного репозитория подготовлены
манифесты для создания необходимых компонентов `kube-state-metrics` версии `2.9.2`:

После применения манифеста будут созданы следующие сущности в Kubernetes:

* ClusterRole
* ClusterRoleBinding
* ServiceAccount
* Deployment
* Service

Для установки `kube-state-metrics` версии `2.9.2`, выполните следующую команду:

```bash

kubectl create -f ./kube-state-metrics/*.yaml

```

Установка компонентов **kube-state-metrics** будет произведена в namespace **kube-system**.

Ссылка на проект в GitHub - <https://github.com/kubernetes/kube-state-metrics>

### Установка kube-state-metrics при помощи Helm Chart

Ссылка на Chart - <https://artifacthub.io/packages/helm/prometheus-community/kube-state-metrics>.

## Установка metrics-server

В каталоге `metric-server` данного репозитория подготовлен
манифест для создания необходимых компонентов `metrics-server` версии `0.6.2`.

После применения манифеста будут созданы следующие сущности в Kubernetes:

* ClusterRole
* ClusterRoleBinding
* ServiceAccount
* Deployment
* Service

Для установки **"Metrics Server"** версии `0.6.2`, выполните следующую команду:

```bash
kubectl apply -f ./metric-server/*.yaml
```

Установка компонентов **"Metrics Server"** будет произведена в namespace **kube-system**.

Ссылка на проект в GitHub - <https://github.com/kubernetes-sigs/metrics-server>

Инструкции по установке других версий **"Metrics Server"** доступны по 
ссылке - <https://github.com/kubernetes-sigs/metrics-server/releases>

### Совместимость версий Metrics Server и Kubernetes

 | Metrics Server | Metrics API group/version | Поддерживаемая версия Kubernetes |
 |----------------|---------------------------|----------------------------------|
 | 0.6.x          | `metrics.k8s.io/v1beta1`  | 1.19+                            |
 | 0.5.x          | `metrics.k8s.io/v1beta1`  | *1.8+                            |
 | 0.4.x          | `metrics.k8s.io/v1beta1`  | *1.8+                            |
 | 0.3.x          | `metrics.k8s.io/v1beta1`  | 1.8-1.21                         |

> Версии Kubernetes ниже v1.16 требуют передачи аргумента `--authorization-always-allow-paths=/livez,/readyz` 
в команду запуска Metrics Server

### Установка metrics-server при помощи Helm Chart

Ссылка на Chart - <https://artifacthub.io/packages/helm/metrics-server/metrics-server>

## Установка Node Exporter

В каталоге `node-exporter` данного репозитория подготовлены
манифесты для создания необходимых `Daemonset` и `Service` в Kubernetes.

Для применения манифеста, выполните следующую команду:

```bash

kubectl create -f ./node-exporter/*.yaml

```

Установка **node-exporter** будет произведена в namespace **monitoring**, его нужно создать заранее, если он не существует.

Ссылка на проект в GitHub - <https://github.com/prometheus/node_exporter>

### Установка node-exporter при помощи Helm Chart

Ссылка на Chart - <https://artifacthub.io/packages/helm/prometheus-community/prometheus-node-exporter>
