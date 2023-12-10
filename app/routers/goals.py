from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List

router = APIRouter()


class GoalType(str, Enum):
    habit = "habit"
    milestone = "milestone"


class Goal(BaseModel):
    id: int
    type: GoalType
    title: str
    description: str
    progress: float
    archived: bool
    completed: bool


goals_store: List[Goal] = [
    Goal(
        id=1,
        type=GoalType.habit,
        title="sleep",
        description="get rest",
        progress=0.1,
        archived=False,
        completed=False,
    )
]


@router.get("/goals", tags=["goals"])
async def get_goals():
    # This endpoint should:
    # - get all goals from the datastore
    # - return 200 status code with all goals
    return goals_store


@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goal_id: str):
    # This endpoint should:
    # - take goal_id from the path of the URL
    # - get goal with such id from datastore
    # - return 200 status code on success with the goal
    # - return 404 error status code when there is none
    return


@router.get("/goals/{username}", tags=["goals"])
async def get_user_goals(username: str):
    # This endpoint should:
    # - take username/userID from the path of the URL
    # - take all goal with such user in the datastore
    # - return 200 status code on success with the list of goals even if empty
    return [{"goal": "Learn Python"}]


@router.post("/goals", tags=["goals"])
async def post_goal(goal):
    # This endpoint should:
    # - take goal_id from the URL path and get goal with such ID from datastore
    # - take goal passed in the request body, and change corresponding fields in the one got from datastore
    # - return 200 status code on success and the updated goal
    # - return 404 when there is no goal with such id in datastore
    return ""


@router.put("/goals/{goal_id}", tags=["goals"])
async def update_goal(goal_id: int, goal: Goal) -> Goal:
    # This endpoint should:

    # - take goal_id from the URL path and get goal with such ID from datastore
    g = next((x for x in goals_store if x.id == goal_id), None)

    # - return 404 when there is no goal with such id in datastore
    if g is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # - take goal passed in the request body, and change corresponding fields (we only want it to change title, description and maybe something more in the future )
    # - update the goal in the datastore
    # - return 200 status code on success and the updated goal
    # - return 404 when there is no goal with such id in datastore
    for i in range(len(goals_store)):
        if goals_store[i].id == goal_id:
            goals_store[i].title = goal.title
            goals_store[i].description = goal.description
            return goals_store[i]
    return


@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: str):
    # This endpoint should:
    # - delete goals with given ID from datastore
    # - return 204 status code on success
    # - return 404 when there is no goal with such id in datastore
    return


@router.post("/goals/{goal_id}", tags=["goals"])
async def post_progress_goal(goal_id: str, progress: float):
    # This endpoint should:
    # - similarly like an update endpoint, take goal_id from path for the goal to search for in datastore
    # - update progress model in body
    # - update given goal with progress, and check if it's positive number, and not greater then 100 while it will represent percents
    # - return 200 on success and updated goal
    # - return 404 when there is no goal with such id in datastore
    return

@router.post("/goals/{goal_id}/archive", tags=["goals"])
async def archive_goal(goal_id: str) -> (int, Goal):

    goal = get_goal(goal_id)

    if goal is None:
        return (404, None)
    
    goal.archived = not goal.archived
    
    update_goal(goal_id, goal)
    
    return (200, goal)

@router.post("/goals/{goal_id}/complete", tags=["goals"])
async def complete_goal(goal_id: str):
    # This endpoint should:
    # - similarly like an update endpoint, take goal_id from path for the goal to search for in datastore
    # - change "completed" property of goal from false to true or vice versa
    # - return 200 on success and archived goal
    # - return 404 when there is no goal with such id in datastore
    return
