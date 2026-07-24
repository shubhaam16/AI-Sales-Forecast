from uuid import UUID

from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectService:

    @staticmethod
    def get_all_projects(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get_project(db: Session, project_id: UUID):
        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    @staticmethod
    def create_project(db: Session, project: Project):
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def update_project(db: Session):
        db.commit()

    @staticmethod
    def delete_project(db: Session, project: Project):
        db.delete(project)
        db.commit()