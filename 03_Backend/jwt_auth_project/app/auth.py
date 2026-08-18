from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, LoginRequest,Token,ChangePassword,RefreshTokenRequest
from app.security import hash_password,verify_password,create_access_token,create_refresh_token
from app.dependencies import get_current_user
from app.security import (
    SECRET_KEY,
    ALGORITHM,
)

router = APIRouter()

@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user.email).first()

    if existing_email:
        raise HTTPException(status_code=409, detail="Email already registered")

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})

    refresh_token = create_refresh_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/change-password")
def change_password(
    request: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    if not verify_password(request.current_password, current_user.hashed_password):
        raise HTTPException(status_code=401, detail="Current password is incorrect")

    new_hashed_password = hash_password(request.new_password)

    current_user.hashed_password = new_hashed_password

    db.commit()
    db.refresh(current_user)

    return {"message": "Password updated successfully"}

@router.post("/refresh")
def refresh_token(request: RefreshTokenRequest):
    try:

        payload = jwt.decode(
            request.refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token"
            )

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )
    new_access_token = create_access_token(data={"sub": username})
    return {"access_token": new_access_token, "token_type": "bearer"}
