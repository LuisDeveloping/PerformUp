# app/modules/users/domain/entities/user.py

from uuid import UUID
from datetime import datetime


class User:
    def __init__(
        self,
        id: UUID,
        email: str,
        password_hash: str,
        is_active: bool,
        created_at: datetime,
        updated_at: datetime
    ):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        
    def deactivate(self):
        if not self.is_active:
            raise ValueError("User is already inactive")

        self.is_active = False

    def activate(self):
        if self.is_active:
            raise ValueError("User is already active")

        self.is_active = True