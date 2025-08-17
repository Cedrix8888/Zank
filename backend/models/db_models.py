from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

# 基础模型类,所有数据库模型都继承此类
Base = declarative_base()

class User(Base):
    """用户模型,存储系统用户信息"""
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)  # 存储加密后的密码
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 与AI生成结果建立一对多关系
    ai_results = relationship("AIResult", back_populates="user", cascade="all, delete-orphan")

class AIResult(Base):
    """AI生成结果模型,存储所有AI交互记录"""
    __tablename__ = "ai_results"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    prompt = Column(Text, nullable=False)  # 用户输入的提示词
    content = Column(Text, nullable=False)  # AI生成的内容
    model_name = Column(String(100), nullable=False)  # 使用的AI模型名称
    request_id = Column(String(36), unique=True, nullable=False, index=True)  # 用于追踪请求的唯一ID
    is_successful = Column(Boolean, default=True)  # 标记生成是否成功
    processing_time = Column(String(20))  # 处理时间（毫秒）
    created_at = Column(DateTime, default=datetime.utcnow, index=True)  # 生成时间
    
    # 关联到用户
    user = relationship("User", back_populates="ai_results")

class ModelUsage(Base):
    """模型使用统计,用于跟踪不同AI模型的调用情况"""
    __tablename__ = "model_usage"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    model_name = Column(String(100), nullable=False, index=True)
    total_calls = Column(String(20), default="0")  # 总调用次数
    total_tokens = Column(String(20), default="0")  # 总消耗token数（如适用
    last_used = Column(DateTime, default=datetime.utcnow)  # 最后使用时间
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    