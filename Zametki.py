# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(402, 300)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 3, 401, 301))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Save = QPushButton(self.layoutWidget)
        self.Save.setObjectName(u"Save")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy)
        self.Save.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 10pt \"Segoe Script\";")

        self.horizontalLayout.addWidget(self.Save)

        self.OpenF = QPushButton(self.layoutWidget)
        self.OpenF.setObjectName(u"OpenF")
        self.OpenF.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 10pt \"Segoe Script\";")

        self.horizontalLayout.addWidget(self.OpenF)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 10pt \"Segoe Script\";")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Text = QTextEdit(self.layoutWidget)
        self.Text.setObjectName(u"Text")
        self.Text.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"margin: 5px;\n"
"font-size: 12px")

        self.verticalLayout.addWidget(self.Text)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Save.setText(QCoreApplication.translate("Dialog", u"Save as...", None))
        self.OpenF.setText(QCoreApplication.translate("Dialog", u"Open with..", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Convert to .py", None))
    # retranslateUi

