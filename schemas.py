"""
Database Schemas for Elder Care Service

Each Pydantic model represents a collection in MongoDB.
Collection name is the lowercase of the class name.

Examples:
- CareRequest -> "carerequest" collection
- Caregiver -> "caregiver" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Literal
from datetime import date

class CareRequest(BaseModel):
    """
    Care requests submitted by families/clients
    Collection: "carerequest"
    """
    full_name: str = Field(..., description="Requestor's full name")
    email: Optional[EmailStr] = Field(None, description="Contact email")
    phone: str = Field(..., description="Contact phone number")
    address: str = Field(..., description="Service address")
    preferred_dates: Optional[List[date]] = Field(None, description="Preferred service dates")
    preferred_time_window: Optional[str] = Field(None, description="e.g., 'mornings', 'evenings', 'overnight'")
    services: List[Literal[
        "house_cleaning",
        "meal_preparation",
        "toileting_support",
        "companionship",
        "medication_reminders",
        "shopping_errands",
        "overnight"
    ]] = Field(..., description="Selected services")
    notes: Optional[str] = Field(None, description="Additional details or special needs")

class Caregiver(BaseModel):
    """
    Caregiver profiles
    Collection: "caregiver"
    """
    name: str = Field(..., description="Caregiver full name")
    years_experience: int = Field(..., ge=0, le=60)
    specialties: List[str] = Field(default_factory=list)
    can_overnight: bool = Field(False)
    availability: List[str] = Field(default_factory=list, description="e.g., ['mornings', 'evenings', 'weekends']")
    bio: Optional[str] = Field(None)
    rating: Optional[float] = Field(None, ge=0, le=5)

# You can add more schemas like Client, Booking, etc., later if needed.
