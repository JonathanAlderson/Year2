#ifndef RESETPASSWORD_H
#define RESETPASSWORD_H

#include <QDialog>

namespace Ui {
class ResetPassword;
}

class ResetPassword : public QDialog
{
    Q_OBJECT

public:
    explicit ResetPassword(QWidget *parent = 0);
    ~ResetPassword();
    void setEmail(QString _email);

private slots:
    void on_cancelButton_clicked();

    void on_confirmButton_clicked();

private:
    Ui::ResetPassword *ui;
    QString email;
};

#endif // RESETPASSWORD_H
