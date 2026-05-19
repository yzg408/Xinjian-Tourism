"""新建大观 · 种子数据"""
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend.models import Base, ScenicSpot, Route, Festival


def seed_data():
    db = SessionLocal()
    try:
        # 检查是否已有数据
        if db.query(ScenicSpot).count() > 0:
            return

        # ===== 景点数据 =====
        spots_data = [
            ScenicSpot(
                name="海昏侯国遗址公园",
                alias="海昏侯墓",
                category="人文",
                description="汉代海昏侯刘贺的封国遗址，出土金器、青铜器、竹简等珍贵文物万余件，被誉为「汉代考古的百科全书」。",
                detail="海昏侯国遗址是中国迄今为止发现的面积最大、保存最好、内涵最丰富的汉代侯国聚落遗址。出土金器478件，总重量超过115公斤，青铜器、玉器、漆木器、竹简等各类珍贵文物1万余件（套）。",
                cover="/api/placeholder/haixu",
                address="南昌市新建区大塘坪乡",
                opening_hours="08:30-17:30",
                ticket_price="¥60",
                rating=4.8,
                visit_duration="2-3小时",
                best_season="春秋季",
                tags=["汉代", "考古", "国宝", "金色"],
                is_featured=True,
                sort_order=1,
            ),
            ScenicSpot(
                name="南矶山湿地自然保护区",
                alias="南矶山",
                category="生态",
                description="鄱阳湖西南岸的候鸟天堂，每年数十万只候鸟在此越冬，被誉为「珍禽王国，候鸟乐园」。",
                detail="南矶山是鄱阳湖流域最重要的候鸟栖息地之一，每年10月至次年3月，数以万计的候鸟从西伯利亚、蒙古等地飞来越冬。白鹤、白头鹤、白枕鹤等国家一级保护动物在此栖息。",
                cover="/api/placeholder/nanjishan",
                address="南昌市新建区南矶乡",
                opening_hours="全天开放",
                ticket_price="免费",
                rating=4.7,
                visit_duration="半天",
                best_season="冬季（观鸟季）",
                tags=["自然", "观鸟", "湿地", "生态"],
                is_featured=True,
                sort_order=2,
            ),
            ScenicSpot(
                name="厚田沙漠",
                alias="江南第一沙漠",
                category="自然",
                description="江南地区最大的沙漠景观，金色沙丘连绵起伏，与远处的赣江、绿洲构成奇特的沙漠绿洲画卷。",
                detail="厚田沙漠位于新建区西南部，面积约4.5万亩，是江南地区最大的沙漠自然景观。沙丘高10-30米，绵延起伏。这里集沙漠、绿洲、河流、草原于一体，被誉为「江南第一沙漠」。",
                cover="/api/placeholder/houtian",
                address="南昌市新建区厚田乡",
                opening_hours="08:00-18:00",
                ticket_price="¥30",
                rating=4.5,
                visit_duration="2-4小时",
                best_season="春秋季",
                tags=["沙漠", "摄影", "星空", "橙色"],
                is_featured=True,
                sort_order=3,
            ),
            ScenicSpot(
                name="西山万寿宫",
                alias="南昌万寿宫",
                category="人文",
                description="江南著名道教宫观，始建于晋代，为纪念许逊治水而建，已有1700余年历史。",
                detail="西山万寿宫是江南最著名的道教圣地之一，始建于公元370年（晋代），为纪念道教净明道创始人许逊（许真君）治水功绩而建。历史上曾与北京白云观、成都青羊宫齐名。",
                cover="/api/placeholder/wanshougong",
                address="南昌市新建区西山镇",
                opening_hours="07:00-17:30",
                ticket_price="¥25",
                rating=4.6,
                visit_duration="1-2小时",
                best_season="春秋季（农历正月祈福）",
                tags=["道教", "古建", "祈福", "历史"],
                is_featured=True,
                sort_order=4,
            ),
            ScenicSpot(
                name="梦山风景区",
                alias="梦山水库",
                category="自然",
                description="山水相依的静谧之地，湖水碧绿如玉，环山青翠欲滴，是城市近郊的天然氧吧。",
                detail="梦山风景区位于新建区北部，以梦山水库为核心，周围群山环抱，植被茂密。湖水清澈见底，倒映着青山绿树，四季景色各异。春天山花烂漫，夏季凉爽宜人，秋日层林尽染，冬季宁静致远。",
                cover="/api/placeholder/mengshan",
                address="南昌市新建区石埠镇",
                opening_hours="08:00-17:30",
                ticket_price="¥20",
                rating=4.4,
                visit_duration="2-3小时",
                best_season="春夏秋",
                tags=["山水", "徒步", "休闲", "蓝色"],
                sort_order=5,
            ),
            ScenicSpot(
                name="象山森林公园",
                alias="南昌后花园",
                category="生态",
                description="南昌近郊最大的城市森林公园，森林覆盖率达85%，是名副其实的「城市绿肺」。",
                detail="象山森林公园总面积约2.5万亩，森林覆盖率为85%，是南昌近郊面积最大、保存最完好的天然森林公园。园内有丰富的动植物资源，负氧离子含量极高。",
                cover="/api/placeholder/xiangshan",
                address="南昌市新建区象山镇",
                opening_hours="全天开放",
                ticket_price="免费",
                rating=4.3,
                visit_duration="半天",
                best_season="春秋季",
                tags=["森林", "氧吧", "徒步", "绿色"],
                sort_order=6,
            ),
            ScenicSpot(
                name="汪山土库",
                alias="江南豪宅",
                category="古建",
                description="清代大型围屋建筑群，程氏家族的府邸，素有「江南豪宅」之称，是赣派建筑的杰出代表。",
                detail="汪山土库始建于清乾隆年间，为程氏家族的聚居大宅。建筑群占地100余亩，房屋144间，规模宏大，布局严谨。融合了赣派建筑的典型特征：青砖黛瓦、马头墙、天井院落，内部雕梁画栋。",
                cover="/api/placeholder/wangshan",
                address="南昌市新建区大塘坪乡",
                opening_hours="08:30-17:00",
                ticket_price="¥30",
                rating=4.5,
                visit_duration="1-2小时",
                best_season="全年",
                tags=["古建", "赣派", "历史", "文化"],
                sort_order=7,
            ),
            ScenicSpot(
                name="溪霞怪石岭",
                alias="江南长城",
                category="自然",
                description="怪石嶙峋的山岭，形似一条蜿蜒的巨龙盘踞山巅，被誉爲「江南小长城」。",
                detail="溪霞怪石岭是一处典型的丹霞地貌景观，山体由红色砂岩构成，经亿万年的风化侵蚀，形成千姿百态的奇石景观。山脊上蜿蜒的步道宛如长城，被游客称为「江南小长城」。",
                cover="/api/placeholder/xixia",
                address="南昌市新建区溪霞镇",
                opening_hours="08:00-17:30",
                ticket_price="¥35",
                rating=4.4,
                visit_duration="2-3小时",
                best_season="秋冬季",
                tags=["丹霞", "登山", "摄影", "奇石"],
                sort_order=8,
            ),
        ]
        db.add_all(spots_data)
        db.flush()

        # ===== 路线数据 =====
        routes_data = [
            Route(
                name="汉风探秘一日游",
                subtitle="穿越千年，感受汉文化的厚重与辉煌",
                description="从海昏侯的璀璨金器到汪山土库的赣派建筑，一日领略新建的历史文化精髓。",
                duration="一日游",
                difficulty="轻松",
                spot_ids=[1, 7],
                tags=["文化", "历史", "经典"],
                is_featured=True,
                sort_order=1,
            ),
            Route(
                name="生态秘境两日游",
                subtitle="在山水之间，找回内心的宁静",
                description="走进南矶山的候鸟天堂，探访象山森林公园的天然氧吧，两天沉浸在大自然的怀抱。",
                duration="两日游",
                difficulty="适中",
                spot_ids=[2, 6],
                tags=["自然", "生态", "观鸟"],
                is_featured=True,
                sort_order=2,
            ),
            Route(
                name="沙漠星空之旅",
                subtitle="江南沙漠，星空篝火，别样的浪漫",
                description="白天滑沙嬉戏，晚上篝火露营，在厚田沙漠的星空下开启一段难忘之旅。",
                duration="一日游/两日游",
                difficulty="适中",
                spot_ids=[3],
                tags=["沙漠", "星空", "露营", "浪漫"],
                is_featured=True,
                sort_order=3,
            ),
            Route(
                name="问道祈福之旅",
                subtitle="参访千年道观，寻一方心灵的净土",
                description="拜谒西山万寿宫，在千年道观中感受道家文化的深邃与宁静。",
                duration="半日游",
                difficulty="轻松",
                spot_ids=[4],
                tags=["祈福", "宗教", "文化"],
                sort_order=4,
            ),
            Route(
                name="全域新建全景游",
                subtitle="串珠成链，一程尽览新建之美",
                description="三天两夜，从海昏侯到厚田沙漠，从万寿宫到南矶山，尽览新建的自然与人文精华。",
                duration="三日游",
                difficulty="挑战",
                spot_ids=[1, 2, 3, 4, 7],
                tags=["全景", "精华", "深入"],
                is_featured=True,
                sort_order=5,
            ),
        ]
        db.add_all(routes_data)

        # ===== 节日数据 =====
        festivals_data = [
            Festival(
                name="海昏汉韵文化节",
                date="2026年4月",
                location="海昏侯国遗址公园",
                description="以汉代文化为主题的大型节庆活动，包含汉服巡游、汉代礼仪展示、金器特展等精彩内容。",
                category="传统节庆",
                highlights=["汉服巡游", "金器特展", "汉代礼仪", "文创市集"],
                is_upcoming=True,
                sort_order=1,
            ),
            Festival(
                name="南矶山观鸟节",
                date="2026年11月-2027年3月",
                location="南矶山湿地自然保护区",
                description="每年冬季举办的观鸟盛会，数十万只候鸟在此栖息，是观鸟爱好者的天堂。",
                category="传统节庆",
                highlights=["候鸟观赏", "生态摄影", "自然教育", "湿地徒步"],
                is_upcoming=True,
                sort_order=2,
            ),
            Festival(
                name="厚田沙漠音乐节",
                date="2026年10月",
                location="厚田沙漠景区",
                description="在江南唯一的沙漠中，享受音乐与星空的碰撞。露营、篝火、音乐，别样的沙漠狂欢。",
                category="现代活动",
                highlights=["音乐演出", "星空露营", "篝火晚会", "沙漠运动"],
                is_upcoming=True,
                sort_order=3,
            ),
            Festival(
                name="西山万寿宫祈福庙会",
                date="2027年2月（农历正月）",
                location="西山万寿宫",
                description="传承千年的祈福庙会，新春之际到万寿宫烧香祈福，感受地道的年味与传统。",
                category="传统节庆",
                highlights=["新春祈福", "传统庙会", "民俗表演", "素食文化"],
                sort_order=4,
            ),
            Festival(
                name="新建丰收节",
                date="2026年9月",
                location="溪霞现代农业园",
                description="庆祝丰收的乡村盛会，采摘、农耕体验、乡土美食，感受田园生活的美好。",
                category="现代活动",
                highlights=["采摘体验", "农耕文化", "乡土美食", "亲子互动"],
                sort_order=5,
            ),
        ]
        db.add_all(festivals_data)

        db.commit()
        print(f"✅ 种子数据已导入: {len(spots_data)}个景点, {len(routes_data)}条路线, {len(festivals_data)}个节日")

    finally:
        db.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed_data()
    print("✅ 种子数据完成")
