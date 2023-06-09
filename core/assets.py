from core.common.names import *
from core.common.constants import *

pics: Dict[str,Surface] = {}
fonts: Dict[str,Font] = {}

def load_assets():
    pics['clown'] = pg.image.load(here+"assets/clown.png")
    fonts['small'] = SysFont('monospace',15)
    fonts['medium'] = SysFont('monospace',25)
    fonts['big'] = SysFont('monospace',35)
    fonts['gigantic'] = SysFont('monospace',50)