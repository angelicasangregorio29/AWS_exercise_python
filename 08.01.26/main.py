import uuid
import datetime


projects: list[dict] =[]

def check_project_name(name: str , projects: list[dict]) -> bool:
    result: bool =False
    for p in projects:
        if p.name == name:
            result = True
        break
    return result

def create_project(name: str) -> dict:
  
    print(check_project_name(name ,projects))