/********************************************************************************
** Form generated from reading UI file 'updatestaff.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UPDATESTAFF_H
#define UI_UPDATESTAFF_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_UpdateStaff
{
public:
    QGroupBox *groupBox;
    QGroupBox *groupBox_2;
    QLabel *currentNameLabel;
    QLabel *currentEmailLabel;
    QLabel *currentContactNumberLabel;
    QLabel *currentAddressLabel;
    QLabel *currentShopLabel;
    QLabel *currentAdminRightsLabel;
    QLabel *currentIDLabel;
    QGroupBox *groupBox_3;
    QLineEdit *updatePersonalDetailsLineEdit;
    QComboBox *personalDetailsComboBox;
    QPushButton *updatePersonalDetailsButton;
    QGroupBox *groupBox_5;
    QComboBox *updateAdminComboBox;
    QPushButton *updateAdminButton;
    QPushButton *cancelButton;
    QPushButton *findButton;
    QWidget *widget;
    QHBoxLayout *horizontalLayout;
    QLabel *emailLabel;
    QLineEdit *emailLineEdit;

    void setupUi(QDialog *UpdateStaff)
    {
        if (UpdateStaff->objectName().isEmpty())
            UpdateStaff->setObjectName(QStringLiteral("UpdateStaff"));
        UpdateStaff->resize(989, 835);
        groupBox = new QGroupBox(UpdateStaff);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 10, 631, 421));
        QFont font;
        font.setPointSize(11);
        groupBox->setFont(font);
        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(10, 70, 611, 161));
        currentNameLabel = new QLabel(groupBox_2);
        currentNameLabel->setObjectName(QStringLiteral("currentNameLabel"));
        currentNameLabel->setGeometry(QRect(12, 40, 601, 20));
        currentEmailLabel = new QLabel(groupBox_2);
        currentEmailLabel->setObjectName(QStringLiteral("currentEmailLabel"));
        currentEmailLabel->setGeometry(QRect(12, 60, 601, 20));
        currentContactNumberLabel = new QLabel(groupBox_2);
        currentContactNumberLabel->setObjectName(QStringLiteral("currentContactNumberLabel"));
        currentContactNumberLabel->setGeometry(QRect(12, 80, 601, 20));
        currentAddressLabel = new QLabel(groupBox_2);
        currentAddressLabel->setObjectName(QStringLiteral("currentAddressLabel"));
        currentAddressLabel->setGeometry(QRect(12, 100, 601, 20));
        currentShopLabel = new QLabel(groupBox_2);
        currentShopLabel->setObjectName(QStringLiteral("currentShopLabel"));
        currentShopLabel->setGeometry(QRect(12, 120, 601, 20));
        currentAdminRightsLabel = new QLabel(groupBox_2);
        currentAdminRightsLabel->setObjectName(QStringLiteral("currentAdminRightsLabel"));
        currentAdminRightsLabel->setGeometry(QRect(12, 140, 601, 20));
        currentIDLabel = new QLabel(groupBox_2);
        currentIDLabel->setObjectName(QStringLiteral("currentIDLabel"));
        currentIDLabel->setGeometry(QRect(12, 20, 601, 20));
        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setGeometry(QRect(10, 240, 611, 61));
        updatePersonalDetailsLineEdit = new QLineEdit(groupBox_3);
        updatePersonalDetailsLineEdit->setObjectName(QStringLiteral("updatePersonalDetailsLineEdit"));
        updatePersonalDetailsLineEdit->setGeometry(QRect(20, 20, 137, 36));
        personalDetailsComboBox = new QComboBox(groupBox_3);
        personalDetailsComboBox->setObjectName(QStringLiteral("personalDetailsComboBox"));
        personalDetailsComboBox->setGeometry(QRect(160, 20, 171, 36));
        updatePersonalDetailsButton = new QPushButton(groupBox_3);
        updatePersonalDetailsButton->setObjectName(QStringLiteral("updatePersonalDetailsButton"));
        updatePersonalDetailsButton->setGeometry(QRect(340, 20, 88, 36));
        groupBox_5 = new QGroupBox(groupBox);
        groupBox_5->setObjectName(QStringLiteral("groupBox_5"));
        groupBox_5->setGeometry(QRect(10, 310, 611, 61));
        updateAdminComboBox = new QComboBox(groupBox_5);
        updateAdminComboBox->setObjectName(QStringLiteral("updateAdminComboBox"));
        updateAdminComboBox->setGeometry(QRect(20, 20, 77, 36));
        updateAdminButton = new QPushButton(groupBox_5);
        updateAdminButton->setObjectName(QStringLiteral("updateAdminButton"));
        updateAdminButton->setGeometry(QRect(101, 20, 88, 36));
        cancelButton = new QPushButton(groupBox);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));
        cancelButton->setGeometry(QRect(10, 380, 88, 36));
        findButton = new QPushButton(groupBox);
        findButton->setObjectName(QStringLiteral("findButton"));
        findButton->setGeometry(QRect(210, 20, 88, 36));
        widget = new QWidget(groupBox);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(20, 20, 180, 38));
        horizontalLayout = new QHBoxLayout(widget);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        emailLabel = new QLabel(widget);
        emailLabel->setObjectName(QStringLiteral("emailLabel"));

        horizontalLayout->addWidget(emailLabel);

        emailLineEdit = new QLineEdit(widget);
        emailLineEdit->setObjectName(QStringLiteral("emailLineEdit"));

        horizontalLayout->addWidget(emailLineEdit);


        retranslateUi(UpdateStaff);

        QMetaObject::connectSlotsByName(UpdateStaff);
    } // setupUi

    void retranslateUi(QDialog *UpdateStaff)
    {
        UpdateStaff->setWindowTitle(QApplication::translate("UpdateStaff", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("UpdateStaff", "Update Staff", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("UpdateStaff", "Current Details", Q_NULLPTR));
        currentNameLabel->setText(QApplication::translate("UpdateStaff", "Name : ", Q_NULLPTR));
        currentEmailLabel->setText(QApplication::translate("UpdateStaff", "Email :", Q_NULLPTR));
        currentContactNumberLabel->setText(QApplication::translate("UpdateStaff", "Contact Number :", Q_NULLPTR));
        currentAddressLabel->setText(QApplication::translate("UpdateStaff", "Address :", Q_NULLPTR));
        currentShopLabel->setText(QApplication::translate("UpdateStaff", "Shop :", Q_NULLPTR));
        currentAdminRightsLabel->setText(QApplication::translate("UpdateStaff", "Admin Rights : ", Q_NULLPTR));
        currentIDLabel->setText(QApplication::translate("UpdateStaff", "ID :", Q_NULLPTR));
        groupBox_3->setTitle(QApplication::translate("UpdateStaff", "Update Personal Details", Q_NULLPTR));
        personalDetailsComboBox->clear();
        personalDetailsComboBox->insertItems(0, QStringList()
         << QApplication::translate("UpdateStaff", "Name", Q_NULLPTR)
         << QApplication::translate("UpdateStaff", "Email", Q_NULLPTR)
         << QApplication::translate("UpdateStaff", "Contact Number", Q_NULLPTR)
         << QApplication::translate("UpdateStaff", "Address", Q_NULLPTR)
        );
        updatePersonalDetailsButton->setText(QApplication::translate("UpdateStaff", "Update", Q_NULLPTR));
        groupBox_5->setTitle(QApplication::translate("UpdateStaff", "Update Admin", Q_NULLPTR));
        updateAdminComboBox->clear();
        updateAdminComboBox->insertItems(0, QStringList()
         << QApplication::translate("UpdateStaff", "Yes", Q_NULLPTR)
         << QApplication::translate("UpdateStaff", "No", Q_NULLPTR)
        );
        updateAdminButton->setText(QApplication::translate("UpdateStaff", "Update", Q_NULLPTR));
        cancelButton->setText(QApplication::translate("UpdateStaff", "Cancel", Q_NULLPTR));
        findButton->setText(QApplication::translate("UpdateStaff", "Find", Q_NULLPTR));
        emailLabel->setText(QApplication::translate("UpdateStaff", "Email", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class UpdateStaff: public Ui_UpdateStaff {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UPDATESTAFF_H
