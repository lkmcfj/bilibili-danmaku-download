# bilibili-danmaku-download

批量下载b站弹幕

## 使用方法

将本仓库clone到本地后使用Python3运行`start.py`，并在命令行参数中指定目标视频、输出位置

计划支持三种视频ID：BV号、AV号和番剧的media id，目前仅支持media id，另外两种将很快加上

对于单个视频（使用BV/AV号指定），它将下载各p的弹幕。对于一季番剧（用media id），它将批量下载所有集的弹幕。

命令行参数

| 参数                           | 取值                       | 解释                                                         |
| ------------------------------ | -------------------------- | ------------------------------------------------------------ |
| `-t <type>`或`--type <type>`   | `<type>`取`BV`/`av`/`md`   | 使用哪种ID来指定目标视频                                     |
| `--id <id>`                    | `<id>`取对应类型的视频编号 | 目标视频                                                     |
| `-o <path>`或`--output <path>` | 已经存在的路径             | 下载的目标文件夹                                             |
| `--mkdir`                      | 有或没有                   | 是否在目标文件夹下新建文件夹                                 |
| `--save-info`                  | 有或没有                   | 是否额外保存一个json文件，包含标题、编号、各集标题等元信息   |
| `--use-name`                   | 有或没有                   | 如果指定了这个参数，子文件夹（如果有`--mkdir`）、各个弹幕文件、json文件（如果有`--save-info`）的文件名将是对应的标题，否则是编号，详见使用示例 |

关于番剧的media id：以《吹响吧！上低音号 第二季》为例，它的番剧主页是https://www.bilibili.com/bangumi/media/md28223434/，网址中的28223434就是它的media id。观众更常见到的页面可能是https://www.bilibili.com/bangumi/play/ss28937 这样的，在这里可以点击下方标题进入番剧主页。

使用示例：

```
> python start.py -t md -o C:\tmp --mkdir --save-info --use-name --id 28223434
Collecting information
Title: 吹响吧！上低音号 第二季
Video number: 13
Downloading
Complete.
```

之后`C:\tmp`下的目录结构如下

```
C:\tmp
└─吹响吧！上低音号 第二季
        1.盛夏的开场号.xml
        10.放学后的助奏.xml
        11.初恋小号.xml
        12.最后的大赛.xml
        13.早春的尾声.xml
        2.踌躇的长笛.xml
        3.烦恼的夜曲.xml
        4.觉醒的双簧管.xml
        5.奇迹的和声.xml
        6.下雨的指挥家.xml
        7.车站大楼音乐会.xml
        8.感冒的狂想曲.xml
        9.吹响吧！上低音号.xml
        吹响吧！上低音号 第二季.json
```

而如果不指定`--use-name`参数，则会变成

```
C:\tmp
└─md28223434
        1.xml
        10.xml
        11.xml
        12.xml
        13.xml
        2.xml
        3.xml
        4.xml
        5.xml
        6.xml
        7.xml
        8.xml
        9.xml
        md28223434.json
```

