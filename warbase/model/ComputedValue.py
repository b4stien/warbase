from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint, Index

from . import Base


class ComputedValue(Base):
    __tablename__ = 'wb_computed_values'
    id = Column(Integer, primary_key=True)

    key = Column(String)
    target_id = Column(Integer)

    expired = Column(Boolean)
    value = Column(Integer)

    datetime = Column(DateTime, index=True)

    __table_args__ = (
        UniqueConstraint('key', 'target_id'),
        Index('idx_computed_values', 'key', 'target_id'))
