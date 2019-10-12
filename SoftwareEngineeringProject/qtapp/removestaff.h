#ifndef REMOVESTAFF_H
#define REMOVESTAFF_H

#include <QDialog>

namespace Ui {
class RemoveStaff;
}

class RemoveStaff : public QDialog
{
    Q_OBJECT

public:
    explicit RemoveStaff(QWidget *parent = 0);
    ~RemoveStaff();

private slots:
    void on_removeButton_clicked();

    void on_cancelButton_clicked();

private:
    Ui::RemoveStaff *ui;
};

#endif // REMOVESTAFF_H
