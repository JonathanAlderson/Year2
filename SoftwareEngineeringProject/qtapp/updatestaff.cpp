#include "updatestaff.h"
#include "ui_updatestaff.h"
#include "mainwindow.h"

UpdateStaff::UpdateStaff(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::UpdateStaff)
{
    ui->setupUi(this);
    findSuccess = false;
}

UpdateStaff::~UpdateStaff()
{
    delete ui;
}

void UpdateStaff::on_findButton_clicked()
{
    // Open database
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to open database. Contact the 16Cycles IT Support Team");
        this->close();
        qDebug()<<("Error opening db update staff");
    }

    // Reset Labels in case second press
    ui-> currentIDLabel-> setText("ID : ");
    ui-> currentNameLabel-> setText("Name : ");
    ui-> currentEmailLabel-> setText("Email : ");
    ui-> currentContactNumberLabel-> setText("Contact Number : ");
    ui-> currentAddressLabel-> setText("Address : ");
    ui-> currentShopLabel-> setText("Shop : ");
    ui-> currentAdminRightsLabel-> setText("Admin Rights : ");

    // Get text from email line edit
    QString email;
    email = ui-> emailLineEdit-> text();

    // Query to find staff
    QSqlQuery query;
    query.prepare("SELECT * FROM staff WHERE email = '" + email + "'");
    if(!query.exec())
    {
        QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to find staff. Contact the 16Cycles IT Support Team");
        this->close();
        qDebug()<<("Error find staff");
    }

    // Check staff member exists
    if(!query.next())
    {
        QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to find staff.");
        // Set find success
        findSuccess = false;
        return;
    }

    // Set find success
    findSuccess = true;

    // Set current details of staff
    QString currentID,currentName,currentEmail,currentContactNumber,currentAddress,currentAdmin,currentShopID;
    int currentAdminInt;
    currentID = "ID : " + query.value(0).toString();
    currentName = "Name : " + query.value(4).toString();
    currentEmail = "Email : " + query.value(1).toString();
    currentContactNumber = "Contact Number : " + query.value(3).toString();
    currentAddress = "Address : " + query.value(5).toString();
    currentShopID = "Shop : " + query.value(7).toString();
    currentAdminInt = query.value(6).toInt();
    ui-> currentIDLabel-> setText(currentID);
    ui-> currentNameLabel-> setText(currentName);
    ui-> currentEmailLabel-> setText(currentEmail);
    ui-> currentContactNumberLabel-> setText(currentContactNumber);
    ui-> currentAddressLabel-> setText(currentAddress);
    ui-> currentShopLabel-> setText(currentShopID);
    if(currentAdminInt == 1)
    {
        currentAdmin = "Admin Rights : Yes";
    }
    else
    {
        currentAdmin = "Admin Rights : No";
    }
    ui-> currentAdminRightsLabel-> setText(currentAdmin);

    // Close connection
    mainWindow.closeConnection();
}

void UpdateStaff::on_cancelButton_clicked()
{
    this-> close();
}

void UpdateStaff::on_updateAdminButton_clicked()
{
    // Open database
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to open database. Contact the 16Cycles IT Support Team");
        this->close();
        qDebug()<<("Error open db update admin");
    }

    // Check find success
    if(findSuccess)
    {
        // Get email
        QString email;
        email = ui-> emailLineEdit-> text();

        // Get admin
        QString admin,adminLabel;
        admin = ui-> updateAdminComboBox-> currentText();

        // Set admin int
        int adminInt;
        QString yes = "Yes";
        if(QString::compare(yes,admin,Qt::CaseSensitive) != 0)
        {
            adminInt = 0;
            adminLabel = "Admin Rights : No";
        }
        else
        {
            adminInt = 1;
            adminLabel = "Admin Rights : Yes";
        }

        // Query to update admin
        QSqlQuery query;
        query.prepare("UPDATE staff SET admin = :admin WHERE email = '" + email + "'");
        query.bindValue(":admin",adminInt);
        if(!query.exec())
        {
            QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to update. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error update admin");
        }

        // Success
        QMessageBox::information(this,"16CyclesUpdateAdmin","Successfully updated admin");

        // Reset label
        ui-> currentAdminRightsLabel-> setText(adminLabel);
    }

    else
    {
       QMessageBox::critical(this,"16CyclesUpdateStaff","find staff first");
    }

    // Close connection
    mainWindow.closeConnection();
}

void UpdateStaff::on_updatePersonalDetailsButton_clicked()
{
    /*
        Does not error check. down to user to ensure detials entered right on form
        If there is an sql error, will just have message to contact support team
    */

    // Ask user if details correct
    QMessageBox::StandardButton reply = QMessageBox::question(this,"16Cycles","Are you sure details are correct?",
                                                              QMessageBox::Yes | QMessageBox::No);

    // Close window if yes clicked, else do nothing
    if(reply == QMessageBox::Yes)
    {
        // Open database
        MainWindow mainWindow;
        if(!mainWindow.openConnection())
        {
            QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to open database. Contact the 16Cycles IT Support Team");
            this->close();
            qDebug()<<("Error open db update details");
        }

        // Check find success
        if(findSuccess)
        {
            // Get email
            QString email;
            email = ui-> emailLineEdit-> text();

            // Get combo box text
            QString comboBoxText;
            comboBoxText = ui-> personalDetailsComboBox-> currentText();

            // Get line edit text
            QString newDetails;
            newDetails = ui-> updatePersonalDetailsLineEdit-> text();

            // Compare combobox to decide which details to update
            QString name = "Name";
            QString emailComp = "Email";
            QString contactNumber = "Contact Number";
            QString address = "Address";
            if(QString::compare(name,comboBoxText,Qt::CaseSensitive) == 0)
            {
                // Update Name
                QSqlQuery query;
                query.prepare("UPDATE staff SET name = '" + newDetails + "' WHERE email = '" + email + "'");
                if(!query.exec())
                {
                    QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to update. Contact the 16Cycles IT Support Team");
                    this->close();
                    qDebug()<<("Error update name");
                }

                // Success
                QMessageBox::information(this,"16CyclesUpdateAdmin","Successfully updated name");

                // Reset label
                QString newLabel = "Name : ";
                newLabel += newDetails;
                ui-> currentNameLabel-> setText(newLabel);
            }
            else if(QString::compare(emailComp,comboBoxText,Qt::CaseSensitive) == 0)
            {
                // Update email
                QSqlQuery query;
                query.prepare("UPDATE staff SET email = '" + newDetails + "' WHERE email = '" + email + "'");
                if(!query.exec())
                {
                    QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to update. Contact the 16Cycles IT Support Team");
                    this->close();
                    qDebug()<<("Error update email");
                }

                // Success
                QMessageBox::information(this,"16CyclesUpdateAdmin","Successfully updated email");

                // Reset label
                QString newLabel = "Email : ";
                newLabel += newDetails;
                ui-> currentEmailLabel-> setText(newLabel);
            }
            else if(QString::compare(contactNumber,comboBoxText,Qt::CaseSensitive) == 0)
            {
                // Update contact Number
                QSqlQuery query;
                query.prepare("UPDATE staff SET contact_number = :contactNumber WHERE email = '" + email + "'");
                query.bindValue(":contactNumber",newDetails);
                if(!query.exec())
                {
                    QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to update. Contact the 16Cycles IT Support Team");
                    this->close();
                    qDebug()<<("Error update contact number");
                }

                // Success
                QMessageBox::information(this,"16CyclesUpdateAdmin","Successfully updated contact details");

                // Reset label
                QString newLabel = "Contact Number : ";
                newLabel += newDetails;
                ui-> currentContactNumberLabel-> setText(newLabel);
            }
            else
            {
                // Update Address
                QSqlQuery query;
                query.prepare("UPDATE staff SET address = '" + newDetails + "' WHERE email = '" + email + "'");
                if(!query.exec())
                {
                    QMessageBox::critical(this,"16CyclesUpdateStaff","Failed to update. Contact the 16Cycles IT Support Team");
                    this->close();
                    qDebug()<<("Error update address");
                }

                // Success
                QMessageBox::information(this,"16CyclesUpdateAdmin","Successfully updated address");

                // Reset label
                QString newLabel = "Address : ";
                newLabel += newDetails;
                ui-> currentAddressLabel-> setText(newLabel);
            }
        }
        else
        {
            QMessageBox::critical(this,"16CyclesUpdateStaff","find staff first");
        }

        // Close connection
        mainWindow.closeConnection();
    }

    ui-> updatePersonalDetailsLineEdit-> clear();
}
