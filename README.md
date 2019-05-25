### 開發時啟用dev-docker-compose.yml

```
docker-compose -f dev-docker-compose.yml up -d
```

即出現四個container, redisA, redisB, mongo, mongo-express 供調用

可透過`localhost:8081` 觀看mongo 的資料變化

關閉開發環境

```
docker-compose -f dev-docker-compose.yml down
```

### 生產未定義合作流程

目前是將源碼經pytest測試後，封裝成image，

啟用container時，以wsgi作對接


