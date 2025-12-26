from fastapi import Request, HTTPException, status

def get_current_user(request: Request):
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated",
        )

    if user.get("stake_level_id") != 3:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized Access",
        )

    return user

def get_current_admin(request: Request):
    user = getattr(request.state, "user", None)
    # print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated admin",
        )

    if user.get("stake_level_id") != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return user

def get_current_user_admin(request: Request):
    # print("get_current_user_admin")
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated",
        )

    if user.get("stake_level_id") != 2 or user.get("stake_level_id") != 3:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin/User access required",
        )

    return user