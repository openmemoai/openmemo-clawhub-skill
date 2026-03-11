"""
Configuration for OpenMemo ClawHub Skill.
"""

import os

DEFAULT_ENDPOINT = "http://localhost:8765"
HEALTH_PATH = "/health"
MEMORY_WRITE_PATH = "/memory/write"
MEMORY_RECALL_PATH = "/memory/recall"
MEMORY_SEARCH_PATH = "/memory/search"
TASK_CHECK_PATH = "/memory/search"
HEALTH_TIMEOUT = 5
REQUEST_TIMEOUT = 10

MODE_BOOTSTRAP = "bootstrap"
MODE_MEMORY = "memory"


class SkillConfig:
    def __init__(self,
                 endpoint: str = "",
                 health_timeout: int = HEALTH_TIMEOUT,
                 request_timeout: int = REQUEST_TIMEOUT,
                 auto_detect: bool = True):
        self.endpoint = endpoint or os.environ.get("OPENMEMO_ENDPOINT", DEFAULT_ENDPOINT)
        self.health_timeout = health_timeout
        self.request_timeout = request_timeout
        self.auto_detect = auto_detect
