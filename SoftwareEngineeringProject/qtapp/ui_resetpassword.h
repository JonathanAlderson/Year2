/********************************************************************************
** Form generated from reading UI file 'resetpassword.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_RESETPASSWORD_H
#define UI_RESETPASSWORD_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_ResetPassword
{
public:
    QGroupBox *groupBox;
    QLineEdit *newPasswordLineEdit;
    QLabel *ConfirmNewPasswordLabel;
    QLineEdit *ConfirmNewPasswordLineEdit;
    QLineEdit *oldPasswordLineEdit;
    QLabel *newPasswordLabel;
    QLabel *oldPasswordLabel;
    QPushButton *confirmButton;
    QPushButton *cancelButton;

    void setupUi(QDialog *ResetPassword)
    {
        if (ResetPassword->objectName().isEmpty())
            ResetPassword->setObjectName(QStringLiteral("ResetPassword"));
        ResetPassword->resize(1010, 726);
        groupBox = new QGroupBox(ResetPassword);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 10, 211, 261));
        QFont font;
        font.setPointSize(11);
        groupBox->setFont(font);
        newPasswordLineEdit = new QLineEdit(groupBox);
        newPasswordLineEdit->setObjectName(QStringLiteral("newPasswordLineEdit"));
        newPasswordLineEdit->setGeometry(QRect(20, 110, 137, 36));
        newPasswordLineEdit->setEchoMode(QLineEdit::Password);
        ConfirmNewPasswordLabel = new QLabel(groupBox);
        ConfirmNewPasswordLabel->setObjectName(QStringLiteral("ConfirmNewPasswordLabel"));
        ConfirmNewPasswordLabel->setGeometry(QRect(20, 150, 154, 20));
        ConfirmNewPasswordLineEdit = new QLineEdit(groupBox);
        ConfirmNewPasswordLineEdit->setObjectName(QStringLiteral("ConfirmNewPasswordLineEdit"));
        ConfirmNewPasswordLineEdit->setGeometry(QRect(20, 170, 137, 36));
        ConfirmNewPasswordLineEdit->setEchoMode(QLineEdit::Password);
        oldPasswordLineEdit = new QLineEdit(groupBox);
        oldPasswordLineEdit->setObjectName(QStringLiteral("oldPasswordLineEdit"));
        oldPasswordLineEdit->setGeometry(QRect(20, 50, 137, 36));
        oldPasswordLineEdit->setEchoMode(QLineEdit::Password);
        newPasswordLabel = new QLabel(groupBox);
        newPasswordLabel->setObjectName(QStringLiteral("newPasswordLabel"));
        newPasswordLabel->setGeometry(QRect(20, 90, 98, 20));
        oldPasswordLabel = new QLabel(groupBox);
        oldPasswordLabel->setObjectName(QStringLiteral("oldPasswordLabel"));
        oldPasswordLabel->setGeometry(QRect(20, 30, 91, 20));
        confirmButton = new QPushButton(groupBox);
        confirmButton->setObjectName(QStringLiteral("confirmButton"));
        confirmButton->setGeometry(QRect(110, 210, 88, 36));
        cancelButton = new QPushButton(groupBox);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));
        cancelButton->setGeometry(QRect(20, 210, 88, 36));

        retranslateUi(ResetPassword);

        QMetaObject::connectSlotsByName(ResetPassword);
    } // setupUi

    void retranslateUi(QDialog *ResetPassword)
    {
        ResetPassword->setWindowTitle(QApplication::translate("ResetPassword", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("ResetPassword", "Reset Password", Q_NULLPTR));
        ConfirmNewPasswordLabel->setText(QApplication::translate("ResetPassword", "Confirm New Password", Q_NULLPTR));
        newPasswordLabel->setText(QApplication::translate("ResetPassword", "New Password", Q_NULLPTR));
        oldPasswordLabel->setText(QApplication::translate("ResetPassword", "Old Password", Q_NULLPTR));
        confirmButton->setText(QApplication::translate("ResetPassword", "Confirm ", Q_NULLPTR));
        cancelButton->setText(QApplication::translate("ResetPassword", "Cancel", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class ResetPassword: public Ui_ResetPassword {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_RESETPASSWORD_H
