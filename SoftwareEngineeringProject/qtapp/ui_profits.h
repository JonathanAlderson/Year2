/********************************************************************************
** Form generated from reading UI file 'profits.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PROFITS_H
#define UI_PROFITS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>
#include <qcustomplot.h>

QT_BEGIN_NAMESPACE

class Ui_Profits
{
public:
    QGroupBox *groupBox;
    QGroupBox *filterTwoDatesGroupBox;
    QGroupBox *filterTwoDatesProfitsAllShopsGroupBox;
    QLabel *filterTwoDatesProfitsLabel;
    QGroupBox *filterTwoDatesShopsGroupBox;
    QLabel *filterTwoDatesProfitsShopsLabel;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_4;
    QLabel *filterTwoDatesShopsLabel;
    QComboBox *filterTwoDatesShopsComboBox;
    QPushButton *filterTwoDatesRefreshButton;
    QWidget *layoutWidget1;
    QHBoxLayout *horizontalLayout_2;
    QLabel *dateOneLabel;
    QLineEdit *dateOneLineEdit;
    QWidget *layoutWidget2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *dateTwoLabel;
    QLineEdit *dateTwoLineEdit;
    QGroupBox *groupBox_2;
    QLabel *filterAllTimeShopsProfitsLabel;
    QWidget *layoutWidget3;
    QHBoxLayout *horizontalLayout;
    QLabel *filterAllTimeShopsLabel;
    QComboBox *filterAllTimeShopsComboBox;
    QGroupBox *groupBox_3;
    QCustomPlot *plot;
    QWidget *layoutWidget4;
    QHBoxLayout *horizontalLayout_5;
    QLabel *startDateLabel;
    QLineEdit *startDateLineEdit;
    QLabel *EndDateLabel;
    QLineEdit *endDateLineEdit;
    QPushButton *graphsRefreshButton;
    QCheckBox *allShopsCheckBox;
    QCheckBox *shop2CheckBox;
    QCheckBox *shop1CheckBox;
    QCheckBox *shop3CheckBox;
    QPushButton *goBackButton;

    void setupUi(QDialog *Profits)
    {
        if (Profits->objectName().isEmpty())
            Profits->setObjectName(QStringLiteral("Profits"));
        Profits->resize(1079, 822);
        groupBox = new QGroupBox(Profits);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 20, 1051, 791));
        filterTwoDatesGroupBox = new QGroupBox(groupBox);
        filterTwoDatesGroupBox->setObjectName(QStringLiteral("filterTwoDatesGroupBox"));
        filterTwoDatesGroupBox->setGeometry(QRect(10, 130, 1021, 111));
        filterTwoDatesProfitsAllShopsGroupBox = new QGroupBox(filterTwoDatesGroupBox);
        filterTwoDatesProfitsAllShopsGroupBox->setObjectName(QStringLiteral("filterTwoDatesProfitsAllShopsGroupBox"));
        filterTwoDatesProfitsAllShopsGroupBox->setGeometry(QRect(230, 20, 171, 81));
        filterTwoDatesProfitsLabel = new QLabel(filterTwoDatesProfitsAllShopsGroupBox);
        filterTwoDatesProfitsLabel->setObjectName(QStringLiteral("filterTwoDatesProfitsLabel"));
        filterTwoDatesProfitsLabel->setGeometry(QRect(20, 40, 91, 20));
        filterTwoDatesProfitsLabel->setLayoutDirection(Qt::LeftToRight);
        filterTwoDatesShopsGroupBox = new QGroupBox(filterTwoDatesGroupBox);
        filterTwoDatesShopsGroupBox->setObjectName(QStringLiteral("filterTwoDatesShopsGroupBox"));
        filterTwoDatesShopsGroupBox->setGeometry(QRect(420, 20, 301, 81));
        filterTwoDatesProfitsShopsLabel = new QLabel(filterTwoDatesShopsGroupBox);
        filterTwoDatesProfitsShopsLabel->setObjectName(QStringLiteral("filterTwoDatesProfitsShopsLabel"));
        filterTwoDatesProfitsShopsLabel->setGeometry(QRect(230, 40, 61, 20));
        filterTwoDatesProfitsShopsLabel->setLayoutDirection(Qt::LeftToRight);
        layoutWidget = new QWidget(filterTwoDatesShopsGroupBox);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(21, 31, 199, 38));
        horizontalLayout_4 = new QHBoxLayout(layoutWidget);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        filterTwoDatesShopsLabel = new QLabel(layoutWidget);
        filterTwoDatesShopsLabel->setObjectName(QStringLiteral("filterTwoDatesShopsLabel"));

        horizontalLayout_4->addWidget(filterTwoDatesShopsLabel);

        filterTwoDatesShopsComboBox = new QComboBox(layoutWidget);
        filterTwoDatesShopsComboBox->setObjectName(QStringLiteral("filterTwoDatesShopsComboBox"));

        horizontalLayout_4->addWidget(filterTwoDatesShopsComboBox);

        filterTwoDatesRefreshButton = new QPushButton(filterTwoDatesGroupBox);
        filterTwoDatesRefreshButton->setObjectName(QStringLiteral("filterTwoDatesRefreshButton"));
        filterTwoDatesRefreshButton->setGeometry(QRect(730, 60, 88, 36));
        layoutWidget1 = new QWidget(filterTwoDatesGroupBox);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(10, 20, 208, 39));
        horizontalLayout_2 = new QHBoxLayout(layoutWidget1);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        dateOneLabel = new QLabel(layoutWidget1);
        dateOneLabel->setObjectName(QStringLiteral("dateOneLabel"));

        horizontalLayout_2->addWidget(dateOneLabel);

        dateOneLineEdit = new QLineEdit(layoutWidget1);
        dateOneLineEdit->setObjectName(QStringLiteral("dateOneLineEdit"));

        horizontalLayout_2->addWidget(dateOneLineEdit);

        layoutWidget2 = new QWidget(filterTwoDatesGroupBox);
        layoutWidget2->setObjectName(QStringLiteral("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(10, 60, 208, 39));
        horizontalLayout_3 = new QHBoxLayout(layoutWidget2);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        dateTwoLabel = new QLabel(layoutWidget2);
        dateTwoLabel->setObjectName(QStringLiteral("dateTwoLabel"));

        horizontalLayout_3->addWidget(dateTwoLabel);

        dateTwoLineEdit = new QLineEdit(layoutWidget2);
        dateTwoLineEdit->setObjectName(QStringLiteral("dateTwoLineEdit"));

        horizontalLayout_3->addWidget(dateTwoLineEdit);

        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(10, 30, 1021, 81));
        filterAllTimeShopsProfitsLabel = new QLabel(groupBox_2);
        filterAllTimeShopsProfitsLabel->setObjectName(QStringLiteral("filterAllTimeShopsProfitsLabel"));
        filterAllTimeShopsProfitsLabel->setGeometry(QRect(230, 40, 91, 20));
        filterAllTimeShopsProfitsLabel->setLayoutDirection(Qt::LeftToRight);
        layoutWidget3 = new QWidget(groupBox_2);
        layoutWidget3->setObjectName(QStringLiteral("layoutWidget3"));
        layoutWidget3->setGeometry(QRect(10, 30, 199, 38));
        horizontalLayout = new QHBoxLayout(layoutWidget3);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        filterAllTimeShopsLabel = new QLabel(layoutWidget3);
        filterAllTimeShopsLabel->setObjectName(QStringLiteral("filterAllTimeShopsLabel"));

        horizontalLayout->addWidget(filterAllTimeShopsLabel);

        filterAllTimeShopsComboBox = new QComboBox(layoutWidget3);
        filterAllTimeShopsComboBox->setObjectName(QStringLiteral("filterAllTimeShopsComboBox"));

        horizontalLayout->addWidget(filterAllTimeShopsComboBox);

        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setGeometry(QRect(10, 250, 1021, 491));
        plot = new QCustomPlot(groupBox_3);
        plot->setObjectName(QStringLiteral("plot"));
        plot->setGeometry(QRect(10, 30, 991, 391));
        layoutWidget4 = new QWidget(groupBox_3);
        layoutWidget4->setObjectName(QStringLiteral("layoutWidget4"));
        layoutWidget4->setGeometry(QRect(10, 439, 518, 38));
        horizontalLayout_5 = new QHBoxLayout(layoutWidget4);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        startDateLabel = new QLabel(layoutWidget4);
        startDateLabel->setObjectName(QStringLiteral("startDateLabel"));

        horizontalLayout_5->addWidget(startDateLabel);

        startDateLineEdit = new QLineEdit(layoutWidget4);
        startDateLineEdit->setObjectName(QStringLiteral("startDateLineEdit"));

        horizontalLayout_5->addWidget(startDateLineEdit);

        EndDateLabel = new QLabel(layoutWidget4);
        EndDateLabel->setObjectName(QStringLiteral("EndDateLabel"));

        horizontalLayout_5->addWidget(EndDateLabel);

        endDateLineEdit = new QLineEdit(layoutWidget4);
        endDateLineEdit->setObjectName(QStringLiteral("endDateLineEdit"));

        horizontalLayout_5->addWidget(endDateLineEdit);

        graphsRefreshButton = new QPushButton(layoutWidget4);
        graphsRefreshButton->setObjectName(QStringLiteral("graphsRefreshButton"));

        horizontalLayout_5->addWidget(graphsRefreshButton);

        allShopsCheckBox = new QCheckBox(groupBox_3);
        allShopsCheckBox->setObjectName(QStringLiteral("allShopsCheckBox"));
        allShopsCheckBox->setGeometry(QRect(551, 430, 88, 26));
        shop2CheckBox = new QCheckBox(groupBox_3);
        shop2CheckBox->setObjectName(QStringLiteral("shop2CheckBox"));
        shop2CheckBox->setGeometry(QRect(551, 460, 75, 26));
        shop1CheckBox = new QCheckBox(groupBox_3);
        shop1CheckBox->setObjectName(QStringLiteral("shop1CheckBox"));
        shop1CheckBox->setGeometry(QRect(650, 430, 75, 26));
        shop3CheckBox = new QCheckBox(groupBox_3);
        shop3CheckBox->setObjectName(QStringLiteral("shop3CheckBox"));
        shop3CheckBox->setGeometry(QRect(650, 460, 75, 26));
        goBackButton = new QPushButton(groupBox);
        goBackButton->setObjectName(QStringLiteral("goBackButton"));
        goBackButton->setGeometry(QRect(10, 750, 92, 36));

        retranslateUi(Profits);

        QMetaObject::connectSlotsByName(Profits);
    } // setupUi

    void retranslateUi(QDialog *Profits)
    {
        Profits->setWindowTitle(QApplication::translate("Profits", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("Profits", "Profits", Q_NULLPTR));
        filterTwoDatesGroupBox->setTitle(QApplication::translate("Profits", "Filter By Two Dates", Q_NULLPTR));
        filterTwoDatesProfitsAllShopsGroupBox->setTitle(QApplication::translate("Profits", "Total Profits All shops", Q_NULLPTR));
        filterTwoDatesProfitsLabel->setText(QApplication::translate("Profits", "\302\2430.00", Q_NULLPTR));
        filterTwoDatesShopsGroupBox->setTitle(QApplication::translate("Profits", "Total Profits Per Shop", Q_NULLPTR));
        filterTwoDatesProfitsShopsLabel->setText(QApplication::translate("Profits", "\302\2430.00", Q_NULLPTR));
        filterTwoDatesShopsLabel->setText(QApplication::translate("Profits", "Current Shop", Q_NULLPTR));
        filterTwoDatesRefreshButton->setText(QApplication::translate("Profits", "Refresh", Q_NULLPTR));
        dateOneLabel->setText(QApplication::translate("Profits", "Start Date", Q_NULLPTR));
        dateOneLineEdit->setText(QApplication::translate("Profits", "YYYY-MM-DD", Q_NULLPTR));
        dateTwoLabel->setText(QApplication::translate("Profits", "End Date", Q_NULLPTR));
        dateTwoLineEdit->setText(QApplication::translate("Profits", "YYYY-MM-DD", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("Profits", "Filter All time By Shop", Q_NULLPTR));
        filterAllTimeShopsProfitsLabel->setText(QApplication::translate("Profits", "\302\2430.00", Q_NULLPTR));
        filterAllTimeShopsLabel->setText(QApplication::translate("Profits", "Current Shop", Q_NULLPTR));
        groupBox_3->setTitle(QApplication::translate("Profits", "View Graphs", Q_NULLPTR));
        startDateLabel->setText(QApplication::translate("Profits", "Start Date", Q_NULLPTR));
        startDateLineEdit->setText(QApplication::translate("Profits", "YYYY-MM-DD", Q_NULLPTR));
        EndDateLabel->setText(QApplication::translate("Profits", "End Date", Q_NULLPTR));
        endDateLineEdit->setText(QApplication::translate("Profits", "YYYY-MM-DD", Q_NULLPTR));
        graphsRefreshButton->setText(QApplication::translate("Profits", "Refresh", Q_NULLPTR));
        allShopsCheckBox->setText(QApplication::translate("Profits", "All shops", Q_NULLPTR));
        shop2CheckBox->setText(QApplication::translate("Profits", "Shop 2", Q_NULLPTR));
        shop1CheckBox->setText(QApplication::translate("Profits", "Shop 1", Q_NULLPTR));
        shop3CheckBox->setText(QApplication::translate("Profits", "Shop 3", Q_NULLPTR));
        goBackButton->setText(QApplication::translate("Profits", "Go Back", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Profits: public Ui_Profits {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PROFITS_H
