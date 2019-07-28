from typing import Union
from uuid import uuid4

from sqlalchemy import Column, String

from app import wrapper


class Template(wrapper.Base):
    __tablename__: str = "Template"

    uuid: Union[Column, str] = Column(String(36), primary_key=True, unique=True)

    @property
    def serialize(self) -> dict:
        _: str = self.uuid
        d: dict = self.__dict__.copy()

        del d["_sa_instance_state"]

        return d

    @staticmethod
    def create() -> "Template":
        uuid: str = str(uuid4())

        template: Template = Template(uuid=uuid)

        wrapper.session.add(template)
        wrapper.session.commit()

        return template
