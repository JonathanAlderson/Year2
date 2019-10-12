/********************************************************************************
** Form generated from reading UI file 'removestaff.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_REMOVESTAFF_H
#define UI_REMOVESTAFF_H

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
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_RemoveStaff
{
public:
    QGroupBox *groupBox;
    QWidget *widget;
    QHBoxLayout *horizontalLayout;
    QLabel *emailLabel;
    QLineEdit *emailLineEdit;
    QWidget *widget1;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *cancelButton;
    QPushButton *removeButton;

    void setupUi(QDialog *RemoveStaff)
    {
        if (RemoveStaff->objectName().isEmpty())
            RemoveStaff->setObjectName(QStringLiteral("RemoveStaff"));
        RemoveStaff->resize(466, 398);
        groupBox = new QGroupBox(RemoveStaff);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 10, 221, 121));
        QFont font;
        font.setPointSize(11);
        groupBox->setFont(font);
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

        widget1 = new QWidget(groupBox);
        widget1->setObjectName(QStringLiteral("widget1"));
        widget1->setGeometry(QRect(20, 70, 184, 38));
        horizontalLayout_2 = new QHBoxLayout(widget1);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        cancelButton = new QPushButton(widget1);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));

        horizontalLayout_2->addWidget(cancelButton);

        removeButton = new QPushButton(widget1);
        removeButton->setObjectName(QStringLiteral("removeButton"));

        horizontalLayout_2->addWidget(removeButton);


        retranslateUi(RemoveStaff);

        QMetaObject::connectSlotsByName(RemoveStaff);
    } // setupUi

    void retranslateUi(QDialog *RemoveStaff)
    {
        RemoveStaff->setWindowTitle(QApplication::translate("RemoveStaff", "Dialog", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("RemoveStaff", "Remove Staff", Q_NULLPTR));
        emailLabel->setText(QApplication::translate("RemoveStaff", "Email", Q_NULLPTR));
        cancelButton->setText(QApplication::translate("RemoveStaff", "Cancel", Q_NULLPTR));
        removeButton->setText(QApplication::translate("RemoveStaff", "Remove", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class RemoveStaff: public Ui_RemoveStaff {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_REMOVESTAFF_H
