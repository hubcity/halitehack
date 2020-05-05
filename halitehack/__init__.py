from kaggle_environments.core import register
import kaggle_environments.envs.halite.halite as original_halite
import halitehack.halitehack as hack

# Register Environment
register("halitehack", {
    "agents": original_halite.agents,
    "html_renderer": hack.html_renderer,
    "interpreter": hack.interpreter,
    "renderer": original_halite.renderer,
    "specification": hack.specification,
})
