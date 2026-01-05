from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from web.db import Base

class PromptRun(Base):
    __tablename__ = "prompt_runs"

    id = Column(Integer, primary_key=True)
    prompt_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    generation = relationship("Generation", back_populates="prompt_run", uselist=False)

class Generation(Base):
    __tablename__ = "generations"

    id = Column(Integer, primary_key=True)
    prompt_run_id = Column(Integer, ForeignKey("prompt_runs.id"), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    tags_json = Column(Text, nullable=False)  # store as JSON string
    model_version = Column(String(64), nullable=False, default="gpt2_finetuned")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    prompt_run = relationship("PromptRun", back_populates="generation")
    recommendations = relationship("Recommendation", back_populates="generation", cascade="all, delete-orphan")

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True)
    generation_id = Column(Integer, ForeignKey("generations.id"), nullable=False)

    track_id = Column(String(64), nullable=False)
    track_name = Column(String(255), nullable=False)
    artists = Column(String(255), nullable=False)
    spotify_url = Column(Text, nullable=False)
    popularity = Column(Integer, nullable=False, default=0)
    rank = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    generation = relationship("Generation", back_populates="recommendations")
