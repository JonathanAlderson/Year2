#ifndef ADDSTAFF_H
#define ADDSTAFF_H

#include <QDialog>

namespace Ui {
class AddStaff;
}

class AddStaff : public QDialog
{
    Q_OBJECT

public:
    explicit AddStaff(QWidget *parent = 0);
    ~AddStaff();

private slots:
    void on_cancelButton_clicked();

    void on_addStaffButton_clicked();

private:
    Ui::AddStaff *ui;
};

#endif // ADDSTAFF_H
