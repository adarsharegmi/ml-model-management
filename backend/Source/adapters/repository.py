from Source.domain import model
from Source.adapters.orm import FileUpload
from Source.adapters.connection import get_connection


class FileUploadRepository:
    def __init__(self) -> None:
        get_connection()

    def _add(
        self,
        model: model.File,
    ):
        file = FileUpload(
            file_id=model.id_,
            name=model.name,
            source=model.source,
            active=model.active,
            parameters=model.parameters,
            placement_name=model.placement_name,
            effective_from=model.effective_from,
            effective_to=model.effective_to,
        )
        get_connection()
        file.save()

    def get(self, ref: str):
        object = FileUpload.filter(file_id=ref)
        return object

    def get_all(self):
        objects = FileUpload.objects.all()
        return objects[0]

    def update(self, model: model.File):
        object = FileUpload.filter(file_id=model.id)
        object.update()

    def change_file_status(self, id_: str):
        object = FileUpload.filter(file_id=model.id)
        object.update(active=False)
