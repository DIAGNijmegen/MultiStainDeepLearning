import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pathlib import Path

from utils import read_json


# def build_custom_colormap(data, name):
#     color_values = np.array(data["color_values"])
#     color_values -= color_values[0]
#     color_values = color_values / color_values[-1]
#     color_names = data["color_names"]
#     cMap = list(zip(color_values, color_names))
#     custom_cmap = LinearSegmentedColormap.from_list(name, cMap)
#     return custom_cmap

def build_custom_colormap(data, name):
    cmap_type = data["type"]
    cmap_args = data["args"]

    if cmap_type == "LinearSegmentedColormap.from_list":
        colors = cmap_args["colors"]
        custom_cmap = LinearSegmentedColormap.from_list(name, colors)
    elif cmap_type == "LinearSegmentedColormap":
        segmentdata = cmap_args["segmentdata"]
        custom_cmap = LinearSegmentedColormap(name, segmentdata)
    elif cmap_type == "ListedColormap":
        colors = cmap_args["colors"]
        custom_cmap = ListedColormap(colors, name=name)
    else:
        print(f"Unsupported colormap type: {cmap_type}")
        return None

    return custom_cmap


def get_custom_colormaps(cmap_path="colormaps.json"):
    cmap_dict = read_json(Path(cmap_path))
    cmaps = []
    for cmap_name in cmap_dict:
        data = cmap_dict[cmap_name]
        cmap = build_custom_colormap(data, cmap_name)
        if cmap is not None:
            cmaps.append((cmap_name, cmap))
    return cmaps

custom_cmaps = get_custom_colormaps("./utils/colormaps.json")
for name, cmap in custom_cmaps:
    plt.colormaps.register(cmap)


# Preview custom color maps by running this script on its own. Requires some changes to the imports to work,
# but I'm leaving this in in case it's needed again later.
if __name__ == "__main__":
    def plot_examples(cmaps):
        """
        Helper function to plot data with associated colormap.
        Code adapted from https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
        """
        data = np.random.randn(30, 30)
        n = len(cmaps)
        fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3), constrained_layout=True, squeeze=False)
        for [ax, (name, cmap)] in zip(axs.flat, cmaps):
            psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
            fig.colorbar(psm, ax=ax)
            ax.set_title(name)
        plt.show()
    plot_examples(custom_cmaps)



# ### OLD VERSION BELOW:

# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.cm as cm
# import matplotlib.colors as mplcolors
# from pathlib import Path

# from utils import read_json


# def build_custom_colormap(data, name):
#     type_str = data["type"]
#     type_str = type_str.split(".")
#     constructor = mplcolors
#     for s in type_str:
#         try:
#             constructor = getattr(constructor, s)
#         except:
#             print(f"Could not find constructor for colormap {name}, skipping this colormap.")
#             return None
#     cmap = constructor(name=name, **data["args"])
#     return cmap


# def get_custom_colormaps(cmap_path="colormaps.json"):
#     cmap_dict = read_json(Path(cmap_path))
#     cmaps = []
#     for cmap_name in cmap_dict:
#         data = cmap_dict[cmap_name]
#         cmap = build_custom_colormap(data, cmap_name)
#         if cmap is not None:
#             cmaps += [(cmap_name, cmap)]
#     return cmaps


# custom_cmaps = get_custom_colormaps("./utils/colormaps.json")
# for name, cmap in custom_cmaps:
#     cm.register_cmap(name=name, cmap=cmap)


# # Preview custom color maps by running this script on its own. Requires some changes to the imports to work,
# # but I'm leaving this in in case it's needed again later.
# if __name__ == "__main__":
#     def plot_examples(cmaps):
#         """
#         Helper function to plot data with associated colormap.
#         Code adapted from https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
#         """
#         data = np.random.randn(30, 30)
#         n = len(cmaps)
#         fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3), constrained_layout=True, squeeze=False)
#         for [ax, (name, cmap)] in zip(axs.flat, cmaps):
#             psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
#             fig.colorbar(psm, ax=ax)
#             ax.set_title(name)
#         plt.show()
#     plot_examples(custom_cmaps)