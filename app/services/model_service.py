from app.models.trained_model import TrainedModel
from uuid import UUID
from sqlalchemy.orm import Session
from app.schemas.trained_model import TrainedModelCreate

class ModelService:

    @staticmethod
    def create_model (db:Session , model_data:TrainedModelCreate)->TrainedModel:
        trained_model = TrainedModel(
            project_id=model_data.project_id,
            dataset_id=model_data.dataset_id,
            model_name=model_data.model_name,
            algorithm=model_data.algorithm,
            model_path=model_data.model_path,
            mae=model_data.mae,
            rmse=model_data.rmse,
            r2_score=model_data.r2_score
        )
        db.add(trained_model)
        db.commit()
        db.refresh(trained_model)
        return trained_model


    @staticmethod
    def get_all_model (db:Session):
        return db.query(TrainedModel).all()

    @staticmethod
    def get_model(db:Session , model_id:UUID  )->TrainedModel:
        return db.query(TrainedModel).filter(TrainedModel.id == model_id).first()

    @staticmethod
    def list_models(db:Session , project_id:UUID):
        return db.query(TrainedModel).filter(TrainedModel.project_id==project_id).order_by(TrainedModel.created_at.desc()).all()

    @staticmethod
    def delete_model (db:Session , model_id :UUID)-> bool:
        model= db.query(TrainedModel).delete(TrainedModel.id==model_id).first()
        if not model:
            return False
        db.delete(model)
        db.commit

        @staticmethod
        def active_model(db:Session , model_id = UUID)->TrainedModel | None:
            model = db.query(TrainedModel).filter(TrainedModel.id == model_id).first()
            if not model:
                return False
            db.query(TrainedModel).filter(TrainedModel.project_id==model.project_id).update({TrainedModel.is_active:False})
            model.is_active=True

            db.commit()
            db.refresh (model)
            return model
        