from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP
)
from sqlalchemy.sql import func
from database.db import Base
class AIInsight(Base):
    __tablename__ = "ai_insights"
    id = Column( Integer, 
        primary_key=True
    )
    insight_type = Column( 
        String(100)
    )
    title = Column(
        String(255)
    )
    content = Column(
        Text
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )