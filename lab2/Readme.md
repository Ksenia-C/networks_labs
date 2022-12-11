# Запуск
В пакетах где-то в репозитории github есть какой-то встроенный hub, можно загрузить прямо оттуда, но я не проверяла насколько он публичный. Поэтому есть еще обычный docker hub

```bash
sudo docker pull kseniac/mtu_search
```

В папке есть mtu_searcher_pure_script.py и mtu_searcher_pure.py. Первый принимает аргументы но не через click, а топорно, поэтому предполагается использовать второй - он собран в докере, поэтому принимает переменные окружения.

```bash
sudo docker run --env DESTINATION_ADDRESS=google.com -it kseniac/mtu_searcher bash
```

```bash
sudo docker run --env DESTINATION_ADDRESS=google.com -e TIMEOUT=10 -e MAX_MTU=1600 -it kseniac/mtu_searcher bash
```