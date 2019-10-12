/********************************************************************************
** Form generated from reading UI file 'adminhome.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADMINHOME_H
#define UI_ADMINHOME_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableView>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AdminHome
{
public:
    QGroupBox *welcomeGroupBox;
    QGroupBox *statistsicsGroupBox;
    QWidget *widget;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *statisticsProfitsButton;
    QPushButton *statisticsHiresButton;
    QGroupBox *staffGroupBox;
    QWidget *widget1;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *staffAddButton;
    QPushButton *staffRemoveButton;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *staffUpdateButton;
    QPushButton *staffViewButton;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *adminLogOutButton;
    QPushButton *resetPasswordButton;
    QTableView *tableView;

    void setupUi(QDialog *AdminHome)
    {
        if (AdminHome->objectName().isEmpty())
            AdminHome->setObjectName(QStringLiteral("AdminHome"));
        AdminHome->resize(807, 326);
        welcomeGroupBox = new QGroupBox(AdminHome);
        welcomeGroupBox->setObjectName(QStringLiteral("welcomeGroupBox"));
        welcomeGroupBox->setGeometry(QRect(10, 10, 251, 291));
        QFont font;
        font.setPointSize(12);
        welcomeGroupBox->setFont(font);
        statistsicsGroupBox = new QGroupBox(welcomeGroupBox);
        statistsicsGroupBox->setObjectName(QStringLiteral("statistsicsGroupBox"));
        statistsicsGroupBox->setGeometry(QRect(10, 160, 221, 71));
        widget = new QWidget(statistsicsGroupBox);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(21, 21, 184, 39));
        horizontalLayout_3 = new QHBoxLayout(widget);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        statisticsProfitsButton = new QPushButton(widget);
        statisticsProfitsButton->setObjectName(QStringLiteral("statisticsProfitsButton"));

        horizontalLayout_3->addWidget(statisticsProfitsButton);

        statisticsHiresButton = new QPushButton(widget);
        statisticsHiresButton->setObjectName(QStringLiteral("statisticsHiresButton"));

        horizontalLayout_3->addWidget(statisticsHiresButton);

        staffGroupBox = new QGroupBox(welcomeGroupBox);
        staffGroupBox->setObjectName(QStringLiteral("staffGroupBox"));
        staffGroupBox->setGeometry(QRect(10, 30, 221, 121));
        widget1 = new QWidget(staffGroupBox);
        widget1->setObjectName(QStringLiteral("widget1"));
        widget1->setGeometry(QRect(20, 21, 186, 86));
        verticalLayout = new QVBoxLayout(widget1);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        staffAddButton = new QPushButton(widget1);
        staffAddButton->setObjectName(QStringLiteral("staffAddButton"));

        horizontalLayout->addWidget(staffAddButton);

        staffRemoveButton = new QPushButton(widget1);
        staffRemoveButton->setObjectName(QStringLiteral("staffRemoveButton"));

        horizontalLayout->addWidget(staffRemoveButton);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        staffUpdateButton = new QPushButton(widget1);
        staffUpdateButton->setObjectName(QStringLiteral("staffUpdateButton"));

        horizontalLayout_2->addWidget(staffUpdateButton);

        staffViewButton = new QPushButton(widget1);
        staffViewButton->setObjectName(QStringLiteral("staffViewButton"));

        horizontalLayout_2->addWidget(staffViewButton);


        verticalLayout->addLayout(horizontalLayout_2);

        layoutWidget = new QWidget(welcomeGroupBox);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 240, 223, 39));
        horizontalLayout_5 = new QHBoxLayout(layoutWidget);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        adminLogOutButton = new QPushButton(layoutWidget);
        adminLogOutButton->setObjectName(QStringLiteral("adminLogOutButton"));

        horizontalLayout_5->addWidget(adminLogOutButton);

        resetPasswordButton = new QPushButton(layoutWidget);
        resetPasswordButton->setObjectName(QStringLiteral("resetPasswordButton"));

        horizontalLayout_5->addWidget(resetPasswordButton);

        tableView = new QTableView(AdminHome);
        tableView->setObjectName(QStringLiteral("tableView"));
        tableView->setGeometry(QRect(280, 10, 491, 291));

        retranslateUi(AdminHome);

        QMetaObject::connectSlotsByName(AdminHome);
    } // setupUi

    void retranslateUi(QDialog *AdminHome)
    {
        AdminHome->setWindowTitle(QApplication::translate("AdminHome", "Dialog", Q_NULLPTR));
        welcomeGroupBox->setTitle(QApplication::translate("AdminHome", "Welcome", Q_NULLPTR));
        statistsicsGroupBox->setTitle(QApplication::translate("AdminHome", "Statistics", Q_NULLPTR));
        statisticsProfitsButton->setText(QApplication::translate("AdminHome", "Profits", Q_NULLPTR));
        statisticsHiresButton->setText(QApplication::translate("AdminHome", "Hires", Q_NULLPTR));
        staffGroupBox->setTitle(QApplication::translate("AdminHome", "Staff", Q_NULLPTR));
        staffAddButton->setText(QApplication::translate("AdminHome", "Add", Q_NULLPTR));
        staffRemoveButton->setText(QApplication::translate("AdminHome", "Remove", Q_NULLPTR));
        staffUpdateButton->setText(QApplication::translate("AdminHome", "Update", Q_NULLPTR));
        staffViewButton->setText(QApplication::translate("AdminHome", "View", Q_NULLPTR));
        adminLogOutButton->setText(QApplication::translate("AdminHome", "Log Out", Q_NULLPTR));
        resetPasswordButton->setText(QApplication::translate("AdminHome", "Reset Password", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class AdminHome: public Ui_AdminHome {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMINHOME_H
