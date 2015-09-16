from Infrastructure.get_resources import get_default_image, load_image

__author__ = 'umqra'

from Model.towers import EnergyTower, LightTower, JustTower, Fortress
from PyQt4.QtGui import QWidget, QPainter, QPixmap, QImage, QColor, QGridLayout
from PyQt4.QtCore import Qt


def get_tower_view(tower):
    if isinstance(tower, EnergyTower):
        return EnergyTowerView(tower)
    elif isinstance(tower, LightTower):
        return LightTowerView(tower)
    elif isinstance(tower, JustTower):
        return JustTowerView(tower)
    elif isinstance(tower, Fortress):
        return FortressView(tower)
    return TowerView(tower)


class TowerView(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def paintEvent(self, QPaintEvent):
        pass


def draw_loader(x, y, w, h, percentage, qp, color):
    qp.fillRect(x, y, int(w * percentage), h, color)
    qp.drawRect(x, y, w, h)


class EnergyTowerView(TowerView):
    image = load_image("energy_tower.png", 50)

    def __init__(self, model):
        super().__init__(model)
        self.pixmap = QPixmap(EnergyTowerView.image)
        self.height_pixmap = self.pixmap.height()

    def paintEvent(self, QPaintEvent):
        if not self.model.is_alive:
            self.close()
        qp = QPainter()
        qp.begin(self)
        bbox = self.model.shape.get_bounding_box()
        x_coord = bbox[0].x
        y_coord = bbox[0].y
        loader_width = 40  # TODO: replace to constant!!
        loader_height = 5
        shift = (50 - loader_width) / 2
        qp.drawPixmap(x_coord, y_coord, self.pixmap)
        spacing = 2
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing,
                    loader_width, loader_height,
                    self.model.health / 100, qp,
                    QColor.fromRgb(87, 166, 57))
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing + loader_height + spacing,
                    loader_width, loader_height,
                    1 - self.model.time_to_attack / self.model.recharge_time, qp,
                    QColor.fromRgb(116, 66, 200))

    def mousePressEvent(self, QMouseEvent):
        print("Press {}".format(self))


class LightTowerView(TowerView):
    image = load_image("light_tower.png", 50)

    def __init__(self, model):
        super().__init__(model)
        self.pixmap = QPixmap(LightTowerView.image)
        self.height_pixmap = self.pixmap.height()

    def paintEvent(self, QPaintEvent):
        if not self.model.is_alive:
            self.close()
        qp = QPainter()
        qp.begin(self)
        bbox = self.model.shape.get_bounding_box()

        x_coord = bbox[0].x
        y_coord = bbox[0].y
        loader_width = 40  # TODO: replace to constant!!
        loader_height = 5
        shift = (50 - loader_width) / 2
        qp.drawPixmap(x_coord, y_coord, self.pixmap)
        spacing = 2
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing,
                    loader_width, loader_height,
                    self.model.health / 100, qp,
                    QColor.fromRgb(87, 166, 57))
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing + loader_height + spacing,
                    loader_width, loader_height,
                    1 - self.model.time_to_attack / self.model.recharge_time, qp,
                    QColor.fromRgb(116, 66, 200))

    def mousePressEvent(self, QMouseEvent):
        print("Press {}".format(self))


class JustTowerView(TowerView):
    image = load_image("just_tower.png", 50)

    def __init__(self, model):
        super().__init__(model)
        self.pixmap = QPixmap(JustTowerView.image)
        self.height_pixmap = self.pixmap.height()

    def paintEvent(self, QPaintEvent):
        if not self.model.is_alive:
            self.close()
        qp = QPainter()
        qp.begin(self)
        bbox = self.model.shape.get_bounding_box()

        x_coord = bbox[0].x
        y_coord = bbox[0].y
        loader_width = 40  # TODO: replace to constant!!
        loader_height = 5
        shift = (50 - loader_width) / 2
        qp.drawPixmap(x_coord, y_coord, self.pixmap)
        spacing = 2
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing,
                    loader_width, loader_height,
                    self.model.health / 100, qp,
                    QColor.fromRgb(87, 166, 57))

    def mousePressEvent(self, QMouseEvent):
        print("Press {}".format(self))


class FortressView(TowerView):
    image = load_image("fortress.png", 50)

    def __init__(self, model):
        super().__init__(model)
        self.pixmap = QPixmap(FortressView.image)
        self.height_pixmap = self.pixmap.height()

    def paintEvent(self, QPaintEvent):
        if not self.model.is_alive:
            self.close()
        qp = QPainter()
        qp.begin(self)
        bbox = self.model.shape.get_bounding_box()

        x_coord = bbox[0].x
        y_coord = bbox[0].y
        loader_width = 40  # TODO: replace to constant!!
        loader_height = 5
        shift = (50 - loader_width) / 2
        qp.drawPixmap(x_coord, y_coord, self.pixmap)
        spacing = 2
        draw_loader(x_coord + shift, y_coord + self.pixmap.height() + spacing,
                    loader_width, loader_height,
                    self.model.health / 100, qp,
                    QColor.fromRgb(87, 166, 57))

    def mousePressEvent(self, QMouseEvent):
        print("Press {}".format(self))