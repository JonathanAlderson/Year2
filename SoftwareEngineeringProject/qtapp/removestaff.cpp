#include "removestaff.h"
#include "ui_removestaff.h"
#include "mainwindow.h"

RemoveStaff::RemoveStaff(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::RemoveStaff)
{
    ui->setupUi(this);
}

RemoveStaff::~RemoveStaff()
{
    delete ui;
}

void RemoveStaff::on_removeButton_clicked()
{
    // Display question to check user wants to quit
    QMessageBox::StandardButton reply = QMessageBox::question(this,"16Cycles","Are you sure you want to remove this staff member? This action cannot be undone.",
                                                              QMessageBox::Yes | QMessageBox::No);

    // Close window if yes clicked, else do nothing
    if(reply == QMessageBox::Yes)
    {
        // Try to open the database
        MainWindow mainWindow;

        // Close if failed to open connection
        if(!mainWindow.openConnection())
        {
            QMessageBox::critical(this,"16CyclesRemoveStaff","Failed to open database. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error opening db add staff");
        }

        // Get email from line edit
        QString email;
        email = ui-> emailLineEdit-> text();

        // Query to ensure staff memebr exists
        QSqlQuery query;
        query.prepare("SELECT * FROM staff WHERE email = '" + email + "'");

        if(!query.exec())
        {
            QMessageBox::critical(this,"16CyclesRemoveStaff","Failed to find staff. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error find staff");
        }

        if(!query.next())
        {
            QMessageBox::critical(this,"16CyclesRemoveStaff","This email does not exist.");
            return;
        }

        // Query to remove staff member

        query.prepare("DELETE FROM staff WHERE email = '" + email + "'");
        if(!query.exec())
        {
            QMessageBox::critical(this,"16CyclesRemoveStaff","Failed to remove staff. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error remove staff");
        }

        QMessageBox::information(this,"16CyclesRemoveStaff","Successfully removed staff");

        // Clear line edits
        foreach(QLineEdit* lineEdit, findChildren<QLineEdit*>())
        {
            lineEdit->clear();
        }

        // Close connection
        mainWindow.closeConnection();
    }
}

void RemoveStaff::on_cancelButton_clicked()
{
    this-> close();
}
