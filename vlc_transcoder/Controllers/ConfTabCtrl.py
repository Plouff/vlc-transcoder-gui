#! python3
# -*-coding: utf-8 -*-

"""
@file ConfTabCtrl.py
The Controller for the output configuration tab
"""

# Import PyQt modules
from PyQt5 import QtCore

# Import custom modules
from NzPyQtToolBox.NzToolTipList import \
    TooltipedDataListModel as TooltipListModel

# Import standard modules


class ConfTabCtrl(QtCore.QObject):
    """
    The controller for the configuration tab widgets
    """
    def __init__(self, model, view):
        """
        The class constructor

        @param model the model of the MVC GUI
        @param view the view of the MVC GUI
        """
        # Save pointers to model and view
        self.model = model
        self.view = view

    def connectModelAndView(self):
        """
        Create models and connect them to the different views.
        """
        # Encapsulator
        self.encapsulatorModel = TooltipListModel(
            self.model.encapsulatorsODic)
        self.view.encapsCombo.setModel(self.encapsulatorModel)
        self.view.encapsCombo.setCurrentIndex(
            self.view.encapsCombo.findText("ts"))

        # Video codec
        self.vCodecModel = TooltipListModel(
            self.model.vCodecODic)
        self.view.vCodecCombo.setModel(self.vCodecModel)
        self.view.vCodecCombo.setCurrentIndex(
            self.view.vCodecCombo.findText("h264"))

        # Audio codec
        self.aCodecModel = TooltipListModel(
            self.model.aCodecODic)
        self.view.aCodecCombo.setModel(self.aCodecModel)

        # Audio bitrate
        self.aBitRateModel = QtCore.QStringListModel(self.model.aBitRateList)
        self.view.aBitRateCombo.setModel(self.aBitRateModel)
        self.view.aBitRateCombo.setCurrentIndex(
            self.view.aBitRateCombo.findText("128kB/s"))

        # Sample rate
        # TODO: add sample rate
#         self.aSampleRateModel = QtCore.QStringListModel(
#             self.model.aSampleRateList)
#         self.view.aSampleRateCombo.setModel(self.aSampleRateModel)

        # Standard Resolution
        self.stdResolModel = TooltipListModel(
            self.model.stdResolutionOdic)
        self.view.byStdResolCombo.setModel(self.stdResolModel)

        # Resize by height
        self.heightModel = QtCore.QStringListModel(self.model.vHeightList)
        self.view.byHeightCombo.setModel(self.heightModel)

        # Resize by width
        self.widthModel = QtCore.QStringListModel(self.model.vWidthList)
        self.view.byWidthCombo.setModel(self.widthModel)
