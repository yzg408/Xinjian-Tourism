"""新建大观 · Pydantic 数据模型"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ===== 景点 =====
class ScenicSpotBase(BaseModel):
    name: str
    alias: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    detail: Optional[str] = None
    cover: Optional[str] = None
    images: Optional[List[str]] = None
    address: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    opening_hours: Optional[str] = None
    ticket_price: Optional[str] = None
    rating: Optional[float] = 4.5
    visit_duration: Optional[str] = None
    best_season: Optional[str] = None
    tags: Optional[List[str]] = None
    is_featured: bool = False
    sort_order: int = 0


class ScenicSpotCreate(ScenicSpotBase):
    pass


class ScenicSpotUpdate(BaseModel):
    name: Optional[str] = None
    alias: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    detail: Optional[str] = None
    cover: Optional[str] = None
    images: Optional[List[str]] = None
    address: Optional[str] = None
    opening_hours: Optional[str] = None
    ticket_price: Optional[str] = None
    rating: Optional[float] = None
    visit_duration: Optional[str] = None
    best_season: Optional[str] = None
    tags: Optional[List[str]] = None
    is_featured: Optional[bool] = None
    sort_order: Optional[int] = None


class ScenicSpotResponse(ScenicSpotBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ===== 路线 =====
class RouteBase(BaseModel):
    name: str
    subtitle: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    duration: Optional[str] = None
    difficulty: Optional[str] = None
    spot_ids: Optional[List[int]] = None
    tags: Optional[List[str]] = None
    is_featured: bool = False
    sort_order: int = 0


class RouteCreate(RouteBase):
    pass


class RouteResponse(RouteBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RouteDetailResponse(RouteResponse):
    spots: List[ScenicSpotResponse] = []


# ===== 节日 =====
class FestivalBase(BaseModel):
    name: str
    date: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    images: Optional[List[str]] = None
    category: Optional[str] = None
    highlights: Optional[List[str]] = None
    is_upcoming: bool = False
    sort_order: int = 0


class FestivalCreate(FestivalBase):
    pass


class FestivalResponse(FestivalBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ===== 反馈 =====
class FeedbackCreate(BaseModel):
    name: Optional[str] = None
    contact: Optional[str] = None
    content: str
    category: str = "general"


class FeedbackResponse(BaseModel):
    id: int
    name: Optional[str] = None
    contact: Optional[str] = None
    content: str
    category: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ===== 定制旅程 =====
class TourPlanCreate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    days: Optional[int] = None
    preferences: Optional[str] = None
    contact_time: Optional[str] = None


class TourPlanResponse(BaseModel):
    id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    days: Optional[int] = None
    preferences: Optional[str] = None
    contact_time: Optional[str] = None
    status: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
