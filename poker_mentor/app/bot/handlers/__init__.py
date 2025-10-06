from .start import router as start_router
from .profile import router as profile_router
from .statistics import router as statistics_router
from .analysis import router as analysis_router
from .quick_game import router as quick_game_router
from .game_setup import router as game_setup_router
from .learning import router as learning_router

__all__ = [
    "start_router",
    "profile_router", 
    "statistics_router",
    "analysis_router",
    "quick_game_router",
    "game_setup_router",
    "learning_router"
]