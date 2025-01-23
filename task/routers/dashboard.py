from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User, Task, Team
from ..auth import get_current_user

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard/user-dashboard")
def user_dashboard(db: Session = Depends(get_db), 
        current_user: User = Depends(get_current_user)):
    
    assigned_tasks = db.query(Task).filter(Task.assignee_id == current_user.id).all()

    created_tasks = db.query(Task).filter(Task.creator_id == current_user.id).all()

    review_tasks = db.query(Task).filter(Task.reviewer_id == current_user.id).all()


    dashboard_data = {
        "user_id": current_user.id,
        "user_name": current_user.username,
        "assigned_tasks": assigned_tasks,
        "created_tasks": created_tasks,
        "review_tasks": review_tasks,
    }

    return dashboard_data



@router.get("/dashboard/admin-dashboard")
def admin_dashboard(db:Session = Depends(get_db), 
        current_user: User = Depends(get_current_user)
    ):

    total_tasks = db.query(Task).count()
    total_user = db.query(User).count()
    total_team = db.query(Team).count()

    recent_tasks = db.query(Task).order_by(Task.created_at.desc()).limit(5).all()
    recent_users = db.query(User).order_by(User.id.desc()).limit(5).all()
    recent_teams = db.query(Team).order_by(Team.id.desc()).limit(5).all()


    all_data={
        "total_counts":{
            "total_tasks": total_tasks,
            "total_users": total_user,
            "total_team": total_team
        },
        "all_data":{
            "Tasks": recent_tasks,
            "users": recent_users,
            "teams": recent_teams
        }
    }
    return all_data


# @router.get("/dashboard/team-dashboard")
# def get(db:Session = Depends(get_db), 
#         current_user: User = Depends(get_current_user)
#     ):

    
