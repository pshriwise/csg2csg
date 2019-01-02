#/usr/env/python3

from Input import InputDeck
from SerpentSurfaceCard import SerpentSurfaceCard, write_serpent_surface
from SerpentCellCard import SerpentCellCard, write_serpent_cell
from SerpentMaterialCard import SerpentMaterialCard, write_serpent_material

class SerpentInput(InputDeck):
    """ SerpentInput class - does the actual processing
    """

    # constructor
    def __init__(self,filename = ""):
        InputDeck.__init__(self,filename)

#    def from_input(self,InputDeckClass):
#        InputDeck.filename = InputDeckClass.filename
#        InputDeck.title = InputDeckClass.title
#        InputDeck.cell_list = InputDeckClass.cell_list
#        InputDeck.surfcace_list = InputDeckClass.surface_list
#        return

    # Write the Serpent Cell definitions
    def __write_serpent_cells(self, filestream):
        filestream.write("% --- cell definitions --- %\n")
        for cell in self.cell_list:
            write_serpent_cell(filestream,cell)
        return

    # write the serpent surface definitions
    def __write_serpent_surfaces(self, filestream):
        filestream.write("% --- surface definitions --- %\n")
        for surface in self.surface_list:
            write_serpent_surface(filestream,surface)
        return

    # write the material compositions
    def __write_serpent_materials(self, filestream):
        filestream.write("% --- material definitions --- %\n")
        for material in self.material_list:
            write_serpent_material(filestream, self.material_list[material])
        return

    # main write serpent method, depending upon where the geometry
    # came from
    def write_serpent(self, filename, flat = True):
        f = open(filename,'w')
        self.__write_serpent_surfaces(f)
        self.__write_serpent_cells(f)
        self.__write_serpent_materials(f)
        f.close()

    def process(self):

        self.__set_title()

        # clear out comment lines
        idx = 0
        while True:
            if idx == len(self.file_lines):
                break
            if self.file_lines[idx][0] == "%":
                del self.file_lines[idx]
            if "%" in self.file_lines[idx]:
                self.file_lines[idx] = self.file_lines[idx].split("%")[-1]
            idx += 1

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            logging.debug("%s", "Input Echo")
            for idx, line in enumerate(self.file_lines):
                logging.debug("%i %s", idx, line)

        # get the cell cards
        idx = self.__get_cell_cards()

    def __set_title(self):
        # set the title card
        for i, line in enumerate(self.file_lines):
            title_key = "set title"
            if title_key in line:
                self.title = line.split(title_key)[-1]
                del self.file_lines[i]
                break

    def __get_cell_cards(self):
        # line by line insert into list of cell descriptions
        for line in self.file_lines:
            if "cell" == line[0:4]:
                cellcard = SerpentCellCard(line)
                self.cell_list.append(cellcard)

    def __get_surface_cards(self):
        # line by line insert into list of surface descriptions
        for line in self.file_lines:
            if "surf" == line[0:4]:
                surfcard = SerpentSurfaceCard(line)
                self.surface_list.append(surfcard)

    def __get_transform_cards(self):
        for line in self.file_lines:
            if "trans" == line[0:4]:
                transcard = Serpent
