# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(800, 600)
        vtn_principal.setSizeIncrement(QSize(2, 2))
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vtn_nombre = QLineEdit(self.centralwidget)
        self.vtn_nombre.setObjectName(u"vtn_nombre")
        self.vtn_nombre.setGeometry(QRect(380, 120, 191, 41))
        self.vtn_apellido = QLineEdit(self.centralwidget)
        self.vtn_apellido.setObjectName(u"vtn_apellido")
        self.vtn_apellido.setGeometry(QRect(380, 180, 191, 41))
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(250, 120, 111, 41))
        self.lbl_nombre.setSizeIncrement(QSize(2, 2))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_nombre.setFont(font)
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(250, 180, 101, 41))
        self.lbl_apellido.setFont(font)
        self.vtn_guardar = QPushButton(self.centralwidget)
        self.vtn_guardar.setObjectName(u"vtn_guardar")
        self.vtn_guardar.setGeometry(QRect(340, 340, 151, 61))
        font1 = QFont()
        font1.setFamilies([u"MS Reference Sans Serif"])
        font1.setPointSize(14)
        self.vtn_guardar.setFont(font1)
        vtn_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        vtn_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Ventana Principal", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"NOMBRE", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"APELLIDO", None))
        self.vtn_guardar.setText(QCoreApplication.translate("vtn_principal", u"GUARDAR", None))
    # retranslateUi

