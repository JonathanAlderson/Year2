#-------------------------------------------------
#
# Project created by QtCreator 2019-03-23T20:00:23
#
#-------------------------------------------------

QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets printsupport

TARGET = 16Cycles
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    addstaff.cpp \
    simplecrypt.cpp \
    adminhome.cpp \
    updatestaff.cpp \
    removestaff.cpp \
    resetpassword.cpp \
    profits.cpp \
    qcustomplot.cpp \
    hires.cpp

HEADERS  += mainwindow.h \
    addstaff.h \
    simplecrypt.h \
    adminhome.h \
    updatestaff.h \
    removestaff.h \
    resetpassword.h \
    profits.h \
    qcustomplot.h \
    hires.h

FORMS    += mainwindow.ui \
    addstaff.ui \
    adminhome.ui \
    updatestaff.ui \
    removestaff.ui \
    resetpassword.ui \
    profits.ui \
    hires.ui
    
RESOURCES += \
    resources.qrc
