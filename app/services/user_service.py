from sqlalchemy.orm import Session
from app.models.user import User
from uuid import UUID 


class UserService :
    @staticmethod
    def get_all_users(db:Session):
        return db.query(User).all()
    
    @staticmethod
    def get_user(db:Session , user_id: UUID ):
        return db.query(User).filter(User.id==user_id).first()
    
    @staticmethod
    def create_user(db:Session , user:User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def delete_user(db: Session, user: User):
        db.delete(user)
        db.commit()

    @staticmethod
    def update_user(db: Session):
        db.commit()