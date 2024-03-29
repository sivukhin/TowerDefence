from PyQt4.QtGui import QWidget, QGridLayout

from Model.game_state import GameResult
from PyQtExtension.custom_button import CustomButton


__author__ = 'umqra'


class ControlPanelView(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.layout = QGridLayout()
        self.layout.setRowStretch(0, 1)

        self.pause_button = CustomButton("Pause")
        self.pause_button.clicked.connect(self.pause_button_clicked)
        self.layout.addWidget(self.pause_button, 1, 0)

        self.restart_button = CustomButton("Restart")
        self.restart_button.clicked.connect(self.restart_button_clicked)
        self.layout.addWidget(self.restart_button, 2, 0)

        self.next_level_button = CustomButton("Next level")
        self.next_level_button.clicked.connect(self.next_level_button_clicked)
        self.layout.addWidget(self.next_level_button, 3, 0)

        self.layout.setRowStretch(4, 1)

        self.setLayout(self.layout)

    def pause_button_clicked(self):
        if self.model.pause:
            self.model.resume()
            self.pause_button.setText("Pause")
        else:
            self.model.stop()
            self.pause_button.setText("Start")

    def restart_button_clicked(self):
        self.model.restart()

    def next_level_button_clicked(self):
        if self.model.game_result != GameResult.Win:
            return
        self.model.next_level()