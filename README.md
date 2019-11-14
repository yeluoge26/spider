# 使用说明

## 进入工作路径

```shell
cd ~/spider
```

## 创建 Docker 镜像

```shell
docker build . -t javspider --network=host
```

## 进入 Docker shell

```shell
docker run --network=host -it -v $PWD:/usr/src/app --entrypoint /bin/bash javspider
```

## 执行程序

### 获取分类
会生成 `output/category_javforme.txt` 文件，里面是所有分类
```shell
python3 run.py --index_category
```

### 建立所有视频索引
会生成 `output/page_index.csv` 文件，里面是所有视频链接
```shell
python3 run.py --index_page
```

### 开启下载
会自动开启下载视频
```shell
python3 run.py --download_video
```

## 注意：如何多个服务器分批次下载

将 `output/page_index.csv` 拆分，放到不同的机器的 `output/`， 然后执行 `python3 run.py --download_video` 上跑就行