#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Set logo label to image
    QPixmap pix(":/resources/images/app_static_images_logo.png");
    int w = ui-> logo-> width();
    int h = ui-> logo-> height();
    ui-> logo-> setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
}

MainWindow::~MainWindow()
{
    delete ui;
}

// Close database connection
void MainWindow::closeConnection()
{
    db.close();
    db.removeDatabase(QSqlDatabase::defaultConnection);
}

// Open database connection, true if opened, false otherwise
bool MainWindow::openConnection()
{
    db = QSqlDatabase::addDatabase("QSQLITE");
    QDir dir = QDir::current();
    QString dbpath = dir.currentPath();
    dbpath += "/app.db";
    db.setDatabaseName(dbpath);

    if(!db.open())
    {
        qDebug()<<("database not open");
        return false;
    }
    qDebug()<<("database open");
    return true;
}

// Quit slot
void MainWindow::on_quitButton_clicked()
{
    // Display question to check user wants to quit
    QMessageBox::StandardButton reply = QMessageBox::question(this,"16Cycles","Are you sure you want to quit?",
                                                              QMessageBox::Yes | QMessageBox::No);

    // Close window if yes clicked, else do nothing
    if(reply == QMessageBox::Yes)
        this-> close();
}

// Sign in slot
void MainWindow::on_signInButton_clicked()
{
    // Get data entered on window as strings
    QString email,password;
    email = ui-> usernameLineEdit-> text();
    password = ui-> passwordLineEdit-> text();

    // Open connection to database
    if(!openConnection())
    {
        this->close();
        qDebug()<<("Error opening db mainwindow");
    }

    // Prepare query to find username and password in database
    QSqlQuery query;
    query.prepare("SELECT password,name FROM staff WHERE email = '" + email + "'");

    // Execute query
    query.exec();

    // If query returned a value, log in user
    if(query.next())
    {
        // Decrypt password
        SimpleCrypt crypto(Q_UINT64_C(0x0c2ad4a4acb9f023));
        QString passwordDecrypt = crypto.decryptToString(query.value(0).toString());

        // Compare with users input
        if(QString::compare(password,passwordDecrypt,Qt::CaseSensitive) != 0)
        {
            QMessageBox::critical(this,"16Cycles","Username and password incorrect");
            return;
        }

        // Always close connection before closing window and opening new window
        closeConnection();

        // Success message
        QMessageBox::information(this,"16Cycles","Successful log in");

        // Clear line edits
        foreach(QLineEdit* lineEdit, findChildren<QLineEdit*>())
        {
            lineEdit->clear();
        }

        // Create new window
        AdminHome adminHome;
        adminHome.setModal(true);
        adminHome.setGroupBoxName(query.value(1).toString());
        adminHome.setUserEmail(email);
        QDesktopWidget desktop;
        QRect mainScreenSize = desktop.availableGeometry(desktop.primaryScreen());
        adminHome.setFixedSize(mainScreenSize.width(),mainScreenSize.height());

        // Remove title bar
        adminHome.setWindowFlags(Qt::Window | Qt::FramelessWindowHint);

        // Set window title
        adminHome.setWindowTitle("16CyclesAdminHome");

        // Show window
        adminHome.exec();

    }

    // If query has no values, username and password incorrect, display error to user
    else
        QMessageBox::critical(this,"16Cycles","Username and password incorrect");
}
