# 家庭电视直播源

家里小米电视（L65RB-RA / MiTV-ASTP0）用的直播源，以及电脑上用 VLC 看的版本。

## 文件说明

| 文件 | 用途 |
|---|---|
| `tv.m3u` | 电视端「我的电视」App 用（TVBox 格式，带 tvg-id 和分组） |
| `tv-vlc.m3u` | 电脑 VLC 用（每台内嵌播放器 UA 指令） |
| `make-vlc.py` | 改完 `tv.m3u` 后跑一次，自动生成 `tv-vlc.m3u` |

## 电视端地址

```
https://ghproxy.net/https://raw.githubusercontent.com/cloudzun/iptv-src/master/tv.m3u
```

> 国内直连 `raw.githubusercontent.com` 不通，必须套 `ghproxy.net` 这类加速前缀。

## 电脑 VLC 地址

```
https://ghproxy.net/https://raw.githubusercontent.com/cloudzun/iptv-src/master/tv-vlc.m3u
```

VLC → 媒体 → 打开网络串流 → 粘贴上面的地址。

## 怎么更新

```bash
# 1. 编辑 tv.m3u
python make-vlc.py                      # 同步生成 VLC 版
git add -A && git commit -m "update" && git push
# 2. 电视上重启「我的电视」App 即可
```

## 频道内容

央视 17 套 + CCTV5+ / CGTN 五路 + 30 余省级卫视 + 4K 频道 + 历年春晚，共 120 个，分 4 组。

## 说明

直播流来自互联网公开来源，仅供家庭自用。源可能随时失效，失效时替换 `tv.m3u` 里的地址即可。
