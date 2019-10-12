#include "hires.h"
#include "ui_hires.h"
#include "mainwindow.h"

Hires::Hires(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Hires)
{
    ui->setupUi(this);

    // Create bar chart
    hires = new QCPBars(ui-> plot-> xAxis, ui-> plot-> yAxis);
    hires-> setAntialiased(false);
    hires-> setName("Hires");
    hires-> setPen(QPen(QColor(0,0,255).lighter(170))); // Colour of the bar outline
    hires-> setBrush(QColor(0,0,255)); // Colour of bar

    // Add 4 ticks to x axis for each data
    ticks << 1 << 2 << 3 << 4;
    labels << "All Shops" << "Shop 1" << "Shop 2" << "Shop 3";
    QSharedPointer<QCPAxisTickerText> textTicker(new QCPAxisTickerText);
    textTicker-> addTicks(ticks,labels);
    ui-> plot-> xAxis-> setTicker(textTicker);
    ui-> plot-> xAxis-> setSubTicks(false); // Only show the 4 main ticks created
    ui-> plot-> xAxis-> setTickLength(0,5);
    ui-> plot-> xAxis-> setRange(0,5);
    ui-> plot-> yAxis-> setRange(0,10);
    ui-> plot-> yAxis-> setLabel("Hires");

    // Style legend
    ui-> plot-> legend-> setVisible(true);
    ui-> plot-> legend-> setBrush(QColor(255,255,255,150));
}

Hires::~Hires()
{
    delete ui;
}

void Hires::on_pushButton_clicked()
{
    this-> close();
}

void Hires::on_graphsRefreshButton_clicked()
{
    // Clear existing data
    while(!hiresData.isEmpty())
    {
        hiresData.remove(0);
    }

    // Get the dates entered
    QString startDate, endDate;
    startDate = ui-> startDateLineEdit-> text();
    endDate = ui-> endDateLineEdit-> text();

    if(startDate.length() < 0 || endDate.length() < 0)
    {
        return;
    }

    // Open DB
    MainWindow mainWindow;
    if(!mainWindow.openConnection())
    {
        this->close();
        qDebug()<<("Failed open db bikes");
    }

    QSqlQuery query;

    // Count number of hires for all shops
    query.prepare("SELECT COUNT(*) FROM rented_bikes WHERE start_date >= '" + startDate + "' AND end_date <= '" + endDate + "'");
    query.exec();
    query.next();

    // Add data for all shops
    hiresData.append(query.value(0).toDouble());

    // Set the all shops label to show the number of hires
    QString shopsText = "All Shops : ";
    QString shopsDataString = QString::number(query.value(0).toDouble());
    shopsText += shopsDataString;
    ui-> allShopsLabel-> setText(shopsText);

    // Loop each shop id and carry out the same process
    for(int i = 1; i < 4; ++i)
    {
        // Count hires for specific shop
        QString shopID = QString::number(i);
        query.prepare("SELECT COUNT(*) FROM rented_bikes rb INNER JOIN bikes b ON rb.bike_id = b.id WHERE b.shop_id = '" + shopID + "' AND start_date >= '" + startDate + "' AND end_date <= '" + endDate + "'");
        query.exec();
        query.next();
        hiresData.append(query.value(0).toDouble());

        // Change corresponding label
        if(i == 1)
        {
            shopsText = "Shop 1 : ";
            QString shopsDataStringNew = QString::number(query.value(0).toDouble());
            shopsText += shopsDataStringNew;
            ui-> shop1Label-> setText(shopsText);
        }
        if(i == 2)
        {
            shopsText = "Shop 2 : ";
            QString shopsDataStringNew = QString::number(query.value(0).toDouble());
            shopsText += shopsDataStringNew;
            ui-> shop2Label-> setText(shopsText);
        }
        if(i == 3)
        {
            shopsText = "Shop 3 : ";
            QString shopsDataStringNew = QString::number(query.value(0).toDouble());
            shopsText += shopsDataStringNew;
            ui-> shop3Label-> setText(shopsText);
        }
    }

    // Replot data
    hires-> setData(ticks, hiresData);
    ui-> plot->yAxis-> rescale(true);
    ui-> plot-> replot();
    ui-> plot-> update();

    mainWindow.closeConnection();
}
