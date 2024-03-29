import copy
from PyQt4 import QtCore
from Controller.controller_events import StoreControllerEvent, MapControllerEvent
from Geometry.point import Point
from Model.game_result import GameResult

__author__ = 'umqra'


class MainController:
    def __init__(self, state):
        self.state = state
        self.selected_item = None
        self.store_info = None

    def select(self, factory, store_info=None):
        if self.state.game_result != GameResult.Running:
            return
        item = factory(self.state.map)
        self.selected_item = item
        self.store_info = store_info
        self.state.map.add_preview_item(item)

    def unselect(self):
        if self.selected_item is None:
            return
        self.state.map.remove_preview_item(self.selected_item)
        self.selected_item = None

    def handle_store_event(self, event):
        if self.selected_item is not None:
            self.unselect()
        if event.mouse_event.buttons() == QtCore.Qt.LeftButton:
            self.select(event.factory_for_items, event.store_info)

    def handle_map_event(self, event):
        if event.mouse_event.type() == QtCore.QEvent.MouseMove:
            if self.selected_item is not None:
                self.selected_item.move_to(Point(event.mouse_event.x(), event.mouse_event.y()))
        elif event.mouse_event.type() == QtCore.QEvent.MouseButtonPress:
            if event.mouse_event.buttons() == QtCore.Qt.RightButton:
                self.unselect()
            elif event.mouse_event.buttons() == QtCore.Qt.LeftButton and self.selected_item is not None:
                if self.state.try_buy_item(self.selected_item, self.store_info):
                    self.unselect()

    def handle_event(self, event):
        if isinstance(event, StoreControllerEvent):
            self.handle_store_event(event)
        elif isinstance(event, MapControllerEvent):
            self.handle_map_event(event)