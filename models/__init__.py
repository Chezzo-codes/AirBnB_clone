#!/usr/bin/python3
"""
Instantiation file that starts the file storage system
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
