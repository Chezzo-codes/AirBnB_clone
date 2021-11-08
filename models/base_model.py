#!/usr/bin/python3
"""
Module contains BaseModel class
"""
import uuid
import datetime


class BaseModel:
    """
    class BaseModel that defines all
    common attributes/methods for other classes
    """
    def __init__(self):
        """
        Initialize instances
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        prints str format of class instance
        """
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__ ))

    def save(self):
        """
        updates update_at - time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        pass
    
