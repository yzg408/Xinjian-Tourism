"""新建大观 · FastAPI 后端入口"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import json

from backend.database import init_db, get_db, engine
from backend.models import Base, ScenicSpot, Route, Festival, Feedback, TourPlan
from backend.schemas import (
    ScenicSpotCreate, ScenicSpotUpdate, ScenicSpotResponse,
    RouteCreate, RouteResponse, RouteDetailResponse,
    FestivalCreate, FestivalResponse,
    FeedbackCreate, FeedbackResponse,
    TourPlanCreate, TourPlanResponse,
)
from backend.seed import seed_data

app = FastAPI(
    title="新建大观 API",
    description="新建区全域智慧文旅平台后端接口",
    version="1.0.0",
)

# CORS — 允许前端调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    seed_data()


# ========== 景点 Scenic Spots ==========

@app.get("/api/scenic-spots", response_model=List[ScenicSpotResponse])
def list_spots(
    category: Optional[str] = None,
    featured: Optional[bool] = None,
    search: Optional[str] = None,
    tag: Optional[str] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    q = db.query(ScenicSpot).filter(ScenicSpot.is_active == True)
    if category:
        q = q.filter(ScenicSpot.category == category)
    if featured:
        q = q.filter(ScenicSpot.is_featured == True)
    if search:
        q = q.filter(ScenicSpot.name.contains(search) | ScenicSpot.description.contains(search))
    if tag:
        q = q.filter(ScenicSpot.tags.contains(tag))
    q = q.order_by(ScenicSpot.sort_order).offset(skip).limit(limit)
    return q.all()


@app.get("/api/scenic-spots/categories")
def list_categories(db: Session = Depends(get_db)):
    results = db.query(ScenicSpot.category).filter(
        ScenicSpot.is_active == True, ScenicSpot.category.isnot(None)
    ).distinct().all()
    return [r[0] for r in results]


@app.get("/api/scenic-spots/{spot_id}", response_model=ScenicSpotResponse)
def get_spot(spot_id: int, db: Session = Depends(get_db)):
    spot = db.query(ScenicSpot).filter(ScenicSpot.id == spot_id).first()
    if not spot:
        raise HTTPException(status_code=404, detail="景点不存在")
    return spot


@app.post("/api/scenic-spots", response_model=ScenicSpotResponse)
def create_spot(spot: ScenicSpotCreate, db: Session = Depends(get_db)):
    db_spot = ScenicSpot(**spot.model_dump())
    db.add(db_spot)
    db.commit()
    db.refresh(db_spot)
    return db_spot


@app.patch("/api/scenic-spots/{spot_id}", response_model=ScenicSpotResponse)
def update_spot(spot_id: int, spot: ScenicSpotUpdate, db: Session = Depends(get_db)):
    db_spot = db.query(ScenicSpot).filter(ScenicSpot.id == spot_id).first()
    if not db_spot:
        raise HTTPException(status_code=404, detail="景点不存在")
    for key, val in spot.model_dump(exclude_unset=True).items():
        setattr(db_spot, key, val)
    db.commit()
    db.refresh(db_spot)
    return db_spot


# ========== 路线 Routes ==========

@app.get("/api/routes", response_model=List[RouteResponse])
def list_routes(
    featured: Optional[bool] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    q = db.query(Route).filter(Route.is_active == True)
    if featured:
        q = q.filter(Route.is_featured == True)
    q = q.order_by(Route.sort_order).offset(skip).limit(limit)
    return q.all()


@app.get("/api/routes/{route_id}", response_model=RouteDetailResponse)
def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        raise HTTPException(status_code=404, detail="路线不存在")
    spots = []
    if route.spot_ids:
        spots = db.query(ScenicSpot).filter(ScenicSpot.id.in_(route.spot_ids), ScenicSpot.is_active == True).all()
        # Preserve order from spot_ids
        spot_map = {s.id: s for s in spots}
        spots = [spot_map[sid] for sid in route.spot_ids if sid in spot_map]
    return RouteDetailResponse(**route.__dict__, spots=spots)


@app.post("/api/routes", response_model=RouteResponse)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    db_route = Route(**route.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


# ========== 节日 Festivals ==========

@app.get("/api/festivals", response_model=List[FestivalResponse])
def list_festivals(
    category: Optional[str] = None,
    upcoming: Optional[bool] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    q = db.query(Festival).filter(Festival.is_active == True)
    if category:
        q = q.filter(Festival.category == category)
    if upcoming:
        q = q.filter(Festival.is_upcoming == True)
    q = q.order_by(Festival.sort_order).offset(skip).limit(limit)
    return q.all()


@app.get("/api/festivals/{festival_id}", response_model=FestivalResponse)
def get_festival(festival_id: int, db: Session = Depends(get_db)):
    festival = db.query(Festival).filter(Festival.id == festival_id).first()
    if not festival:
        raise HTTPException(status_code=404, detail="活动不存在")
    return festival


@app.post("/api/festivals", response_model=FestivalResponse)
def create_festival(festival: FestivalCreate, db: Session = Depends(get_db)):
    db_festival = Festival(**festival.model_dump())
    db.add(db_festival)
    db.commit()
    db.refresh(db_festival)
    return db_festival


# ========== 反馈 Feedback ==========

@app.post("/api/feedback", response_model=FeedbackResponse)
def submit_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = Feedback(**feedback.model_dump())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


# ========== 定制旅程 Tour Plans ==========

@app.post("/api/tour-plans", response_model=TourPlanResponse)
def submit_tour_plan(plan: TourPlanCreate, db: Session = Depends(get_db)):
    db_plan = TourPlan(**plan.model_dump())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


# ========== 健康检查 ==========

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "新建大观 API", "version": "1.0.0"}


# ========== 统计 ==========

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    return {
        "scenic_spots": db.query(ScenicSpot).filter(ScenicSpot.is_active == True).count(),
        "routes": db.query(Route).filter(Route.is_active == True).count(),
        "festivals": db.query(Festival).filter(Festival.is_active == True).count(),
        "feedbacks": db.query(Feedback).count(),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
