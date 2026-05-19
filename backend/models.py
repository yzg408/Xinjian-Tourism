"""新建大观 · 数据模型"""
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from backend.database import Base


class ScenicSpot(Base):
    """景点"""
    __tablename__ = "scenic_spots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, comment="景点名称")
    alias = Column(String(100), comment="别名")
    category = Column(String(50), comment="分类: 自然/人文/古建/生态")
    description = Column(Text, comment="简介")
    detail = Column(Text, comment="详细介绍")
    cover = Column(String(500), comment="封面图URL")
    images = Column(JSON, comment="多图URL数组")
    address = Column(String(200), comment="地址")
    longitude = Column(Float, comment="经度")
    latitude = Column(Float, comment="纬度")
    opening_hours = Column(String(100), comment="开放时间")
    ticket_price = Column(String(100), comment="门票价格")
    rating = Column(Float, default=4.5, comment="评分")
    visit_duration = Column(String(50), comment="建议游玩时长")
    best_season = Column(String(100), comment="最佳游玩季节")
    tags = Column(JSON, comment="标签数组")
    is_featured = Column(Boolean, default=False, comment="是否推荐")
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Route(Base):
    """旅游路线"""
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, comment="路线名称")
    subtitle = Column(String(200), comment="副标题")
    description = Column(Text, comment="路线简介")
    cover = Column(String(500), comment="封面图")
    duration = Column(String(50), comment="行程时长（如：一日游/两日游）")
    difficulty = Column(String(20), comment="难度等级")
    spot_ids = Column(JSON, comment="包含景点ID数组（有序）")
    tags = Column(JSON, comment="标签")
    is_featured = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Festival(Base):
    """节日活动"""
    __tablename__ = "festivals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, comment="活动名称")
    date = Column(String(50), comment="举办日期")
    location = Column(String(200), comment="举办地点")
    description = Column(Text, comment="活动简介")
    cover = Column(String(500), comment="封面图")
    images = Column(JSON, comment="多图")
    category = Column(String(50), comment="类型: 传统节庆/现代活动/文化体验")
    highlights = Column(JSON, comment="活动亮点")
    is_upcoming = Column(Boolean, default=False, comment="是否即将举办")
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Feedback(Base):
    """用户反馈"""
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), comment="用户昵称")
    contact = Column(String(100), comment="联系方式")
    content = Column(Text, nullable=False, comment="反馈内容")
    category = Column(String(30), default="general", comment="分类")
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class TourPlan(Base):
    """定制旅程"""
    __tablename__ = "tour_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), comment="旅客姓名")
    phone = Column(String(20), comment="电话")
    days = Column(Integer, comment="计划天数")
    preferences = Column(Text, comment="偏好描述")
    contact_time = Column(String(50), comment="联系时间")
    status = Column(String(20), default="pending", comment="状态: pending/contacted/completed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
