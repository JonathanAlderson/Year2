#include "resetpassword.h"
#include "ui_resetpassword.h"
#include "mainwindow.h"

ResetPassword::ResetPassword(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ResetPassword)
{
    ui->setupUi(this);
}

ResetPassword::~ResetPassword()
{
    delete ui;
}

void ResetPassword::setEmail(QString _email)
{
    email = _email;
}

void ResetPassword::on_cancelButton_clicked()
{
    this->close();
}

void ResetPassword::on_confirmButton_clicked()
{
    // Display question to check user wants to cancel
    QMessageBox::StandardButton reply = QMessageBox::question(this,"16Cycles","Are you sure you want to reset your password?",
                                                              QMessageBox::Yes | QMessageBox::No);

    if(reply == QMessageBox::Yes)
    {
        // Try open database connection
        MainWindow mainWindow;
        if(!mainWindow.openConnection())
        {
            QMessageBox::critical(this,"16CyclesAddStaff","Failed to open database. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error opening db add staff");
        }

        // Prepare query to find username and password in database
        QSqlQuery query;
        query.prepare("SELECT password FROM staff WHERE email = '" + email + "'");

        // Execute query
        if(!query.exec())
        {
            QMessageBox::critical(this,"16CyclesAddStaff","Failed to run query. Contact the 16Cycles IT Support Team");
            return;
        }

        // If query returned a value, log in user
        if(query.next())
        {
            // Decrypt password
            SimpleCrypt crypto(Q_UINT64_C(0x0c2ad4a4acb9f023));
            QString passwordDecrypt = crypto.decryptToString(query.value(0).toString());
            QString oldPassword = ui-> oldPasswordLineEdit-> text();

            // Compare with users input
            if(QString::compare(oldPassword,passwordDecrypt,Qt::CaseSensitive) != 0)
            {
                QMessageBox::critical(this,"16Cycles","Incorrect old password");
                // Close the database connection
                mainWindow.closeConnection();
                return;
            }

            QString newPassword = ui-> newPasswordLineEdit-> text();
            QString confirmNewPassword = ui-> ConfirmNewPasswordLineEdit-> text();

            // Check length of passwords
            if(newPassword.length() < 5)
            {
                QMessageBox::critical(this,"16Cycles","New password too short");
                // Close the database connection
                mainWindow.closeConnection();
                return;
            }

            // Compare new password and confirm new password
            if(QString::compare(newPassword,confirmNewPassword,Qt::CaseSensitive) != 0)
            {
                QMessageBox::critical(this,"16Cycles","New passwords do not match");
                // Close the database connection
                mainWindow.closeConnection();
                return;
            }

            // Ensure new password and old password are different
            if(QString::compare(newPassword,oldPassword,Qt::CaseSensitive) == 0)
            {
                QMessageBox::critical(this,"16Cycles","New passwords must be different from your old password");
                // Close the database connection
                mainWindow.closeConnection();
                return;
            }

            // Encrypt new password
            QString passwordEncrypted = crypto.encryptToString(newPassword);

            // Add new password to database
            query.prepare("UPDATE staff SET password = '" + passwordEncrypted + "' WHERE email = '" + email + "'");

            // Execute query
            if(!query.exec())
            {
                QMessageBox::critical(this,"16CyclesResetPassword","Failed to run query. Contact the 16Cycles IT Support Team");
                // Close the database connection
                mainWindow.closeConnection();
                return;
            }

            QMessageBox::information(this,"16CyclesResetPassword","Password successfully changed. Don't forget it.");
        }
        else
        {
            QMessageBox::critical(this,"16CyclesResetPassword","Username not found");
        }
        // Close the database connection
        mainWindow.closeConnection();

        // Clear line edits
        ui-> newPasswordLineEdit-> clear();
        ui-> oldPasswordLineEdit-> clear();
        ui-> ConfirmNewPasswordLineEdit-> clear();
    }
}
