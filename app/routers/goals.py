from fastapi import APIRouter
from .goal import GoalType, Goal
router = APIRouter()

@router.get("/goals", tags=["goals"])
async def get_goals():
    # This endpoint should:
    # - get all goals from the datastore
    # - return 200 status code with all goals
    return []

@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goal_id: str):
    if goal_id in datastore:
        goal = datastore[goal_id]
        return goal
    else:
        # If goal_id not found, raise HTTPException with 404 status code
        raise HTTPException(status_code=404, detail="Goal not found")
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
async def update_goal(goal_id: str, goal): 
    # This endpoint should:
    # - take goal_id from the URL path and get goal with such ID from datastore
    # - take goal passed in the request body, and change corresponding fields (we only want it to change title, description and maybe something more in the future )
    # - update the goal in the datastore
    # - return 200 status code on success and the updated goal
    # - return 404 when there is no goal with such id in datastore
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
async def archive_goal(goal_id: str): 
    # This endpoint should:
    # - similarly like an update endpoint, take goal_id from path for the goal to search for in datastore
    # - change "archived" property of goal from false to true or vice versa
    # - return 200 on success and archived goal 
    # - return 404 when there is no goal with such id in datastore
    return 

@router.post("/goals/{goal_id}/complete", tags=["goals"])
async def complete_goal(goal_id: str): 
    # This endpoint should:
    # - similarly like an update endpoint, take goal_id from path for the goal to search for in datastore
    # - change "completed" property of goal from false to true or vice versa
    # - return 200 on success and archived goal 
    # - return 404 when there is no goal with such id in datastore
    return 