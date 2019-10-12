#include "addstaff.h"
#include "ui_addstaff.h"
#include "mainwindow.h"

AddStaff::AddStaff(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AddStaff)
{
    ui->setupUi(this);

    // Set validator for contact number
    ui-> contactNumberLineEdit-> setValidator(
                new QRegularExpressionValidator(QRegularExpression("[0-9]\\d{0,10}"),this));

    // Populate combo box
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQueryModel *model = new QSqlQueryModel();
    QSqlQuery *query = new QSqlQuery(mainWindow.db);

    // Query to get all current shops id's
    query-> prepare("SELECT id FROM shops");
    query-> exec();
    if(!query-> next())
    {
        this-> close();
        qDebug()<<("error bikes");
    }

    mainWindow.close();

    model-> setQuery(*query);

    ui-> shopIDComboBox-> setModel(model);
}

AddStaff::~AddStaff()
{
    delete ui;
}

void AddStaff::on_cancelButton_clicked()
{
    this->close();
}

void AddStaff::on_addStaffButton_clicked()
{
    // Display question to check user wants to cancel
    QMessageBox::StandardButton reply = QMessageBox::question(this,"16Cycles","Are you sure all your data is correct?",
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

        // Create strings to store values from text edit fields
        QString name,email,password,confirmPassword,contactNumber,address,shopID;
        bool admin;

        // Get all data from form
        name = ui-> nameLineEdit-> text();
        email = ui-> emailLineEdit-> text();
        password = ui-> passwordLineEdit-> text();
        confirmPassword = ui-> confirmPasswordLineEdit -> text();
        contactNumber = ui-> contactNumberLineEdit-> text();
        address = ui-> AddressLineEdit-> text();
        admin = ui-> adminButton-> isChecked();
        shopID = ui-> shopIDComboBox-> currentText();

        // Check all fields entered
        if(name.length() != 0 && email.length() != 0 && password.length() != 0
                && confirmPassword.length() != 0 && address.length() != 0)
        {
            // Check contact number length
            if(contactNumber.length() == 11)
            {
                // Check passwords minimum length
                if(password.length() >= 5)
                {
                    // Check password and confirm password match
                    if((QString::compare(password,confirmPassword,Qt::CaseSensitive)) == 0)
                    {
                        // Check database for duplicate staff
                        QSqlQuery query;
                        query.prepare("SELECT * FROM staff WHERE email = '" + email + "'");
                        query.exec();
                        if(!query.next())
                        {
                            // Query to get next available id
                            query.prepare("SELECT * FROM staff ORDER BY id DESC LIMIT 1");
                            query.exec();
                            if(!query.next())
                            {
                                QMessageBox::critical(this,"16CyclesAddStaff","Failed to add staff. Contact the 16Cycles IT Support Team");
                                qDebug()<<(query.lastError().text());

                                // Close the database connection
                                mainWindow.closeConnection();
                                return;
                            }
                            int id = query.value(0).toInt();
                            id = id + 1;

                            // Get admin as int for query
                            int adminAsInt = 0;
                            if(admin == true)
                            {
                                adminAsInt = 1;
                            }

                            // Encrypt password
                            SimpleCrypt crypto(Q_UINT64_C(0x0c2ad4a4acb9f023));
                            QString passwordEncrypted = crypto.encryptToString(password);

                            // Query to add staff
                            query.prepare("INSERT INTO staff VALUES (:id, :email, :password, :contact_number, :name, :address, :admin, :shop_id)");
                            query.bindValue(":id",id);
                            query.bindValue(":email",email);
                            query.bindValue(":password",passwordEncrypted);
                            query.bindValue(":contact_number",contactNumber);
                            query.bindValue(":name",name);
                            query.bindValue(":address",address);
                            query.bindValue(":admin",adminAsInt);
                            query.bindValue(":shop_id",shopID);
                            if(query.exec())
                            {
                                QMessageBox::information(this,"16CyclesAddStaff","Successfully added staff");

                                // Clear line edits
                                foreach(QLineEdit* lineEdit, findChildren<QLineEdit*>())
                                {
                                    lineEdit->clear();
                                }
                            }
                            else
                            {
                                QMessageBox::critical(this,"16CyclesAddStaff","Failed to add staff. Contact the 16Cycles IT Support Team adding staff");
                                qDebug()<<(query.lastError().text());
                            }
                        }
                        else
                        {
                            // Email already exists in database
                            QMessageBox::critical(this,"16Cycles","Email already exists. Try again.");
                        }
                    }
                    else
                    {
                        // Password fields do not match
                        QMessageBox::critical(this,"16Cycles","Passwords do not match. Try again.");
                    }
                }
                else
                {
                    // Password fields not long enough
                    QMessageBox::critical(this,"16Cycles","Password too short. Minimum length 5 characters. Try again.");
                }
            }
            else
            {
                // Contact number too short
                QMessageBox::critical(this,"16Cycles","Contact Number too short. Must be 11 digits. Try again.");
            }
        }
        else
        {
            // Data missing from form
            QMessageBox::critical(this,"16Cycles","There is data missing. Try again.");
        }

        // Close the database connection
        mainWindow.closeConnection();
    }
}
