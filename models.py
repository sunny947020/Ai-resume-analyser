from sqlalchemy import column, integer, string, text, foreignkey
from db import Base

class User(Base):
    __tablename__ = "users"
    id = column(Integer, primary_key=True, index=True)
    name = column(String(255), nullable=False)
    email = column(String(255), unique=True, index=True, nullable=False)
    password = column(String(255), nullable=False)

    cllass reports(Base):
    __tablename__ = "reports"
    id = column(Integer, primary_key=True, index=True)
    user_id = column(Integer, ForeignKey("users.id"), nullable=False)
    resume_text = column(Text, nullable=False
    result = column(Text, nullable=False))
    

