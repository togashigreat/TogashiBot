from importlib import import_module
import os

def loadModule():
    global commmands
    BOT = f"\x1B[1;38;5;210m[ Togashi ]->\x1B[0m"
    commmands = {}
    for filename in os.listdir("./cmd/"):
        if filename.endswith(".py") and not filename.startswith("__"):
            commmand_name = os.path.splitext(filename)[
                0
            ]  # Remove the '.py' extensionmodule_name
            module_name = f"cmd.{commmand_name}"  # Build the module name
            module = import_module(module_name)
            # getting hasPermission  for command handling
            perm_lvl = module.info["hasPermission"]

            """ Get the function from the module with the same name as module """

            if hasattr(module, commmand_name):
                commmand_function = getattr(module, commmand_name)
                commmands[commmand_name] = (
                    commmand_function,
                    perm_lvl,
                )  # adding commmands in dictionary
            print(
                f"{BOT} \x1B[1;38;5;33mSuccesfully Loadded module: {commmand_name}\x1B[0m"
            )
    return commmands


commmands: dict = loadModule()
