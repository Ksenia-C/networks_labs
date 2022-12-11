# Запуск
Команды линуксовые, для других систем должно быть аналогично.

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