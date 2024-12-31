## 项目运行

  

```
[root@localhost epg_scraper]# python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 31, 2024 - 15:32:49
Django version 4.2, using settings 'epg_scraper.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```

  

## 节目抓取

  

```
[root@localhost epg_scraper]# python epg/spiders/gdtv.py
频道 广东卫视 已存在于数据库。
频道 广东珠江 已存在于数据库。
频道 广东新闻 已存在于数据库。
频道 广东民生 已存在于数据库。
频道 广东体育 已存在于数据库。
频道 大湾区卫视 已存在于数据库。
频道 大湾区卫视（海外版） 已存在于数据库。
频道 经济科教 已存在于数据库。
频道 广东影视 已存在于数据库。
频道 4K超高清 已存在于数据库。
频道 广东少儿 已存在于数据库。
频道 嘉佳卡通 已存在于数据库。
频道 岭南戏曲 已存在于数据库。
频道 现代教育 已存在于数据库。
频道 广东移动 已存在于数据库。
新增节目: 星辰大海(28) (2025-01-02 00:30:00 - 2025-01-02 01:10:00)
新增节目: 三八线上 (2025-01-02 01:10:00 - 2025-01-02 02:30:00)
新增节目: 重播节目、纪录片 (2025-01-02 02:30:00 - 2025-01-02 05:05:00)
新增节目: 虎刺红(14) (2025-01-02 05:05:00 - 2025-01-02 05:50:00)
新增节目: 虎刺红(15) (2025-01-02 05:50:00 - 2025-01-02 06:57:00)
新增节目: 早间天气预报 (2025-01-02 06:57:00 - 2025-01-02 07:00:00)
新增节目: 广东新闻联播重播 (2025-01-02 07:00:00 - 2025-01-02 07:30:00)
新增节目: 枪侠(20) (2025-01-02 07:30:00 - 2025-01-02 08:20:00)
新增节目: 枪侠(21) (2025-01-02 08:20:00 - 2025-01-02 09:10:00)
新增节目: 枪侠(22) (2025-01-02 09:10:00 - 2025-01-02 10:00:00)
新增节目: 枪侠(23) (2025-01-02 10:00:00 - 2025-01-02 10:55:00)
新增节目: 枪侠(24) (2025-01-02 10:55:00 - 2025-01-02 11:50:00)
新增节目: 老广的味道 (2025-01-02 11:50:00 - 2025-01-02 12:20:00)
新增节目: 水上游击队(20) (2025-01-02 12:20:00 - 2025-01-02 13:12:00)
新增节目: 水上游击队(21) (2025-01-02 13:12:00 - 2025-01-02 14:02:00)
新增节目: 水上游击队(22) (2025-01-02 14:02:00 - 2025-01-02 14:55:00)
新增节目: 水上游击队(23) (2025-01-02 14:55:00 - 2025-01-02 15:55:00)
新增节目: 水上游击队(24) (2025-01-02 15:55:00 - 2025-01-02 16:50:00)
新增节目: 水上游击队(25) (2025-01-02 16:50:00 - 2025-01-02 17:40:00)
新增节目: 水上游击队(26) (2025-01-02 17:40:00 - 2025-01-02 18:30:00)
新增节目: 广东新闻联播 (2025-01-02 18:30:00 - 2025-01-02 18:56:00)
新增节目: 天气预报 (2025-01-02 18:56:00 - 2025-01-02 19:00:00)
新增节目: 转播中央台新闻联播 (2025-01-02 19:00:00 - 2025-01-02 19:35:00)
新增节目: 小巷人家(11) (2025-01-02 19:35:00 - 2025-01-02 20:25:00)
新增节目: 小巷人家(12) (2025-01-02 20:25:00 - 2025-01-02 21:20:00)
新增节目: 从农场到餐桌 (2025-01-02 21:20:00 - 2025-01-02 22:00:00)
新增节目: 晚间新闻 (2025-01-02 22:00:00 - 2025-01-02 22:20:00)
新增节目: 星辰大海(29) (2025-01-02 22:20:00 - 2025-01-02 23:05:00)
新增节目: 星辰大海(30) (2025-01-02 23:05:00 - 2025-01-02 23:55:00)
成功抓取 广东卫视 的节目表。
新增节目: 王牌剧场:和平饭店36、37 (2025-01-01 22:00:00 - 2025-01-02 00:15:00)
新增节目: 今日关注(重播) (2025-01-02 00:15:00 - 2025-01-02 01:05:00)
新增节目: 电视剧:情迷睡美人 (2025-01-02 01:05:00 - 2025-01-02 04:10:00)
新增节目: 电视剧:情迷睡美人 (2025-01-02 04:10:00 - 2025-01-02 07:05:00)
新增节目: 今日关注(重播) (2025-01-02 07:05:00 - 2025-01-02 08:55:00)
新增节目: 电视剧:李三枪 (2025-01-02 08:55:00 - 2025-01-02 15:00:00)
新增节目: 电视剧:闪亮茗天 (2025-01-02 15:00:00 - 2025-01-02 17:40:00)
新增节目: 今日财经 (2025-01-02 17:40:00 - 2025-01-02 17:50:00)
新增节目: 摇钱树 (2025-01-02 17:50:00 - 2025-01-02 18:00:00)
新增节目: 珠江新闻 (2025-01-02 18:00:00 - 2025-01-02 19:00:00)
新增节目: 珠江剧场:追风者8 (2025-01-02 19:00:00 - 2025-01-02 20:00:00)
新增节目: 珠江剧场:追风者9 (2025-01-02 20:00:00 - 2025-01-02 21:00:00)
新增节目: 今日关注 (2025-01-02 21:00:00 - 2025-01-02 22:00:00)
新增节目: 王牌剧场:和平饭店38、39 (2025-01-02 22:00:00 - 2025-01-02 23:45:00)
新增节目: 今日关注(重播) (2025-01-02 23:45:00 - 2025-01-03 00:05:00)
成功抓取 广东珠江 的节目表。
新增节目: 老广的味道 (2024-12-31 00:00:00 - 2024-12-31 00:30:00)
新增节目: 今日焦点 (2024-12-31 00:30:00 - 2024-12-31 01:00:00)
新增节目: 今日一线 (2024-12-31 01:00:00 - 2024-12-31 01:45:00)
新增节目: 新闻故事 (2024-12-31 01:45:00 - 2024-12-31 02:05:00)
新增节目: 今日关注 (2024-12-31 02:05:00 - 2024-12-31 05:40:00)
新增节目: 社会纵横 (2024-12-31 05:40:00 - 2024-12-31 06:00:00)
新增节目: 直播广东 (2024-12-31 06:00:00 - 2024-12-31 06:30:00)
新增节目: 新闻故事 (2024-12-31 06:30:00 - 2024-12-31 06:50:00)
新增节目: 社会纵横 (2024-12-31 06:50:00 - 2024-12-31 07:01:00)
新增节目: 今日关注 (2024-12-31 07:01:00 - 2024-12-31 08:00:00)
新增节目: 广东新闻联播 (2024-12-31 08:00:00 - 2024-12-31 08:30:00)
新增节目: 老广的味道 (2024-12-31 08:30:00 - 2024-12-31 09:00:00)
新增节目: 今日一线 (2024-12-31 09:00:00 - 2024-12-31 09:45:00)
新增节目: 社会纵横 (2024-12-31 09:45:00 - 2024-12-31 10:00:00)
新增节目: 正点播报 (2024-12-31 10:00:00 - 2024-12-31 10:30:00)
新增节目: 新闻故事 (2024-12-31 10:30:00 - 2024-12-31 10:50:00)
新增节目: 社会纵横 (2024-12-31 10:50:00 - 2024-12-31 11:00:00)
新增节目: 正点播报 (2024-12-31 11:00:00 - 2024-12-31 11:30:00)
新增节目: 老广的味道 (2024-12-31 11:30:00 - 2024-12-31 12:00:00)
新增节目: 午间30分 (2024-12-31 12:00:00 - 2024-12-31 12:30:00)
新增节目: 新闻故事 (2024-12-31 12:30:00 - 2024-12-31 13:00:00)
新增节目: 正点播报 (2024-12-31 13:00:00 - 2024-12-31 13:30:00)
新增节目: 老广的味道 (2024-12-31 13:30:00 - 2024-12-31 14:00:00)
新增节目: 正点播报 (2024-12-31 14:00:00 - 2024-12-31 14:40:00)
新增节目: 新闻故事 (2024-12-31 14:40:00 - 2024-12-31 15:00:00)
新增节目: 正点播报 (2024-12-31 15:00:00 - 2024-12-31 15:30:00)
新增节目: 老广的味道 (2024-12-31 15:30:00 - 2024-12-31 16:00:00)
新增节目: 正点播报 (2024-12-31 16:00:00 - 2024-12-31 16:30:00)
新增节目: 新闻故事 (2024-12-31 16:30:00 - 2024-12-31 17:00:00)
新增节目: 正点播报 (2024-12-31 17:00:00 - 2024-12-31 17:30:00)
新增节目: 老广的味道 (2024-12-31 17:30:00 - 2024-12-31 18:00:00)
新增节目: 正点播报 (2024-12-31 18:00:00 - 2024-12-31 18:30:00)
新增节目: 老广的味道 (2024-12-31 18:30:00 - 2024-12-31 19:00:00)
新增节目: 正点播报 (2024-12-31 19:00:00 - 2024-12-31 19:25:00)
新增节目: 天气预报 (2024-12-31 19:25:00 - 2024-12-31 19:30:00)
新增节目: 广东新闻联播 (2024-12-31 19:30:00 - 2024-12-31 20:00:00)
新增节目: 直播广东 (2024-12-31 20:00:00 - 2024-12-31 20:30:00)
新增节目: 今日焦点 (2024-12-31 20:30:00 - 2024-12-31 21:00:00)
新增节目: 社会纵横 (2024-12-31 21:00:00 - 2024-12-31 21:10:00)
新增节目: 新闻故事 (2024-12-31 21:10:00 - 2024-12-31 21:30:00)
新增节目: 今日一线 (2024-12-31 21:30:00 - 2024-12-31 22:20:00)
新增节目: 社会纵横 (2024-12-31 22:20:00 - 2024-12-31 22:30:00)
新增节目: 新闻夜线 (2024-12-31 22:30:00 - 2024-12-31 23:00:00)
新增节目: 今日关注 (2024-12-31 23:00:00 - 2024-12-31 23:50:00)
新增节目: 老广的味道 (2025-01-01 00:00:00 - 2025-01-01 00:30:00)
新增节目: 今日焦点 (2025-01-01 00:30:00 - 2025-01-01 01:00:00)
新增节目: 今日一线 (2025-01-01 01:00:00 - 2025-01-01 01:45:00)
新增节目: 新闻故事 (2025-01-01 01:45:00 - 2025-01-01 02:05:00)
新增节目: 今日关注 (2025-01-01 02:05:00 - 2025-01-01 05:40:00)
新增节目: 社会纵横 (2025-01-01 05:40:00 - 2025-01-01 06:00:00)
新增节目: 直播广东 (2025-01-01 06:00:00 - 2025-01-01 06:30:00)
新增节目: 新闻故事 (2025-01-01 06:30:00 - 2025-01-01 06:50:00)
新增节目: 社会纵横 (2025-01-01 06:50:00 - 2025-01-01 07:01:00)
新增节目: 今日关注 (2025-01-01 07:01:00 - 2025-01-01 08:00:00)
新增节目: 广东新闻联播 (2025-01-01 08:00:00 - 2025-01-01 08:30:00)
新增节目: 老广的味道 (2025-01-01 08:30:00 - 2025-01-01 09:00:00)
新增节目: 今日一线 (2025-01-01 09:00:00 - 2025-01-01 09:45:00)
新增节目: 社会纵横 (2025-01-01 09:45:00 - 2025-01-01 10:00:00)
新增节目: 正点播报 (2025-01-01 10:00:00 - 2025-01-01 10:30:00)
新增节目: 新闻故事 (2025-01-01 10:30:00 - 2025-01-01 10:50:00)
新增节目: 社会纵横 (2025-01-01 10:50:00 - 2025-01-01 11:00:00)
新增节目: 正点播报 (2025-01-01 11:00:00 - 2025-01-01 11:30:00)
新增节目: 老广的味道 (2025-01-01 11:30:00 - 2025-01-01 12:00:00)
新增节目: 午间30分 (2025-01-01 12:00:00 - 2025-01-01 12:30:00)
新增节目: 新闻故事 (2025-01-01 12:30:00 - 2025-01-01 12:50:00)
新增节目: 社会纵横 (2025-01-01 12:50:00 - 2025-01-01 13:00:00)
新增节目: 正点播报 (2025-01-01 13:00:00 - 2025-01-01 13:30:00)
新增节目: 老广的味道 (2025-01-01 13:30:00 - 2025-01-01 14:00:00)
新增节目: 正点播报 (2025-01-01 14:00:00 - 2025-01-01 14:40:00)
新增节目: 新闻故事 (2025-01-01 14:40:00 - 2025-01-01 15:00:00)
新增节目: 正点播报 (2025-01-01 15:00:00 - 2025-01-01 15:30:00)
新增节目: 老广的味道 (2025-01-01 15:30:00 - 2025-01-01 16:00:00)
新增节目: 正点播报 (2025-01-01 16:00:00 - 2025-01-01 16:30:00)
新增节目: 新闻故事 (2025-01-01 16:30:00 - 2025-01-01 17:00:00)
新增节目: 正点播报 (2025-01-01 17:00:00 - 2025-01-01 17:30:00)
新增节目: 老广的味道 (2025-01-01 17:30:00 - 2025-01-01 18:00:00)
新增节目: 正点播报 (2025-01-01 18:00:00 - 2025-01-01 18:30:00)
新增节目: 老广的味道 (2025-01-01 18:30:00 - 2025-01-01 19:00:00)
新增节目: 正点播报 (2025-01-01 19:00:00 - 2025-01-01 19:25:00)
新增节目: 天气预报 (2025-01-01 19:25:00 - 2025-01-01 19:30:00)
新增节目: 广东新闻联播 (2025-01-01 19:30:00 - 2025-01-01 20:00:00)
新增节目: 直播广东 (2025-01-01 20:00:00 - 2025-01-01 20:30:00)
新增节目: 今日焦点 (2025-01-01 20:30:00 - 2025-01-01 21:00:00)
新增节目: 社会纵横 (2025-01-01 21:00:00 - 2025-01-01 21:10:00)
新增节目: 新闻故事 (2025-01-01 21:10:00 - 2025-01-01 21:30:00)
新增节目: 今日一线 (2025-01-01 21:30:00 - 2025-01-01 22:20:00)
新增节目: 社会纵横 (2025-01-01 22:20:00 - 2025-01-01 22:30:00)
新增节目: 新闻夜线 (2025-01-01 22:30:00 - 2025-01-01 23:00:00)
新增节目: 今日关注 (2025-01-01 23:00:00 - 2025-01-02 00:00:00)
新增节目: 老广的味道 (2025-01-02 00:00:00 - 2025-01-02 00:30:00)
新增节目: 今日焦点 (2025-01-02 00:30:00 - 2025-01-02 01:00:00)
新增节目: 今日一线 (2025-01-02 01:00:00 - 2025-01-02 01:45:00)
新增节目: 新闻故事 (2025-01-02 01:45:00 - 2025-01-02 02:05:00)
新增节目: 今日关注 (2025-01-02 02:05:00 - 2025-01-02 05:40:00)
新增节目: 社会纵横 (2025-01-02 05:40:00 - 2025-01-02 06:00:00)
新增节目: 直播广东 (2025-01-02 06:00:00 - 2025-01-02 06:30:00)
新增节目: 新闻故事 (2025-01-02 06:30:00 - 2025-01-02 06:50:00)
新增节目: 社会纵横 (2025-01-02 06:50:00 - 2025-01-02 07:01:00)
新增节目: 今日关注 (2025-01-02 07:01:00 - 2025-01-02 08:00:00)
新增节目: 广东新闻联播 (2025-01-02 08:00:00 - 2025-01-02 08:30:00)
新增节目: 老广的味道 (2025-01-02 08:30:00 - 2025-01-02 09:00:00)
新增节目: 今日一线 (2025-01-02 09:00:00 - 2025-01-02 09:45:00)
新增节目: 社会纵横 (2025-01-02 09:45:00 - 2025-01-02 10:00:00)
新增节目: 正点播报 (2025-01-02 10:00:00 - 2025-01-02 10:30:00)
新增节目: 新闻故事 (2025-01-02 10:30:00 - 2025-01-02 11:00:00)
新增节目: 正点播报 (2025-01-02 11:00:00 - 2025-01-02 11:30:00)
新增节目: 老广的味道 (2025-01-02 11:30:00 - 2025-01-02 12:00:00)
新增节目: 午间30分 (2025-01-02 12:00:00 - 2025-01-02 12:30:00)
新增节目: 新闻故事 (2025-01-02 12:30:00 - 2025-01-02 12:50:00)
新增节目: 社会纵横 (2025-01-02 12:50:00 - 2025-01-02 13:00:00)
新增节目: 正点播报 (2025-01-02 13:00:00 - 2025-01-02 13:30:00)
新增节目: 老广的味道 (2025-01-02 13:30:00 - 2025-01-02 14:00:00)
新增节目: 正点播报 (2025-01-02 14:00:00 - 2025-01-02 14:40:00)
新增节目: 新闻故事 (2025-01-02 14:40:00 - 2025-01-02 15:00:00)
新增节目: 正点播报 (2025-01-02 15:00:00 - 2025-01-02 15:30:00)
新增节目: 老广的味道 (2025-01-02 15:30:00 - 2025-01-02 16:00:00)
新增节目: 正点播报 (2025-01-02 16:00:00 - 2025-01-02 16:30:00)
新增节目: 新闻故事 (2025-01-02 16:30:00 - 2025-01-02 17:00:00)
新增节目: 正点播报 (2025-01-02 17:00:00 - 2025-01-02 17:30:00)
新增节目: 老广的味道 (2025-01-02 17:30:00 - 2025-01-02 18:00:00)
新增节目: 正点播报 (2025-01-02 18:00:00 - 2025-01-02 18:30:00)
新增节目: 老广的味道 (2025-01-02 18:30:00 - 2025-01-02 19:00:00)
新增节目: 正点播报 (2025-01-02 19:00:00 - 2025-01-02 19:25:00)
新增节目: 天气预报 (2025-01-02 19:25:00 - 2025-01-02 19:30:00)
新增节目: 广东新闻联播 (2025-01-02 19:30:00 - 2025-01-02 20:00:00)
新增节目: 直播广东 (2025-01-02 20:00:00 - 2025-01-02 20:30:00)
新增节目: 今日焦点 (2025-01-02 20:30:00 - 2025-01-02 21:00:00)
新增节目: 社会纵横 (2025-01-02 21:00:00 - 2025-01-02 21:10:00)
新增节目: 品牌广东 (2025-01-02 21:10:00 - 2025-01-02 21:30:00)
新增节目: 今日一线 (2025-01-02 21:30:00 - 2025-01-02 22:20:00)
新增节目: 社会纵横 (2025-01-02 22:20:00 - 2025-01-02 22:30:00)
新增节目: 新闻夜线 (2025-01-02 22:30:00 - 2025-01-02 23:00:00)
新增节目: 今日关注 (2025-01-02 23:00:00 - 2025-01-02 23:50:00)
成功抓取 广东新闻 的节目表。
新增节目: 国歌 (2025-01-02 07:00:00 - 2025-01-02 07:05:00)
新增节目: DV现场 (2025-01-02 07:05:00 - 2025-01-02 09:15:00)
新增节目: 外来媳妇本地郎 (2025-01-02 09:15:00 - 2025-01-02 10:00:00)
新增节目: 外来媳妇本地郎 (2025-01-02 10:00:00 - 2025-01-02 12:00:00)
新增节目: DV现场 (2025-01-02 12:00:00 - 2025-01-02 14:15:00)
新增节目: 外来媳妇本地郎 (2025-01-02 14:15:00 - 2025-01-02 15:30:00)
新增节目: 民生休闲剧场:前夜 (2025-01-02 15:30:00 - 2025-01-02 17:35:00)
新增节目: 外来媳妇本地郎(4-6) (2025-01-02 17:35:00 - 2025-01-02 18:50:00)
新增节目: DV严选 (2025-01-02 18:50:00 - 2025-01-02 19:00:00)
新增节目: DV现场(4936) (2025-01-02 19:00:00 - 2025-01-02 20:25:00)
新增节目: 全民帮帮忙(925) (2025-01-02 20:25:00 - 2025-01-02 20:40:00)
新增节目: 热搜榜中榜(313) (2025-01-02 20:40:00 - 2025-01-02 21:05:00)
新增节目: 民生休闲剧场:前夜(7-8) (2025-01-02 21:05:00 - 2025-01-02 22:30:00)
新增节目: DV现场 (2025-01-02 22:30:00 - 2025-01-02 23:20:00)
成功抓取 广东民生 的节目表。
新增节目: 重播 羽乐无限:2024世界羽联世界巡回赛总决赛精选(6)52'女单半决赛 大崛彩vs韩悦 (2025-01-02 00:53:00 - 2025-01-02 01:45:00)
新增节目: 首播 ONE周刊(93) (2025-01-02 01:45:00 - 2025-01-02 02:15:00)
新增节目: 重播 全运回眸(3)十四运跳水女子10米台决赛 (2025-01-02 02:15:00 - 2025-01-02 03:07:00)
新增节目: 重播(可删减长度)十分好球(24-25赛季CBA版1231) (2025-01-02 03:07:00 - 2025-01-02 03:10:00)
新增节目: 重播(可删减长度)十分好球(24-25赛季CBA版1105) (2025-01-02 03:10:00 - 2025-01-02 03:13:00)
新增节目: 重播 全运回眸(10)十四运田径项目精选 (2025-01-02 03:13:00 - 2025-01-02 03:28:00)
新增节目: 重播 全运回眸(11)十四运游泳项目精选 (2025-01-02 03:28:00 - 2025-01-02 03:43:00)
新增节目: 重播(可删减长度)十分好球(德甲干净版0924)(24-25赛季) (2025-01-02 03:43:00 - 2025-01-02 03:46:00)
新增节目: 重播(可删减长度)十分好球(24-25赛季CBA版1217) (2025-01-02 03:46:00 - 2025-01-02 03:49:00)
新增节目: 重播 2024中甲第18轮精编版 广州队vs佛山南狮 (2025-01-02 03:49:00 - 2025-01-02 04:15:00)
新增节目: 重播 2024中甲第19轮精编版 云南玉昆vs广州队 (2025-01-02 04:15:00 - 2025-01-02 04:41:00)
新增节目: 重播(可删减长度)十分好球(24-25赛季CBA版1119) (2025-01-02 04:41:00 - 2025-01-02 04:44:00)
新增节目: 重播(可删减长度)十分好球(24-25赛季CBA版1203) (2025-01-02 04:44:00 - 2025-01-02 04:47:00)
新增节目: 重播 羽乐无限:2024世界羽联世界巡回赛总决赛精选(5)男单决赛 安东森vs石宇奇 (2025-01-02 04:47:00 - 2025-01-02 05:43:00)
新增节目: 重播 2024世界F1第20站墨西哥大奖赛正赛 (2025-01-02 05:43:00 - 2025-01-02 07:17:00)
新增节目: 重播 ONE周刊(93) (2025-01-02 07:17:00 - 2025-01-02 08:20:00)
新增节目: 重播 全运回眸(4)十四运跳水女子3米板决赛 (2025-01-02 08:20:00 - 2025-01-02 09:51:00)
新增节目: 重播 2024中甲第27轮精编版 广州队vs江西庐山 (2025-01-02 09:51:00 - 2025-01-02 10:55:00)
新增节目: 重播 24-25CBA第15轮精编版 北京北控vs广东东阳光 (2025-01-02 10:55:00 - 2025-01-02 12:00:00)
新增节目: 重播 出奇智胜(556) (2025-01-02 12:00:00 - 2025-01-02 13:01:00)
新增节目: 重播 全运回眸(3)十四运跳水女子10米台决赛 (2025-01-02 13:01:00 - 2025-01-02 13:58:00)
新增节目: 重播 24-25CBA赛场第23轮 四川丰谷酒业vs广州朗肽海本 (2025-01-02 13:58:00 - 2025-01-02 15:25:00)
新增节目: 重播 24-25CBA赛场第25轮 浙江稠州金租vs深圳马可波罗 (2025-01-02 15:25:00 - 2025-01-02 16:25:00)
新增节目: 重播 2024中甲第22轮精编版 无锡吴钩vs广州队 (2025-01-02 16:25:00 - 2025-01-02 17:28:00)
新增节目: 重播 羽乐无限:2024世界羽联世界巡回赛总决赛精选(6) 女单半决赛 大崛彩vs韩悦 19:00 直播 体育世界 (2025-01-02 17:28:00 - 2025-01-02 19:30:00)
新增节目: 首播 篮球大本营(202501) (2025-01-02 19:30:00 - 2025-01-02 20:05:00)
新增节目: 首播 足球星视界(202501) (2025-01-02 20:05:00 - 2025-01-02 20:31:00)
新增节目: 重播 24-25CBA赛场第21轮 广东东阳光vs宁波町渥 (2025-01-02 20:31:00 - 2025-01-02 21:30:00)
新增节目: 直播 晚间体育新闻 (2025-01-02 21:30:00 - 2025-01-02 21:53:00)
新增节目: 首播 出奇智胜(558) (2025-01-02 21:53:00 - 2025-01-02 23:18:00)
新增节目: 首播 24-25CBA赛场第25轮 广东东阳光vs天津先行者 (2025-01-02 23:18:00 - 2025-01-03 00:08:00)
成功抓取 广东体育 的节目表。
新增节目: 湾区文化坊 (2025-01-02 00:30:00 - 2025-01-02 01:23:00)
新增节目: 我爱返寻味 (2025-01-02 01:23:00 - 2025-01-02 02:00:00)
新增节目: 湾区最新闻 (2025-01-02 02:00:00 - 2025-01-02 02:55:00)
新增节目: 72家房客 (2025-01-02 02:55:00 - 2025-01-02 03:45:00)
新增节目: 我爱返寻味 (2025-01-02 06:05:00 - 2025-01-02 06:30:00)
新增节目: 湾区文化坊 (2025-01-02 06:30:00 - 2025-01-02 07:23:00)
新增节目: 城事特搜(重播) (2025-01-02 07:23:00 - 2025-01-02 08:12:00)
新增节目: 短剧连环炮:72家房客 (2025-01-02 08:12:00 - 2025-01-02 09:25:00)
新增节目: 每日运动派 (2025-01-02 09:25:00 - 2025-01-02 10:35:00)
新增节目: 短剧连环炮:72家房客 (2025-01-02 10:35:00 - 2025-01-02 14:40:00)
新增节目: 养生节目 (2025-01-02 14:40:00 - 2025-01-02 15:25:00)
新增节目: 短剧连环炮:72家房客 (2025-01-02 15:25:00 - 2025-01-02 18:30:00)
新增节目: 笑口组 (2025-01-02 18:30:00 - 2025-01-02 18:40:00)
新增节目: 城事特搜 (2025-01-02 18:40:00 - 2025-01-02 19:30:00)
新增节目: 我爱返寻味 (2025-01-02 19:30:00 - 2025-01-02 20:00:00)
新增节目: 湾区最新闻 (2025-01-02 20:00:00 - 2025-01-02 21:00:00)
新增节目: 72家房客 (2025-01-02 21:00:00 - 2025-01-03 00:30:00)
成功抓取 大湾区卫视 的节目表。
新增节目: 湾区文化坊 (2025-01-02 00:30:00 - 2025-01-02 01:30:00)
新增节目: 我爱返寻 (2025-01-02 01:30:00 - 2025-01-02 02:00:00)
新增节目: 湾区最新闻 (2025-01-02 02:00:00 - 2025-01-02 02:55:00)
新增节目: 午夜经典剧场 (2025-01-02 02:55:00 - 2025-01-02 06:00:00)
新增节目: 每日运动派 (2025-01-02 06:00:00 - 2025-01-02 06:10:00)
新增节目: 湾区文化坊 (2025-01-02 06:10:00 - 2025-01-02 07:00:00)
新增节目: 国歌 (2025-01-02 07:00:00 - 2025-01-02 07:01:00)
新增节目: 我爱返寻味 (2025-01-02 07:01:00 - 2025-01-02 07:55:00)
新增节目: 笑口组 (2025-01-02 07:55:00 - 2025-01-02 08:15:00)
新增节目: 城事特搜 (2025-01-02 08:15:00 - 2025-01-02 09:05:00)
新增节目: 经典剧场 (2025-01-02 09:05:00 - 2025-01-02 18:30:00)
新增节目: 笑口组 (2025-01-02 18:30:00 - 2025-01-02 18:40:00)
新增节目: 城事特搜 (2025-01-02 18:40:00 - 2025-01-02 19:30:00)
新增节目: 我爱返寻味 (2025-01-02 19:30:00 - 2025-01-02 20:00:00)
新增节目: 直播:湾区最新闻 (2025-01-02 20:00:00 - 2025-01-02 21:05:00)
新增节目: 晚间剧场 (2025-01-02 21:05:00 - 2025-01-02 21:55:00)
新增节目: 纪录中国 (2025-01-02 21:55:00 - 2025-01-02 22:40:00)
新增节目: 湾区生活带 (2025-01-02 22:40:00 - 2025-01-02 23:00:00)
新增节目: 老友剧场 (2025-01-02 23:00:00 - 2025-01-02 23:50:00)
成功抓取 大湾区卫视（海外版） 的节目表。
成功抓取 经济科教 的节目表。
新增节目: 午夜剧场 (2024-12-30 00:30:00 - 2024-12-30 01:20:00)
新增节目: 醒晨剧场:边城(16-17) (2024-12-30 06:30:00 - 2024-12-30 08:05:00)
新增节目: 有请大医生(重播) (2024-12-30 08:05:00 - 2024-12-30 08:20:00)
新增节目: 醒晨剧场:边城(18-19) (2024-12-30 08:20:00 - 2024-12-30 11:10:00)
新增节目: 广东电影报道(重播) (2024-12-30 11:10:00 - 2024-12-30 11:15:00)
新增节目: 午间大强档:黎明绝杀(37-41) (2024-12-30 11:15:00 - 2024-12-30 17:05:00)
新增节目: 剧无霸前战剧场:历史转折中的邓小平(10-11) (2024-12-30 17:05:00 - 2024-12-30 18:35:00)
新增节目: 有请大医生 (2024-12-30 18:35:00 - 2024-12-30 18:50:00)
新增节目: 剧无霸剧场:胜利之路(20-24) (2024-12-30 18:50:00 - 2024-12-30 22:10:00)
新增节目: 广东电影报道+有请大医生 (2024-12-30 22:10:00 - 2024-12-30 22:20:00)
新增节目: 剧无霸经典剧场:北国英雄(46-48) (2024-12-30 22:20:00 - 2024-12-31 00:30:00)
新增节目: 午夜剧场 (2024-12-31 00:30:00 - 2024-12-31 01:20:00)
新增节目: 醒晨剧场:边城(20-21) (2024-12-31 06:30:00 - 2024-12-31 08:05:00)
新增节目: 有请大医生(重播) (2024-12-31 08:05:00 - 2024-12-31 08:20:00)
新增节目: 醒晨剧场:边城(22-23) (2024-12-31 08:20:00 - 2024-12-31 11:10:00)
新增节目: 广东电影报道(重播) (2024-12-31 11:10:00 - 2024-12-31 11:15:00)
新增节目: 午间大强档:黎明绝杀(42-46) (2024-12-31 11:15:00 - 2024-12-31 17:05:00)
新增节目: 剧无霸前战剧场:历史转折中的邓小平(12-13) (2024-12-31 17:05:00 - 2024-12-31 18:35:00)
新增节目: 有请大医生 (2024-12-31 18:35:00 - 2024-12-31 18:50:00)
新增节目: 剧无霸剧场:胜利之路(25-29) (2024-12-31 18:50:00 - 2024-12-31 22:10:00)
新增节目: 广东电影报道+有请大医生 (2024-12-31 22:10:00 - 2024-12-31 22:20:00)
新增节目: 剧无霸经典剧场:北国英雄(49-51) (2024-12-31 22:20:00 - 2025-01-01 00:30:00)
新增节目: 醒晨剧场:边城(24-25) (2025-01-01 06:30:00 - 2025-01-01 08:05:00)
新增节目: 有请大医生(重播) (2025-01-01 08:05:00 - 2025-01-01 08:20:00)
新增节目: 醒晨剧场:边城(26-27) (2025-01-01 08:20:00 - 2025-01-01 11:10:00)
新增节目: 广东电影报道(重播) (2025-01-01 11:10:00 - 2025-01-01 11:15:00)
新增节目: 午间大强档:黎明绝杀(47-49) (2025-01-01 11:15:00 - 2025-01-01 17:05:00)
新增节目: 剧无霸前战剧场:历史转折中的邓小平(14-15) (2025-01-01 17:05:00 - 2025-01-01 18:35:00)
新增节目: 有请大医生 (2025-01-01 18:35:00 - 2025-01-01 18:50:00)
新增节目: 剧无霸剧场:胜利之路(30-34) (2025-01-01 18:50:00 - 2025-01-01 22:10:00)
新增节目: 广东电影报道+有请大医生 (2025-01-01 22:10:00 - 2025-01-01 22:20:00)
新增节目: 剧无霸经典剧场:北国英雄(52-54) (2025-01-01 22:20:00 - 2025-01-02 00:30:00)
新增节目: 午夜剧场 (2025-01-02 00:30:00 - 2025-01-02 01:20:00)
新增节目: 醒晨剧场:边城(28-29) (2025-01-02 06:30:00 - 2025-01-02 08:05:00)
新增节目: 有请大医生(重播) (2025-01-02 08:05:00 - 2025-01-02 08:20:00)
新增节目: 醒晨剧场:边城(30-31) (2025-01-02 08:20:00 - 2025-01-02 11:10:00)
新增节目: 广东电影报道(重播) (2025-01-02 11:10:00 - 2025-01-02 11:15:00)
新增节目: 午间大强档:战地花开(1-5) (2025-01-02 11:15:00 - 2025-01-02 17:05:00)
新增节目: 剧无霸前战剧场:历史转折中的邓小平(16-17) (2025-01-02 17:05:00 - 2025-01-02 18:35:00)
新增节目: 有请大医生 (2025-01-02 18:35:00 - 2025-01-02 18:50:00)
新增节目: 剧无霸剧场:胜利之路(35-39) (2025-01-02 18:50:00 - 2025-01-02 22:10:00)
新增节目: 广东电影报道+有请大医生 (2025-01-02 22:10:00 - 2025-01-02 22:20:00)
新增节目: 剧无霸经典剧场:川东游击队(1-3) (2025-01-02 22:20:00 - 2025-01-03 00:30:00)
成功抓取 广东影视 的节目表。
新增节目: 4K深夜剧场 (2025-01-02 01:45:00 - 2025-01-02 06:30:00)
新增节目: 律师有嘢讲 (2025-01-02 06:30:00 - 2025-01-02 07:00:00)
新增节目: 晨早剧场 (2025-01-02 07:00:00 - 2025-01-02 11:30:00)
新增节目: 律师有嘢讲 (2025-01-02 11:30:00 - 2025-01-02 12:00:00)
新增节目: 南粤警视 (2025-01-02 12:00:00 - 2025-01-02 12:30:00)
新增节目: 一起旅游吧/不可思议的中国 (2025-01-02 12:30:00 - 2025-01-02 12:45:00)
新增节目: 我爱返寻味 (2025-01-02 12:45:00 - 2025-01-02 13:05:00)
新增节目: 举案说法 (2025-01-02 13:05:00 - 2025-01-02 13:40:00)
新增节目: 下午茶剧场 (2025-01-02 13:40:00 - 2025-01-02 18:05:00)
新增节目: 最紧要健康 (2025-01-02 18:05:00 - 2025-01-02 18:40:00)
新增节目: 我爱返寻味 (2025-01-02 18:40:00 - 2025-01-02 19:00:00)
新增节目: 4K经典剧场 (2025-01-02 19:00:00 - 2025-01-02 20:30:00)
新增节目: 健康有道 (2025-01-02 20:30:00 - 2025-01-02 21:00:00)
新增节目: 律师有嘢讲 (2025-01-02 21:00:00 - 2025-01-02 21:40:00)
新增节目: 纪录片 (2025-01-02 21:40:00 - 2025-01-02 22:30:00)
新增节目: 深夜剧场 (2025-01-02 22:30:00 - 2025-01-02 23:20:00)
成功抓取 4K超高清 的节目表。
新增节目: 早间卡通剧场《超级飞侠》 (2025-01-02 06:00:00 - 2025-01-02 08:00:00)
新增节目: 《赵琳的探险日记》 (2025-01-02 08:00:00 - 2025-01-02 11:30:00)
新增节目: 《量子战队》 (2025-01-02 11:30:00 - 2025-01-02 13:00:00)
新增节目: 《熊出没》 (2025-01-02 13:00:00 - 2025-01-02 17:30:00)
新增节目: 《猪猪侠》 (2025-01-02 17:30:00 - 2025-01-02 18:00:00)
新增节目: 《宠物旅店》 (2025-01-02 18:00:00 - 2025-01-02 19:00:00)
新增节目: 《南方小记者》 (2025-01-02 19:00:00 - 2025-01-02 19:10:00)
新增节目: 《量子战队》 (2025-01-02 19:10:00 - 2025-01-02 19:30:00)
新增节目: 《爆裂飞车》 (2025-01-02 19:30:00 - 2025-01-02 19:50:00)
新增节目: 《羊村守护者》 (2025-01-02 19:50:00 - 2025-01-02 20:40:00)
成功抓取 广东少儿 的节目表。
新增节目: 遇见中华诗词之美 (2024-12-30 21:08:00 - 2024-12-30 21:11:00)
新增节目: 喜羊羊与灰太狼原始世界历险记 (2024-12-30 21:11:00 - 2024-12-30 22:01:00)
新增节目: 熊猫一家亲(一) (2024-12-31 06:02:00 - 2024-12-31 06:57:00)
新增节目: 喜羊羊与灰太狼勇闯四季城 (2024-12-31 06:57:00 - 2024-12-31 07:30:00)
新增节目: 航拍松江的日与夜 (2024-12-31 07:30:00 - 2024-12-31 08:01:00)
新增节目: 喜羊羊与灰太狼勇闯四季城 (2024-12-31 08:01:00 - 2024-12-31 11:26:00)
新增节目: 小花仙之四时花语春夏 (2024-12-31 11:26:00 - 2024-12-31 14:03:00)
新增节目: 嘉佳全能星-魔豆来啦 (2024-12-31 14:03:00 - 2024-12-31 15:10:00)
新增节目: 疯狂小糖(三) (2024-12-31 15:10:00 - 2024-12-31 16:00:00)
新增节目: 熊出没之怪兽计划(二) (2024-12-31 16:00:00 - 2024-12-31 17:10:00)
新增节目: 萌鸡小队(六) (2024-12-31 17:10:00 - 2024-12-31 17:22:00)
新增节目: 熊出没之怪兽计划(二) (2024-12-31 17:22:00 - 2024-12-31 18:09:00)
新增节目: 猪猪侠之超星五灵侠(七) (2024-12-31 18:09:00 - 2024-12-31 18:34:00)
新增节目: 巴啦啦小魔仙之曜星守护者(一) (2024-12-31 18:34:00 - 2024-12-31 18:48:00)
新增节目: 超级飞侠(十七) (2024-12-31 18:48:00 - 2024-12-31 19:02:00)
新增节目: 铠甲勇士星曜诀醒 (2024-12-31 19:02:00 - 2024-12-31 19:16:00)
新增节目: 奇妙萌可之魔法甜心 (2024-12-31 19:16:00 - 2024-12-31 19:30:00)
新增节目: 变形联盟5烈兽战纪 (2024-12-31 19:30:00 - 2024-12-31 19:41:00)
新增节目: 光影天炎战甲 (2024-12-31 19:41:00 - 2024-12-31 19:55:00)
新增节目: 2024大玩家之小特搜员 (2024-12-31 19:55:00 - 2024-12-31 19:57:00)
新增节目: 奥飞大玩家 (2024-12-31 19:57:00 - 2024-12-31 20:00:00)
新增节目: 大玩家-玩具体验 (2024-12-31 20:00:00 - 2024-12-31 20:06:00)
新增节目: 喜羊羊与灰太狼原始世界历险记 (2024-12-31 20:06:00 - 2024-12-31 21:05:00)
新增节目: 遇见中华诗词之美 (2024-12-31 21:05:00 - 2024-12-31 21:08:00)
新增节目: 喜羊羊与灰太狼原始世界历险记 (2024-12-31 21:08:00 - 2024-12-31 21:58:00)
成功抓取 嘉佳卡通 的节目表。
成功抓取 岭南戏曲 的节目表。
新增节目: 益智动画片、纪录片三档滚动(重播) (2025-01-02 06:00:00 - 2025-01-02 18:00:00)
新增节目: 益智动画片、纪录片三档(首播) (2025-01-02 18:00:00 - 2025-01-02 22:00:00)
新增节目: 纪录片三档(重播) 纪录片三档(重播) (2025-01-02 22:00:00 - 2025-01-02 22:50:00)
成功抓取 现代教育 的节目表。
新增节目: 幸福落地 (2025-01-02 00:06:00 - 2025-01-02 00:49:00)
新增节目: 超级食材 (2025-01-02 00:49:00 - 2025-01-02 01:39:00)
新增节目: 国乐大师 (2025-01-02 06:00:00 - 2025-01-02 06:54:00)
新增节目: 瞰见 (2025-01-02 06:54:00 - 2025-01-02 07:00:00)
新增节目: 文化能人的小康故事 (2025-01-02 07:00:00 - 2025-01-02 07:12:00)
新增节目: 不辞长作岭南人 (2025-01-02 07:12:00 - 2025-01-02 07:26:00)
新增节目: 银发元学堂 (2025-01-02 07:26:00 - 2025-01-02 07:45:00)
新增节目: 移动创星音乐榜 (2025-01-02 07:45:00 - 2025-01-02 08:01:00)
新增节目: 追梦者联盟 (2025-01-02 08:01:00 - 2025-01-02 08:44:00)
新增节目: 韩愈来了 (2025-01-02 08:44:00 - 2025-01-02 08:54:00)
新增节目: 幸福落地 (2025-01-02 08:54:00 - 2025-01-02 09:52:00)
新增节目: 卢作孚 (2025-01-02 09:52:00 - 2025-01-02 10:43:00)
新增节目: 瞰见 (2025-01-02 10:43:00 - 2025-01-02 10:48:00)
新增节目: 岭南博物 (2025-01-02 10:48:00 - 2025-01-02 11:18:00)
新增节目: 指尖上的岭南 (2025-01-02 11:18:00 - 2025-01-02 11:29:00)
新增节目: 文化能人的小康故事 (2025-01-02 11:29:00 - 2025-01-02 11:41:00)
新增节目: 移动创星音乐榜 (2025-01-02 11:41:00 - 2025-01-02 11:50:00)
新增节目: 超级食材 (2025-01-02 11:50:00 - 2025-01-02 12:00:00)
新增节目: 韩愈来了 (2025-01-02 12:00:00 - 2025-01-02 12:08:00)
新增节目: 南岭物语 (2025-01-02 12:08:00 - 2025-01-02 12:33:00)
新增节目: 瞰见 (2025-01-02 12:33:00 - 2025-01-02 12:38:00)
新增节目: 人参 (2025-01-02 12:38:00 - 2025-01-02 13:03:00)
新增节目: 不辞长作岭南人 (2025-01-02 13:03:00 - 2025-01-02 13:16:00)
新增节目: 国乐大师 (2025-01-02 13:16:00 - 2025-01-02 14:06:00)
新增节目: 指尖上的岭南 (2025-01-02 14:06:00 - 2025-01-02 14:17:00)
新增节目: 幸福落地 (2025-01-02 14:17:00 - 2025-01-02 15:12:00)
新增节目: 超级食材 (2025-01-02 15:12:00 - 2025-01-02 15:22:00)
新增节目: 追梦者联盟 (2025-01-02 15:22:00 - 2025-01-02 16:05:00)
新增节目: 岭南博物 (2025-01-02 16:05:00 - 2025-01-02 16:35:00)
新增节目: 瞰见 (2025-01-02 16:35:00 - 2025-01-02 16:41:00)
新增节目: 超级食材 (2025-01-02 16:41:00 - 2025-01-02 16:51:00)
新增节目: 文化能人的小康故事 (2025-01-02 16:51:00 - 2025-01-02 16:57:00)
新增节目: 瞰见 (2025-01-02 16:57:00 - 2025-01-02 17:00:00)
新增节目: 人参 (2025-01-02 17:00:00 - 2025-01-02 17:29:00)
新增节目: 文化能人的小康故事 (2025-01-02 17:29:00 - 2025-01-02 17:35:00)
新增节目: 移动创星音乐榜 (2025-01-02 17:35:00 - 2025-01-02 17:44:00)
新增节目: 不辞长作岭南人 (2025-01-02 17:44:00 - 2025-01-02 18:00:00)
新增节目: 南岭物语 (2025-01-02 18:00:00 - 2025-01-02 18:25:00)
新增节目: 韩愈来了 (2025-01-02 18:25:00 - 2025-01-02 18:34:00)
新增节目: 不辞长作岭南人 (2025-01-02 18:34:00 - 2025-01-02 18:48:00)
新增节目: 指尖上的岭南 (2025-01-02 18:48:00 - 2025-01-02 19:00:00)
新增节目: 卢作孚 (2025-01-02 19:00:00 - 2025-01-02 19:50:00)
新增节目: 超级食材 (2025-01-02 19:50:00 - 2025-01-02 20:00:00)
新增节目: 人参 (2025-01-02 20:00:00 - 2025-01-02 20:25:00)
新增节目: 瞰见 (2025-01-02 20:25:00 - 2025-01-02 20:30:00)
新增节目: 马王堆·岁月不朽 (2025-01-02 20:30:00 - 2025-01-02 21:00:00)
新增节目: 追梦者联盟 (2025-01-02 21:00:00 - 2025-01-02 21:43:00)
新增节目: 不辞长作岭南人 (2025-01-02 21:43:00 - 2025-01-02 21:56:00)
新增节目: 岭南博物 (2025-01-02 21:56:00 - 2025-01-02 22:27:00)
新增节目: 国乐大师 (2025-01-02 22:27:00 - 2025-01-02 23:18:00)
新增节目: 韩愈来了 (2025-01-02 23:18:00 - 2025-01-02 23:29:00)
新增节目: 人参 (2025-01-02 23:29:00 - 2025-01-02 23:54:00)
新增节目: 指尖上的岭南 (2025-01-02 23:54:00 - 2025-01-03 00:05:00)
成功抓取 广东移动 的节目表。
```


## 删除节目

  

```
[root@localhost epg_scraper]# python manage.py delete_all_epgs
Successfully deleted all EPG data
```


