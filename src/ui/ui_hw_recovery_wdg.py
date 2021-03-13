# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_hw_recovery_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgRecoverHw(object):
    def setupUi(self, WdgRecoverHw):
        WdgRecoverHw.setObjectName("WdgRecoverHw")
        WdgRecoverHw.resize(587, 352)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WdgRecoverHw)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages = QtWidgets.QStackedWidget(WdgRecoverHw)
        self.pages.setObjectName("pages")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.page0)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gbSeedSource = QtWidgets.QGroupBox(self.page0)
        self.gbSeedSource.setTitle("")
        self.gbSeedSource.setFlat(False)
        self.gbSeedSource.setObjectName("gbSeedSource")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gbSeedSource)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rbSeedSourceHwScreen = QtWidgets.QRadioButton(self.gbSeedSource)
        self.rbSeedSourceHwScreen.setChecked(False)
        self.rbSeedSourceHwScreen.setObjectName("rbSeedSourceHwScreen")
        self.verticalLayout_5.addWidget(self.rbSeedSourceHwScreen)
        self.rbSeedSourceAppWords = QtWidgets.QRadioButton(self.gbSeedSource)
        self.rbSeedSourceAppWords.setChecked(False)
        self.rbSeedSourceAppWords.setObjectName("rbSeedSourceAppWords")
        self.verticalLayout_5.addWidget(self.rbSeedSourceAppWords)
        self.rbSeedSourceAppEntropy = QtWidgets.QRadioButton(self.gbSeedSource)
        self.rbSeedSourceAppEntropy.setObjectName("rbSeedSourceAppEntropy")
        self.verticalLayout_5.addWidget(self.rbSeedSourceAppEntropy)
        self.verticalLayout.addWidget(self.gbSeedSource)
        self.lblActionTypeMessage = QtWidgets.QLabel(self.page0)
        self.lblActionTypeMessage.setWordWrap(True)
        self.lblActionTypeMessage.setObjectName("lblActionTypeMessage")
        self.verticalLayout.addWidget(self.lblActionTypeMessage)
        spacerItem = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pages.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gbNumberOfMnemonicWords = QtWidgets.QGroupBox(self.page1)
        self.gbNumberOfMnemonicWords.setTitle("")
        self.gbNumberOfMnemonicWords.setObjectName("gbNumberOfMnemonicWords")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.gbNumberOfMnemonicWords)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rbWordsCount24 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount24.setChecked(True)
        self.rbWordsCount24.setObjectName("rbWordsCount24")
        self.verticalLayout_8.addWidget(self.rbWordsCount24)
        self.rbWordsCount18 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount18.setObjectName("rbWordsCount18")
        self.verticalLayout_8.addWidget(self.rbWordsCount18)
        self.rbWordsCount12 = QtWidgets.QRadioButton(self.gbNumberOfMnemonicWords)
        self.rbWordsCount12.setObjectName("rbWordsCount12")
        self.verticalLayout_8.addWidget(self.rbWordsCount12)
        self.verticalLayout_2.addWidget(self.gbNumberOfMnemonicWords)
        spacerItem1 = QtWidgets.QSpacerItem(20, 310, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pages.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblStep1HexEntropy = QtWidgets.QLabel(self.page2)
        self.lblStep1HexEntropy.setObjectName("lblStep1HexEntropy")
        self.verticalLayout_6.addWidget(self.lblStep1HexEntropy)
        self.edtHexEntropy = QtWidgets.QLineEdit(self.page2)
        self.edtHexEntropy.setObjectName("edtHexEntropy")
        self.verticalLayout_6.addWidget(self.edtHexEntropy)
        spacerItem2 = QtWidgets.QSpacerItem(20, 365, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.pages.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblStepWordListTitle = QtWidgets.QLabel(self.page3)
        self.lblStepWordListTitle.setWordWrap(True)
        self.lblStepWordListTitle.setOpenExternalLinks(True)
        self.lblStepWordListTitle.setObjectName("lblStepWordListTitle")
        self.verticalLayout_7.addWidget(self.lblStepWordListTitle)
        self.pages.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblStep1HexEntropy_2 = QtWidgets.QLabel(self.page4)
        self.lblStep1HexEntropy_2.setObjectName("lblStep1HexEntropy_2")
        self.verticalLayout_3.addWidget(self.lblStep1HexEntropy_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblPinMessage = QtWidgets.QLabel(self.page4)
        self.lblPinMessage.setWordWrap(False)
        self.lblPinMessage.setObjectName("lblPinMessage")
        self.horizontalLayout_3.addWidget(self.lblPinMessage)
        self.edtHwOptionsPIN = QtWidgets.QLineEdit(self.page4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtHwOptionsPIN.sizePolicy().hasHeightForWidth())
        self.edtHwOptionsPIN.setSizePolicy(sizePolicy)
        self.edtHwOptionsPIN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edtHwOptionsPIN.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtHwOptionsPIN.setObjectName("edtHwOptionsPIN")
        self.horizontalLayout_3.addWidget(self.edtHwOptionsPIN)
        self.btnShowPIN = QtWidgets.QToolButton(self.page4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShowPIN.sizePolicy().hasHeightForWidth())
        self.btnShowPIN.setSizePolicy(sizePolicy)
        self.btnShowPIN.setMinimumSize(QtCore.QSize(21, 21))
        self.btnShowPIN.setMaximumSize(QtCore.QSize(21, 21))
        self.btnShowPIN.setText("")
        self.btnShowPIN.setObjectName("btnShowPIN")
        self.horizontalLayout_3.addWidget(self.btnShowPIN)
        self.edtSecondaryPIN = QtWidgets.QLineEdit(self.page4)
        self.edtSecondaryPIN.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtSecondaryPIN.setObjectName("edtSecondaryPIN")
        self.horizontalLayout_3.addWidget(self.edtSecondaryPIN)
        self.btnShowSecondaryPIN = QtWidgets.QToolButton(self.page4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShowSecondaryPIN.sizePolicy().hasHeightForWidth())
        self.btnShowSecondaryPIN.setSizePolicy(sizePolicy)
        self.btnShowSecondaryPIN.setMinimumSize(QtCore.QSize(21, 21))
        self.btnShowSecondaryPIN.setMaximumSize(QtCore.QSize(21, 21))
        self.btnShowSecondaryPIN.setText("")
        self.btnShowSecondaryPIN.setObjectName("btnShowSecondaryPIN")
        self.horizontalLayout_3.addWidget(self.btnShowSecondaryPIN)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.chbUsePassphrase = QtWidgets.QCheckBox(self.page4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chbUsePassphrase.sizePolicy().hasHeightForWidth())
        self.chbUsePassphrase.setSizePolicy(sizePolicy)
        self.chbUsePassphrase.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chbUsePassphrase.setText("Use passphrase")
        self.chbUsePassphrase.setObjectName("chbUsePassphrase")
        self.gridLayout_2.addWidget(self.chbUsePassphrase, 3, 0, 1, 1)
        self.chbUsePIN = QtWidgets.QCheckBox(self.page4)
        self.chbUsePIN.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chbUsePIN.setChecked(True)
        self.chbUsePIN.setObjectName("chbUsePIN")
        self.gridLayout_2.addWidget(self.chbUsePIN, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtDeviceLabel = QtWidgets.QLineEdit(self.page4)
        self.edtDeviceLabel.setPlaceholderText("")
        self.edtDeviceLabel.setObjectName("edtDeviceLabel")
        self.horizontalLayout.addWidget(self.edtDeviceLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.lblDeviceLabel = QtWidgets.QLabel(self.page4)
        self.lblDeviceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDeviceLabel.setObjectName("lblDeviceLabel")
        self.gridLayout_2.addWidget(self.lblDeviceLabel, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPassphraseMessage = QtWidgets.QLabel(self.page4)
        self.lblPassphraseMessage.setWordWrap(False)
        self.lblPassphraseMessage.setObjectName("lblPassphraseMessage")
        self.horizontalLayout_4.addWidget(self.lblPassphraseMessage)
        self.edtPassphrase = QtWidgets.QLineEdit(self.page4)
        self.edtPassphrase.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPassphrase.setObjectName("edtPassphrase")
        self.horizontalLayout_4.addWidget(self.edtPassphrase)
        self.btnShowPassphrase = QtWidgets.QToolButton(self.page4)
        self.btnShowPassphrase.setMinimumSize(QtCore.QSize(21, 21))
        self.btnShowPassphrase.setMaximumSize(QtCore.QSize(21, 21))
        self.btnShowPassphrase.setText("")
        self.btnShowPassphrase.setObjectName("btnShowPassphrase")
        self.horizontalLayout_4.addWidget(self.btnShowPassphrase)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.lblDeviceWordsInputType = QtWidgets.QLabel(self.page4)
        self.lblDeviceWordsInputType.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDeviceWordsInputType.setObjectName("lblDeviceWordsInputType")
        self.gridLayout_2.addWidget(self.lblDeviceWordsInputType, 0, 0, 1, 1)
        self.gbDeviceWordsInputType = QtWidgets.QGroupBox(self.page4)
        self.gbDeviceWordsInputType.setObjectName("gbDeviceWordsInputType")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbDeviceWordsInputType)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbScrambledWords = QtWidgets.QRadioButton(self.gbDeviceWordsInputType)
        self.rbScrambledWords.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rbScrambledWords.setChecked(True)
        self.rbScrambledWords.setObjectName("rbScrambledWords")
        self.horizontalLayout_2.addWidget(self.rbScrambledWords)
        self.rbWordsMatrix = QtWidgets.QRadioButton(self.gbDeviceWordsInputType)
        self.rbWordsMatrix.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rbWordsMatrix.setChecked(False)
        self.rbWordsMatrix.setObjectName("rbWordsMatrix")
        self.horizontalLayout_2.addWidget(self.rbWordsMatrix)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_2.addWidget(self.gbDeviceWordsInputType, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.lblOptionsEntropy = QtWidgets.QLabel(self.page4)
        self.lblOptionsEntropy.setStyleSheet("font-size:11px")
        self.lblOptionsEntropy.setWordWrap(True)
        self.lblOptionsEntropy.setOpenExternalLinks(True)
        self.lblOptionsEntropy.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblOptionsEntropy.setObjectName("lblOptionsEntropy")
        self.verticalLayout_3.addWidget(self.lblOptionsEntropy)
        spacerItem5 = QtWidgets.QSpacerItem(20, 293, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.btnPreviewAddresses = QtWidgets.QPushButton(self.page4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviewAddresses.sizePolicy().hasHeightForWidth())
        self.btnPreviewAddresses.setSizePolicy(sizePolicy)
        self.btnPreviewAddresses.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPreviewAddresses.setAutoDefault(False)
        self.btnPreviewAddresses.setObjectName("btnPreviewAddresses")
        self.verticalLayout_3.addWidget(self.btnPreviewAddresses)
        self.pages.addWidget(self.page4)
        self.verticalLayout_4.addWidget(self.pages)

        self.retranslateUi(WdgRecoverHw)
        self.pages.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(WdgRecoverHw)

    def retranslateUi(self, WdgRecoverHw):
        _translate = QtCore.QCoreApplication.translate
        WdgRecoverHw.setWindowTitle(_translate("WdgRecoverHw", "Form"))
        self.label_2.setText(_translate("WdgRecoverHw", "<b>Source of the recovery seed</b>"))
        self.rbSeedSourceHwScreen.setText(_translate("WdgRecoverHw", "Recover from seed words using hardware wallet screen (secure)"))
        self.rbSeedSourceAppWords.setText(_translate("WdgRecoverHw", "Recover from seed words using in-app editor (convenient but insecure)"))
        self.rbSeedSourceAppEntropy.setText(_translate("WdgRecoverHw", "Recover from hexadecimal entropy (insecure)"))
        self.lblActionTypeMessage.setText(_translate("WdgRecoverHw", "..."))
        self.label.setText(_translate("WdgRecoverHw", "<b>The number of words of the recovery seed</b>"))
        self.rbWordsCount24.setText(_translate("WdgRecoverHw", "24"))
        self.rbWordsCount18.setText(_translate("WdgRecoverHw", "18"))
        self.rbWordsCount12.setText(_translate("WdgRecoverHw", "12"))
        self.lblStep1HexEntropy.setText(_translate("WdgRecoverHw", "<b>Enter the hexadecimal entropy of the recovery seed</b>"))
        self.edtHexEntropy.setPlaceholderText(_translate("WdgRecoverHw", "32/24/16-byte hexadecimal string"))
        self.lblStepWordListTitle.setText(_translate("WdgRecoverHw", "<b>Enter the words of your recovery seed</b>"))
        self.lblStep1HexEntropy_2.setText(_translate("WdgRecoverHw", "<b>Tune hardware wallet options as needed</b>"))
        self.lblPinMessage.setText(_translate("WdgRecoverHw", " "))
        self.edtHwOptionsPIN.setPlaceholderText(_translate("WdgRecoverHw", "PIN"))
        self.btnShowPIN.setToolTip(_translate("WdgRecoverHw", "Show PIN"))
        self.edtSecondaryPIN.setToolTip(_translate("WdgRecoverHw", "<html><head/><body><p>This PIN will be used to activate passphrase saved in your Ledger Nano S.</p></body></html>"))
        self.edtSecondaryPIN.setPlaceholderText(_translate("WdgRecoverHw", "Secondary PIN"))
        self.btnShowSecondaryPIN.setToolTip(_translate("WdgRecoverHw", "Show secondary PIN"))
        self.chbUsePassphrase.setWhatsThis(_translate("WdgRecoverHw", "<html><head/><body><p>Check the link attached &lt;a href=&quot;dash.org&quot;&gt;dash.org&lt;/a&gt;</p></body></html>"))
        self.chbUsePIN.setText(_translate("WdgRecoverHw", "Use PIN"))
        self.lblDeviceLabel.setText(_translate("WdgRecoverHw", "Device label"))
        self.lblPassphraseMessage.setText(_translate("WdgRecoverHw", " "))
        self.edtPassphrase.setToolTip(_translate("WdgRecoverHw", "<html><head/><body><p>This passphrase (if used) will be saved in your Ledger Nano S device and will be secured with the secondary PIN .</p></body></html>"))
        self.edtPassphrase.setPlaceholderText(_translate("WdgRecoverHw", "Passphrase"))
        self.btnShowPassphrase.setToolTip(_translate("WdgRecoverHw", "Show passphrase"))
        self.lblDeviceWordsInputType.setText(_translate("WdgRecoverHw", "Tnput type on device"))
        self.rbScrambledWords.setText(_translate("WdgRecoverHw", "Scrambled words"))
        self.rbWordsMatrix.setText(_translate("WdgRecoverHw", "Word matrix"))
        self.lblOptionsEntropy.setText(_translate("WdgRecoverHw", "Entropy:"))
        self.btnPreviewAddresses.setText(_translate("WdgRecoverHw", "Show preview"))
