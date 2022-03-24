import matplotlib.colors
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


class Overwrite(object):
    def __init__(self):
        self.make_c4_color_map()
        return        

    def make_c4_color_map(self):
        color_map = matplotlib.colors.get_named_colors_mapping()

        # defining single colors
        color_map["c4grey"] = "#414042"
        color_map["c4red"] = "#f75151"
        color_map["c4blue"] = "#043D5D"
        color_map["c4olive"] = "#686B30"
        color_map["c4teal"] = "#004342"
        color_map["c4purple"] = "#122945"
        color_map["c4yellow"] = "#D4AD6D"
        color_map["c4green"] = "#05A07E"
        color_map["c4lightblue"] = "#A0B9D0"
        color_map["c4tan"] = "#F8E5C8"
        color_map["c4greengrey"] = "#B3B299"
        return

    def add_century_gothic():
        # Add every font at the specified location
        font_dir = ['./century-gothic']
        for font in font_manager.findSystemFonts(font_dir):
            font_manager.fontManager.addfont(font)

if __name__ == "__main__":
    Overwrite()

