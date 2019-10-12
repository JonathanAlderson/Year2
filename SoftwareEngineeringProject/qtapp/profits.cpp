#include "profits.h"
#include "ui_profits.h"
#include "mainwindow.h"

Profits::Profits(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Profits)
{
    ui->setupUi(this);

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }
    QSqlQuery *queryp = new QSqlQuery(mainWindow.db);

    // Populate profits shop id combo box
    QSqlQueryModel *modelShops = new QSqlQueryModel();
    queryp-> prepare("SELECT id FROM shops");
    queryp-> exec();
    queryp-> next();
    modelShops-> setQuery(*queryp);
    ui-> filterTwoDatesShopsComboBox-> setModel(modelShops);
    ui-> filterAllTimeShopsComboBox-> setModel(modelShops);

    // Add four graphs to the plot, one for all shops then one for each shop
    ui-> plot-> addGraph();
    ui-> plot-> addGraph();
    ui-> plot-> addGraph();
    ui-> plot-> addGraph();

    // Set the names
    ui-> plot-> graph(0)-> setName("All Shops");
    ui-> plot-> graph(1)-> setName("Shop 1");
    ui-> plot-> graph(2)-> setName("Shop 2");
    ui-> plot-> graph(3)-> setName("Shop 3");

    // Set styles of all graphs
    ui-> plot-> graph(0)-> setLineStyle(QCPGraph::lsLine);
    ui-> plot-> graph(0)-> setScatterStyle(QCPScatterStyle(QCPScatterStyle::ssCross));
    ui-> plot-> graph(1)-> setLineStyle(QCPGraph::lsLine);
    ui-> plot-> graph(1)-> setScatterStyle(QCPScatterStyle(QCPScatterStyle::ssCross));
    ui-> plot-> graph(2)-> setLineStyle(QCPGraph::lsLine);
    ui-> plot-> graph(2)-> setScatterStyle(QCPScatterStyle(QCPScatterStyle::ssCross));
    ui-> plot-> graph(3)-> setLineStyle(QCPGraph::lsLine);
    ui-> plot-> graph(3)-> setScatterStyle(QCPScatterStyle(QCPScatterStyle::ssCross));

    // Change colour of line for each graph
    QPen pen0,pen1,pen2,pen3;
    pen0 = ui-> plot-> graph(0)-> pen();
    pen0.setWidth(1.5);
    pen0.setColor(QColor(255,0,0)); //red
    ui-> plot-> graph(0)-> setPen(pen0);
    pen1 = ui-> plot-> graph(1)-> pen();
    pen1.setWidth(1.5);
    pen1.setColor(QColor(0,131,0)); //green
    ui-> plot-> graph(1)-> setPen(pen1);
    pen2 = ui-> plot-> graph(2)-> pen();
    pen2.setWidth(1.5);
    pen2.setColor(QColor(0,0,255)); //blue
    ui-> plot-> graph(2)-> setPen(pen2);
    pen3 = ui-> plot-> graph(3)-> pen();
    pen3.setWidth(1.5);
    pen3.setColor(QColor(158,0,237)); //purple
    ui-> plot-> graph(3)-> setPen(pen3);

    // Set x axis to display dates
    QSharedPointer<QCPAxisTickerDateTime> dateTicker(new QCPAxisTickerDateTime);
    dateTicker->setDateTimeFormat("yyyy/MM/dd");
    ui-> plot-> xAxis-> setTicker(dateTicker);

    // Not sure if needed
    ui-> plot-> graph(0)-> rescaleAxes(true);
    ui-> plot-> graph(1)-> rescaleAxes(true);
    ui-> plot-> graph(2)-> rescaleAxes(true);
    ui-> plot-> graph(3)-> rescaleAxes(true);

    // Style the plot
    ui-> plot-> xAxis-> setTickLabelFont(QFont(QFont().family(),10));
    ui-> plot-> yAxis-> setTickLabelFont(QFont(QFont().family(),10));
    ui-> plot-> xAxis-> setLabel("Date");
    ui-> plot-> yAxis-> setLabel("profit");
    ui-> plot-> xAxis-> grid()-> setVisible(true);
    ui-> plot-> xAxis-> grid()-> setPen(QPen(QColor(130,130,130),0,Qt::DotLine));
    ui-> plot-> yAxis-> grid()-> setSubGridVisible(true);
    ui-> plot-> yAxis-> grid()-> setPen(QPen(QColor(130,130,130),0,Qt::SolidLine));
    ui-> plot-> yAxis-> grid()-> setSubGridPen(QPen(QColor(130,130,130),0,Qt::DotLine));
    ui-> plot-> legend-> setVisible(true);
    ui-> plot-> legend-> setBrush(QColor(255,255,255,150));

    mainWindow.closeConnection();
}

Profits::~Profits()
{
    delete ui;
}

void Profits::on_goBackButton_clicked()
{
    this-> close();
}

// Refresh profits label
void Profits::on_filterTwoDatesRefreshButton_clicked()
{
    // Get the dates entered
    QString dateOne,dateTwo;
    dateOne = ui-> dateOneLineEdit-> text();
    dateTwo = ui-> dateTwoLineEdit-> text();

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQuery query;
    query.prepare("SELECT SUM(o.total_price) FROM orders o WHERE date between '" + dateOne + " 00:00:00' AND '" + dateTwo + " 00:00:00'");

    // Execute query
    if(!query.exec())
    {
        QMessageBox::critical(this,"16CyclesProfits","Failed to run query. Enter dates in format 0000-00-00 (year-month-day)");
    }

    else
    {
        ui-> filterTwoDatesProfitsLabel-> setText("£0.00");
    }

    // If query returned a value
    if(query.next())
    {
        QString profit = "£";
        profit += query.value(0).toString();
        ui-> filterTwoDatesProfitsLabel-> setText(profit);
    }

    else
    {
        ui-> filterTwoDatesProfitsLabel-> setText("£0.00");
    }


    mainWindow.closeConnection();
}

// Automatically update profits label when combo box changed
void Profits::on_filterTwoDatesShopsComboBox_activated(const QString &arg1)
{
    // Get dates again and data from combo box
    QString dateOne,dateTwo,shopID;
    dateOne = ui-> dateOneLineEdit-> text();
    dateTwo = ui-> dateTwoLineEdit-> text();
    shopID = arg1;

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQuery query;
    query.prepare("SELECT SUM(o.total_price) FROM orders o INNER JOIN rented_bikes rb ON o.id = rb.id INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '" + shopID + "' AND date BETWEEN '" + dateOne + " 00:00:00' AND '" + dateTwo + " 00:00:00'");

    // Execute query
    if(!query.exec())
    {
        QMessageBox::critical(this,"16CyclesProfits","Failed to run query. Enter dates in format 0000-00-00 (year-month-day)");
    }

    else
    {
        ui-> filterTwoDatesProfitsShopsLabel-> setText("£0.00");
    }

    // If query returned a value
    if(query.next())
    {
        QString profit = "£";
        profit += query.value(0).toString();
        ui-> filterTwoDatesProfitsShopsLabel-> setText(profit);
    }

    else
    {
        ui-> filterTwoDatesProfitsShopsLabel-> setText("£0.00");
    }


    mainWindow.closeConnection();
}

// Automatically update all time profits label when shop id changed
void Profits::on_filterAllTimeShopsComboBox_activated(const QString &arg1)
{
    QString shopID;
    shopID = arg1;

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQuery query;
    query.prepare("SELECT SUM(o.total_price) FROM orders o INNER JOIN rented_bikes rb ON o.id = rb.id INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '" + shopID + "'");

    // Execute query
    if(!query.exec())
    {
        QMessageBox::critical(this,"16CyclesProfits","Failed to run query.");
    }

    else
    {
        ui-> filterAllTimeShopsProfitsLabel-> setText("£0.00");
    }

    // If query returned a value
    if(query.next())
    {
        QString profit = "£";
        profit += query.value(0).toString();
        ui-> filterAllTimeShopsProfitsLabel-> setText(profit);
    }

    else
    {
        ui-> filterAllTimeShopsProfitsLabel-> setText("£0.00");
    }


    mainWindow.closeConnection();
}

void Profits::on_graphsRefreshButton_clicked()
{
    // Clear existing data
    while(!x0.isEmpty())
    {
        x0.remove(0);
    }
    while(!y0.isEmpty())
    {
        y0.remove(0);
    }
    while(!x1.isEmpty())
    {
        x1.remove(0);
    }
    while(!y1.isEmpty())
    {
        y1.remove(0);
    }
    while(!x2.isEmpty())
    {
        x2.remove(0);
    }
    while(!y2.isEmpty())
    {
        y2.remove(0);
    }
    while(!x3.isEmpty())
    {
        x3.remove(0);
    }
    while(!y3.isEmpty())
    {
        y3.remove(0);
    }

    // Get the dates entered
    QString startDate, endDate;
    startDate = ui-> startDateLineEdit-> text();
    endDate = ui-> endDateLineEdit-> text();

    if(startDate.length() < 0 || endDate.length() < 0)
    {
        return;
    }

    // Convert entered dates to a datetime variable
    QDateTime time1,time2;
    time1 = QDateTime::fromString(startDate,"yyyy-MM-dd");
    time2 = QDateTime::fromString(endDate,"yyyy-MM-dd");

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQuery query;

    // Check radio boxes for which graphs to plot
    if(ui-> allShopsCheckBox-> isChecked())
    {
        // Loop through dates weekly until the week is not complete from start date
        for(double j = time1.toTime_t(); j < time2.toTime_t(); j = j + 7*24*60*60)
        {
            // Create dates for query
            QDateTime firstDate,secondDate;
            firstDate.setTime_t(int(j));
            secondDate.setTime_t(int((j + 7*24*60*60) - 1));
            QString firstDateAsString = firstDate.toString("yyyy-MM-dd");
            QString secondDateAsString = secondDate.toString("yyyy-MM-dd");

            // Execute query to get earnings for the week
            query.prepare("SELECT SUM(o.total_price) FROM orders o WHERE date BETWEEN '" + firstDateAsString + " 00:00:00' AND '" + secondDateAsString + " 00:00:00'");
            query.exec();
            query.next();
            x0.append(j);
            y0.append(query.value(0).toDouble());
        }
    }

    if(ui-> shop1CheckBox-> isChecked())
    {
        // Loop through dates weekly until the week is not complete from start date
        for(double j = time1.toTime_t(); j < time2.toTime_t(); j = j + 7*24*60*60)
        {
            // Create dates for query
            QDateTime firstDate,secondDate;
            firstDate.setTime_t(int(j));
            secondDate.setTime_t(int((j + 7*24*60*60) - 1));
            QString firstDateAsString = firstDate.toString("yyyy-MM-dd");
            QString secondDateAsString = secondDate.toString("yyyy-MM-dd");

            // Execute query to get earnings for the week
            query.prepare("SELECT SUM(o.total_price) FROM orders o INNER JOIN rented_bikes rb ON o.id = rb.id INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '1' AND date BETWEEN '" + firstDateAsString + " 00:00:00' AND '" + secondDateAsString + " 00:00:00'");
            query.exec();
            query.next();
            x1.append(j);
            y1.append(query.value(0).toDouble());
        }
    }

    if(ui-> shop2CheckBox-> isChecked())
    {
        // Loop through dates weekly until the week is not complete from start date
        for(double j = time1.toTime_t(); j < time2.toTime_t(); j = j + 7*24*60*60)
        {
            // Create dates for query
            QDateTime firstDate,secondDate;
            firstDate.setTime_t(int(j));
            secondDate.setTime_t(int((j + 7*24*60*60) - 1));
            QString firstDateAsString = firstDate.toString("yyyy-MM-dd");
            QString secondDateAsString = secondDate.toString("yyyy-MM-dd");

            // Execute query to get earnings for the week
            query.prepare("SELECT SUM(o.total_price) FROM orders o INNER JOIN rented_bikes rb ON o.id = rb.id INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '2' AND date BETWEEN '" + firstDateAsString + " 00:00:00' AND '" + secondDateAsString + " 00:00:00'");
            query.exec();
            query.next();
            x2.append(j);
            y2.append(query.value(0).toDouble());
        }
    }

    if(ui-> shop3CheckBox-> isChecked())
    {
        // Loop through dates weekly until the week is not complete from start date
        for(double j = time1.toTime_t(); j < time2.toTime_t(); j = j + 7*24*60*60)
        {
            // Create dates for query
            QDateTime firstDate,secondDate;
            firstDate.setTime_t(int(j));
            secondDate.setTime_t(int((j + 7*24*60*60) - 1));
            QString firstDateAsString = firstDate.toString("yyyy-MM-dd");
            QString secondDateAsString = secondDate.toString("yyyy-MM-dd");

            // Execute query to get earnings for the week
            query.prepare("SELECT SUM(o.total_price) FROM orders o INNER JOIN rented_bikes rb ON o.id = rb.id INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '3' AND date BETWEEN '" + firstDateAsString + " 00:00:00' AND '" + secondDateAsString + " 00:00:00'");
            query.exec();
            query.next();
            x3.append(j);
            y3.append(query.value(0).toDouble());
        }
    }

    // Replot data
    ui-> plot-> graph(0)-> setData(x0,y0);
    ui-> plot-> graph(1)-> setData(x1,y1);
    ui-> plot-> graph(2)-> setData(x2,y2);
    ui-> plot-> graph(3)-> setData(x3,y3);
    ui-> plot-> rescaleAxes(true);
    ui-> plot-> replot();
    ui-> plot-> update();

    mainWindow.closeConnection();
}
