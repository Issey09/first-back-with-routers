from sqlalchemy.orm import Session

from src import models, schemas


def create_user(db: Session, user: schemas.User):
    db_user = models.Users(nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#