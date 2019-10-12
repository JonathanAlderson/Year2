#ifndef UPDATESTAFF_H
#define UPDATESTAFF_H

#include <QDialog>

namespace Ui {
class UpdateStaff;
}

class UpdateStaff : public QDialog
{
    Q_OBJECT

public:
    explicit UpdateStaff(QWidget *parent = 0);
    ~UpdateStaff();

private slots:
    void on_findButton_clicked();

    void on_cancelButton_clicked();

    void on_updateAdminButton_clicked();

    void on_updatePersonalDetailsButton_clicked();

private:
    Ui::UpdateStaff *ui;
    bool findSuccess;
};

#endif // UPDATESTAFF_H
