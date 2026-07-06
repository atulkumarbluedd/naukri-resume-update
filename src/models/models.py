
from dataclasses import dataclass, field
import time
from typing import Any, Dict


@dataclass
class NaukriSession:
    bearer_token: str
    cookies: dict
    login_time: float = field(default_factory=time.time)

@dataclass
class FileValidationResult:
    file_key: str
    raw_response: dict
    was_key_remapped: bool

@dataclass
class ResumeUpdateResult:
    profile_id: str
    raw_response: dict
    status_code: int



@dataclass
class ProfileUpdateResult:
    profile_id: str
    response: Dict[str, Any]
    status_code: int



