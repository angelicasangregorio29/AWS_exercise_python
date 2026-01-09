"""
Progetti, task e tag hanno ciascuno un ID univoco (uuid).

Task ha: titolo (univoco), completato sì/no, riferimento al progetto, lista di tag, date di creazione/completamento.
"""

import uuid
import datetime

projects: list[dict] = [{'id': 'b3d79aaf-4c9e-41a3-9e6a-b1bb977da4e5', 'name': 'pippo', 'description': 'boh', 'createdAt': '2026-01-08T08:56:27.826Z'}]
tasks: list[dict] = []

def create_task(title: str, project_id: str, tags: list) -> dict:
    """crea un elemento task"""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),
        'title': title,
        "project_id": project_id,
        "tags": tags,
        'is_completed': False,
        'created_at': clean_date,
        'completed_at': None
    }

def check_task_name(title: str, tasks: list[dict]) -> bool: 
    """verifica che non esista una task con lo stesso nome"""
    result: bool = False
    for t in tasks:
        if t['title'] == title:
            result = True
            break 
    return result 
    

def check_project_name(name: str, projects: list[dict]) -> bool: 
    """verifica che non esista un progetto con lo stesso nome"""
    result: bool = False
    for p in projects:
        if p['name'] == name:
            result = True
            break 
    return result 

def create_project(name: str, description: str = "") -> dict:
    """crea un elemento progetto"""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),
        'name': name,
        'description': description,
        'createdAt': clean_date
    }

def save_task(title: str, project_id: str, tags: list ) -> None:
    """salva il progetto nel db"""
    if check_task_name(title, tasks):
        raise ValueError(f"Il task '{title}' esiste già!")

    task = create_task(title, project_id, tags)
    tasks.append(task)
    print(tasks)

def save_project(name: str, description: str = "") -> None:
    """salva il progetto nel db"""
    if check_project_name(name, projects):
        raise ValueError(f"Il progetto '{name}' esiste già!")

    project = create_project(name, description)
    projects.append(project)
    print(projects)
     


def main() -> None: 
    try:
        print(save_task("compra pomodori", 'b3d79aaf-4c9e-41a3-9e6a-b1bb977da4e5', ["spesa"]))
        print(save_task("compra pomodori", 'b3d79aaf-4c9e-41a3-9e6a-b1bb977da4e5', ["spesa"]))

    except ValueError as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()