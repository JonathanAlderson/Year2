#ifndef HIRES_H
#define HIRES_H

#include <QDialog>
#include "qcustomplot.h"

namespace Ui {
class Hires;
}

class Hires : public QDialog
{
    Q_OBJECT

public:
    explicit Hires(QWidget *parent = 0);
    ~Hires();

private slots:
    void on_pushButton_clicked();

    void on_graphsRefreshButton_clicked();

private:
    Ui::Hires *ui;
    QVector<double> ticks;
    QVector<double> hiresData;
    QVector<QString> labels;
    QCPBars *hires;
};

#endif // HIRES_H
