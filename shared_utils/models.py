"""SQLAlchemy models."""

from sqlalchemy import Column, Integer, String

from .db import Base


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    todo_count = Column(Integer)
    file_count = Column(Integer)
