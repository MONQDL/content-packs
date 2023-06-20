# Зависимости плагина обнаружения и сбора метрик Monq Agent

## Установка Kubernetes state metrics

В каталоге `kube-state-metrics` данного репозитория подготовлены
манифесты для создания необходимых сущностей в Kubernetes:

* ClusterRole
* ClusterRoleBinding
* ServiceAccount
* Deployment
* Service

Для применения манифестов, выполните следующую команду:

```bash

kubectl create -f ./kube-state-metrics/*.yaml

```

> Запуск **kube-state-metrics** производится в namespace **kube-system**

Ссылка на проект в GitHub - https://github.com/kubernetes/kube-state-metrics

## Установка metrics-server

Metrics Server можно установить через непосредственное применение манифеста или используя
[Helm chart](https://artifacthub.io/packages/helm/metrics-server/metrics-server). 

Для установки Metrics Server версии v.0.6.2, выполните следующую команду:

```bash
kubectl apply -f ./metric-server/components.yaml
```

> В файле `./metric-server/components.yaml` данного репозитория подготовлены
> манифесты для создания необходимых сущностей в Kubernetes:
> 
> * ClusterRole
> * ClusterRoleBinding
> * ServiceAccount
> * Deployment
> * Service

Инструкции по установке других версий Metrics Server доступны по 
ссылке - https://github.com/kubernetes-sigs/metrics-server/releases

#### Совместимость версий Metrics Server и Kubernetes

 Metrics Server | Metrics API group/version | Поддерживаемая версия Kubernetes 
----------------|---------------------------|------------------------------
 0.6.x          | `metrics.k8s.io/v1beta1`  | 1.19+                        
 0.5.x          | `metrics.k8s.io/v1beta1`  | *1.8+                        
 0.4.x          | `metrics.k8s.io/v1beta1`  | *1.8+                        
 0.3.x          | `metrics.k8s.io/v1beta1`  | 1.8-1.21                     

> Версии Kubernetes ниже v1.16 требуют передачи аргумента `--authorization-always-allow-paths=/livez,/readyz` 
в команду запуска Metrics Server 

> Запуск **Metrics Server** производится в namespace **kube-system**

Ссылка на проект в GitHub - https://github.com/kubernetes-sigs/metrics-server

## Установка Node Exporter

В каталоге `node-exporter` данного репозитория подготовлен
манифест для создания необходимых Daemonset в Kubernetes.

Для применения манифеста, выполните следующую команду:

```bash

kubectl create -f ./node-exporter/daemonset.yaml
kubectl create -f ./node-exporter/service.yaml

```

> Запуск **node-exporter** производится в namespace **monitoring**


Ссылка на проект в GitHub - https://github.com/prometheus/node_exporter
