/********************************************************************************
** Form generated from reading UI file 'hires.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_HIRES_H
#define UI_HIRES_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include <qcustomplot.h>

QT_BEGIN_NAMESPACE

class Ui_Hires
{
public:
    QGroupBox *groupBox;
    QPushButton *pushButton;
    QCustomPlot *plot;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_5;
    QLabel *startDateLabel;
    QLineEdit *startDateLineEdit;
    QLabel *EndDateLabel;
    QLineEdit *endDateLineEdit;
    QPushButton *graphsRefreshButton;
    QGroupBox *groupBox_2;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *allShopsLabel;
    QLabel *shop1Label;
    QHBoxLayout *horizontalLayout_2;
    QLabel *shop2Label;
    QLabel *shop3Label;

    void setupUi(QDialog *Hires)
    {
        if (Hires->objectName().isEmpty())
            Hires->setObjectName(QStringLiteral("Hires"));
        Hires->resize(824, 586);
        groupBox = new QGroupBox(Hires);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 10, 801, 561));
        pushButton = new QPushButton(groupBox);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(10, 510, 92, 36));
        plot = new QCustomPlot(groupBox);
        plot->setObjectName(QStringLiteral("plot"));
        plot->setGeometry(QRect(10, 30, 771, 411));
        layoutWidget = new QWidget(groupBox);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 460, 518, 38));
        horizontalLayout_5 = new QHBoxLayout(layoutWidget);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        startDateLabel = new QLabel(layoutWidget);
        startDateLabel->setObjectName(QStringLiteral("startDateLabel"));

        horizontalLayout_5->addWidget(startDateLabel);

        startDateLineEdit = new QLineEdit(layoutWidget);
        startDateLineEdit->setObjectName(QStringLiteral("startDateLineEdit"));

        horizontalLayout_5->addWidget(startDateLineEdit);

        EndDateLabel = new QLabel(layoutWidget);
        EndDateLabel->setObjectName(QStringLiteral("EndDateLabel"));

        horizontalLayout_5->addWidget(EndDateLabel);

        endDateLineEdit = new QLineEdit(layoutWidget);
        endDateLineEdit->setObjectName(QStringLiteral("endDateLineEdit"));

        horizontalLayout_5->addWidget(endDateLineEdit);

        graphsRefreshButton = new QPushButton(layoutWidget);
        graphsRefreshButton->setObjectName(QStringLiteral("graphsRefreshButton"));

        horizontalLayout_5->addWidget(graphsRefreshButton);

        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(540, 450, 221, 91));
        layoutWidget1 = new QWidget(groupBox_2);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(10, 20, 201, 61));
        verticalLayout = new QVBoxLayout(layoutWidget1);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        allShopsLabel = new QLabel(layoutWidget1);
        allShopsLabel->setObjectName(QStringLiteral("allShopsLabel"));

        horizontalLayout->addWidget(allShopsLabel);

        shop1Label = new QLabel(layoutWidget1);
        shop1Label->setObjectName(QStringLiteral("shop1Label"));

        horizontalLayout->addWidget(shop1Label);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        shop2Label = new QLabel(layoutWidget1);
        shop2Label->setObjectName(QStringLiteral("shop2Label"));

        horizontalLayout_2->addWidget(shop2Label);

        shop3Label = new QLabel(layoutWidget1);
        shop3Label->setObjectName(QStringLiteral("shop3Label"));

        horizontalLayout_2->addWidget(shop3Label);


        verticalLayout->addLayout(horizontalLayout_2);


        retranslateUi(Hires);

        QMetaObject::connectSlotsByName(Hires);
    } // setupUi

    void retranslateUi(QDialog *Hires)
    {
        Hires->setWindowTitle(QApplication::translate("Hires", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("Hires", "Hires", Q_NULLPTR));
        pushButton->setText(QApplication::translate("Hires", "Go Back", Q_NULLPTR));
        startDateLabel->setText(QApplication::translate("Hires", "Start Date", Q_NULLPTR));
        startDateLineEdit->setText(QApplication::translate("Hires", "YYYY-MM-DD", Q_NULLPTR));
        EndDateLabel->setText(QApplication::translate("Hires", "End Date", Q_NULLPTR));
        endDateLineEdit->setText(QApplication::translate("Hires", "YYYY-MM-DD", Q_NULLPTR));
        graphsRefreshButton->setText(QApplication::translate("Hires", "Refresh", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("Hires", "Hires Data", Q_NULLPTR));
        allShopsLabel->setText(QApplication::translate("Hires", "All Shops : ", Q_NULLPTR));
        shop1Label->setText(QApplication::translate("Hires", "Shop 1 : ", Q_NULLPTR));
        shop2Label->setText(QApplication::translate("Hires", "Shop 2 : ", Q_NULLPTR));
        shop3Label->setText(QApplication::translate("Hires", "Shop 3 : ", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Hires: public Ui_Hires {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HIRES_H
