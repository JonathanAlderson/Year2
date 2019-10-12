/********************************************************************************
** Form generated from reading UI file 'addstaff.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADDSTAFF_H
#define UI_ADDSTAFF_H

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
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AddStaff
{
public:
    QGroupBox *groupBox;
    QPushButton *cancelButton;
    QPushButton *addStaffButton;
    QRadioButton *adminButton;
    QWidget *widget;
    QHBoxLayout *horizontalLayout;
    QLabel *nameLabel;
    QLineEdit *nameLineEdit;
    QWidget *widget1;
    QHBoxLayout *horizontalLayout_2;
    QLabel *emailLabel;
    QLineEdit *emailLineEdit;
    QWidget *widget2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *passwordLabel;
    QLineEdit *passwordLineEdit;
    QWidget *widget3;
    QHBoxLayout *horizontalLayout_4;
    QLabel *confirmPasswordLabel;
    QLineEdit *confirmPasswordLineEdit;
    QWidget *widget4;
    QHBoxLayout *horizontalLayout_5;
    QLabel *contactNumberLabel;
    QLineEdit *contactNumberLineEdit;
    QWidget *widget5;
    QHBoxLayout *horizontalLayout_6;
    QLabel *adressLabel;
    QLineEdit *AddressLineEdit;
    QLabel *shopIdLabel;
    QComboBox *shopIDComboBox;

    void setupUi(QDialog *AddStaff)
    {
        if (AddStaff->objectName().isEmpty())
            AddStaff->setObjectName(QStringLiteral("AddStaff"));
        AddStaff->resize(505, 533);
        groupBox = new QGroupBox(AddStaff);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 10, 311, 481));
        QFont font;
        font.setPointSize(11);
        groupBox->setFont(font);
        cancelButton = new QPushButton(groupBox);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));
        cancelButton->setGeometry(QRect(20, 430, 88, 36));
        addStaffButton = new QPushButton(groupBox);
        addStaffButton->setObjectName(QStringLiteral("addStaffButton"));
        addStaffButton->setGeometry(QRect(110, 430, 88, 36));
        adminButton = new QRadioButton(groupBox);
        adminButton->setObjectName(QStringLiteral("adminButton"));
        adminButton->setGeometry(QRect(20, 340, 70, 26));
        widget = new QWidget(groupBox);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(20, 40, 274, 38));
        horizontalLayout = new QHBoxLayout(widget);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        nameLabel = new QLabel(widget);
        nameLabel->setObjectName(QStringLiteral("nameLabel"));
        nameLabel->setFont(font);

        horizontalLayout->addWidget(nameLabel);

        nameLineEdit = new QLineEdit(widget);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));

        horizontalLayout->addWidget(nameLineEdit);

        widget1 = new QWidget(groupBox);
        widget1->setObjectName(QStringLiteral("widget1"));
        widget1->setGeometry(QRect(20, 90, 274, 38));
        horizontalLayout_2 = new QHBoxLayout(widget1);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        emailLabel = new QLabel(widget1);
        emailLabel->setObjectName(QStringLiteral("emailLabel"));
        emailLabel->setFont(font);

        horizontalLayout_2->addWidget(emailLabel);

        emailLineEdit = new QLineEdit(widget1);
        emailLineEdit->setObjectName(QStringLiteral("emailLineEdit"));

        horizontalLayout_2->addWidget(emailLineEdit);

        widget2 = new QWidget(groupBox);
        widget2->setObjectName(QStringLiteral("widget2"));
        widget2->setGeometry(QRect(20, 140, 274, 38));
        horizontalLayout_3 = new QHBoxLayout(widget2);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        passwordLabel = new QLabel(widget2);
        passwordLabel->setObjectName(QStringLiteral("passwordLabel"));
        passwordLabel->setFont(font);

        horizontalLayout_3->addWidget(passwordLabel);

        passwordLineEdit = new QLineEdit(widget2);
        passwordLineEdit->setObjectName(QStringLiteral("passwordLineEdit"));
        passwordLineEdit->setEchoMode(QLineEdit::Password);

        horizontalLayout_3->addWidget(passwordLineEdit);

        widget3 = new QWidget(groupBox);
        widget3->setObjectName(QStringLiteral("widget3"));
        widget3->setGeometry(QRect(20, 190, 273, 38));
        horizontalLayout_4 = new QHBoxLayout(widget3);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        confirmPasswordLabel = new QLabel(widget3);
        confirmPasswordLabel->setObjectName(QStringLiteral("confirmPasswordLabel"));
        confirmPasswordLabel->setFont(font);

        horizontalLayout_4->addWidget(confirmPasswordLabel);

        confirmPasswordLineEdit = new QLineEdit(widget3);
        confirmPasswordLineEdit->setObjectName(QStringLiteral("confirmPasswordLineEdit"));
        confirmPasswordLineEdit->setEchoMode(QLineEdit::Password);

        horizontalLayout_4->addWidget(confirmPasswordLineEdit);

        widget4 = new QWidget(groupBox);
        widget4->setObjectName(QStringLiteral("widget4"));
        widget4->setGeometry(QRect(20, 240, 274, 38));
        horizontalLayout_5 = new QHBoxLayout(widget4);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        contactNumberLabel = new QLabel(widget4);
        contactNumberLabel->setObjectName(QStringLiteral("contactNumberLabel"));
        contactNumberLabel->setFont(font);

        horizontalLayout_5->addWidget(contactNumberLabel);

        contactNumberLineEdit = new QLineEdit(widget4);
        contactNumberLineEdit->setObjectName(QStringLiteral("contactNumberLineEdit"));

        horizontalLayout_5->addWidget(contactNumberLineEdit);

        widget5 = new QWidget(groupBox);
        widget5->setObjectName(QStringLiteral("widget5"));
        widget5->setGeometry(QRect(20, 290, 276, 38));
        horizontalLayout_6 = new QHBoxLayout(widget5);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(0, 0, 0, 0);
        adressLabel = new QLabel(widget5);
        adressLabel->setObjectName(QStringLiteral("adressLabel"));

        horizontalLayout_6->addWidget(adressLabel);

        AddressLineEdit = new QLineEdit(widget5);
        AddressLineEdit->setObjectName(QStringLiteral("AddressLineEdit"));

        horizontalLayout_6->addWidget(AddressLineEdit);

        shopIdLabel = new QLabel(groupBox);
        shopIdLabel->setObjectName(QStringLiteral("shopIdLabel"));
        shopIdLabel->setGeometry(QRect(20, 380, 53, 20));
        shopIDComboBox = new QComboBox(groupBox);
        shopIDComboBox->setObjectName(QStringLiteral("shopIDComboBox"));
        shopIDComboBox->setGeometry(QRect(90, 380, 103, 36));

        retranslateUi(AddStaff);

        QMetaObject::connectSlotsByName(AddStaff);
    } // setupUi

    void retranslateUi(QDialog *AddStaff)
    {
        AddStaff->setWindowTitle(QApplication::translate("AddStaff", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("AddStaff", "Add Staff Form", Q_NULLPTR));
        cancelButton->setText(QApplication::translate("AddStaff", "Cancel", Q_NULLPTR));
        addStaffButton->setText(QApplication::translate("AddStaff", "Add Staff", Q_NULLPTR));
        adminButton->setText(QApplication::translate("AddStaff", "Admin", Q_NULLPTR));
        nameLabel->setText(QApplication::translate("AddStaff", "Name                      ", Q_NULLPTR));
        emailLabel->setText(QApplication::translate("AddStaff", "Email                       ", Q_NULLPTR));
        passwordLabel->setText(QApplication::translate("AddStaff", "Password                ", Q_NULLPTR));
        confirmPasswordLabel->setText(QApplication::translate("AddStaff", "Confirm Password  ", Q_NULLPTR));
        contactNumberLabel->setText(QApplication::translate("AddStaff", "Contact Number     ", Q_NULLPTR));
        adressLabel->setText(QApplication::translate("AddStaff", "Address                   ", Q_NULLPTR));
        shopIdLabel->setText(QApplication::translate("AddStaff", "Shop ID", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class AddStaff: public Ui_AddStaff {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADDSTAFF_H
