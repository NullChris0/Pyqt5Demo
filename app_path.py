import sys
import os
def get_app_path():
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return f'{os.path.dirname(sys.executable)}/_internal'
    return os.path.dirname(__file__)

