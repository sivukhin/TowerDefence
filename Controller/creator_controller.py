from Controller.controller_events import MapCreatorControllerEvent, StoreControllerEvent, ChooseLandscapeEvent, \
    SelectItemControllerEvent, StartCreateNewWaveControllerEvent, GetGatesForWaveControllerEvent
from PyQt4 import QtCore
from Geometry.point import Point
from Model.map_cell import MapCell
from Model.towers import Tower
from Model.wave import Gate

__author__ = 'umqra'


class CreatorController:
    def __init__(self, state):
        self.state = state
        self.selected_item = None
        self.list_choosen = []
        self.new_wave_dialog = None

    def try_put_selected_item_on_map(self, x, y):
        if self.selected_item is None:
            return False
        y, x = self.state.map.get_cell_coordinates(x, y)
        if isinstance(self.selected_item, MapCell):
            self.state.map.set_cell_type(x, y, self.selected_item.get_view_repr() + "1")
        elif isinstance(self.selected_item, Tower):
            if self.state.map.add_tower(self.selected_item):
                self.selected_item = None
                return True
        elif isinstance(self.selected_item, Gate):
            if self.state.map.add_gate(self.selected_item):
                self.selected_item = None
                return True
        return False

    def try_select_item_on_map(self, x, y):
        if self.selected_item is not None:
            return False
        item = self.state.map.get_item_contained_position(x, y)
        if item is None:
            return False
        item.switch()
        if item.selected:
            self.list_choosen.append(item)
        else:
            self.list_choosen.remove(item)
        return True

    def select(self, factory, store_info=None):
        item = factory(self.state.map)
        self.selected_item = item
        self.store_info = store_info
        self.state.map.add_preview_item(item)

    def unselect(self):
        if self.selected_item is None:
            return
        if not isinstance(self.selected_item, MapCell):
            self.state.map.remove_preview_item(self.selected_item)
        self.selected_item = None


    def handle_map_event(self, event):
        if event.mouse_event.type() == QtCore.QEvent.MouseMove:
            if self.selected_item is not None and not isinstance(self.selected_item, MapCell):
                self.selected_item.move_to(Point(event.mouse_event.x(), event.mouse_event.y()))

        if event.mouse_event.type() == QtCore.QEvent.MouseButtonPress:
            if event.mouse_event.buttons() == QtCore.Qt.RightButton:
                self.unselect()
            elif event.mouse_event.buttons() == QtCore.Qt.LeftButton:
                if self.try_put_selected_item_on_map(event.mouse_event.x(), event.mouse_event.y()):
                    return
                self.try_select_item_on_map(event.mouse_event.x(), event.mouse_event.y())

    def handle_store_event(self, event):
        if self.selected_item is not None:
            self.unselect()
        if event.mouse_event.buttons() == QtCore.Qt.LeftButton:
            self.select(event.factory_for_items, event.store_info)

    def handle_choose_landscape_event(self, event):
        self.unselect()
        self.selected_item = event.cell
        print("select {}".format(event.cell))

    def handle_select_event(self, event):
        event.item.select()

    def handle_start_new_wave_event(self, event):
        self.new_wave_dialog = event.dialog

    def handle_get_gates_event(self, event):
        event.dialog.accept_gates(self.list_choosen)
        for item in self.list_choosen:
            item.unselect()
        self.list_choosen.clear()

    def handle_event(self, event):
        if isinstance(event, MapCreatorControllerEvent):
            self.handle_map_event(event)
        elif isinstance(event, ChooseLandscapeEvent):
            self.handle_choose_landscape_event(event)
        elif isinstance(event, StoreControllerEvent):
            self.handle_store_event(event)
        elif isinstance(event, SelectItemControllerEvent):
            self.handle_select_event(event)
        elif isinstance(event, StartCreateNewWaveControllerEvent):
            self.handle_start_new_wave_event(event)
        elif isinstance(event, GetGatesForWaveControllerEvent):
            self.handle_get_gates_event(event)