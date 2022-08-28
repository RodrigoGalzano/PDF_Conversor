/********************************************************************************
** Form generated from reading UI file 'pagestmgfNU.ui'
**
** Created by: Qt User Interface Compiler version 6.3.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PAGESTMGFNU_H
#define PAGESTMGFNU_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_application_pages
{
public:
    QWidget *page_1;
    QVBoxLayout *verticalLayout;
    QFrame *frame_Principal;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_ola;
    QGridLayout *gridLayout;
    QLineEdit *lineEdit;
    QPushButton *psb_AlterarNome;
    QWidget *page_2;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_2;
    QWidget *page_3;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_3;

    void setupUi(QStackedWidget *application_pages)
    {
        if (application_pages->objectName().isEmpty())
            application_pages->setObjectName(QString::fromUtf8("application_pages"));
        application_pages->resize(924, 541);
        page_1 = new QWidget();
        page_1->setObjectName(QString::fromUtf8("page_1"));
        verticalLayout = new QVBoxLayout(page_1);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame_Principal = new QFrame(page_1);
        frame_Principal->setObjectName(QString::fromUtf8("frame_Principal"));
        frame_Principal->setMinimumSize(QSize(500, 100));
        frame_Principal->setMaximumSize(QSize(500, 100));
        frame_Principal->setFrameShape(QFrame::StyledPanel);
        frame_Principal->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(frame_Principal);
        verticalLayout_4->setSpacing(4);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        label_ola = new QLabel(frame_Principal);
        label_ola->setObjectName(QString::fromUtf8("label_ola"));
        label_ola->setMinimumSize(QSize(0, 50));
        label_ola->setMaximumSize(QSize(16777215, 50));
        label_ola->setStyleSheet(QString::fromUtf8("font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);"));

        verticalLayout_4->addWidget(label_ola);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        lineEdit = new QLineEdit(frame_Principal);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setMinimumSize(QSize(0, 40));
        lineEdit->setMaximumSize(QSize(16777215, 50));
        QFont font;
        font.setBold(true);
        lineEdit->setFont(font);
        lineEdit->setStyleSheet(QString::fromUtf8("QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}"));

        gridLayout->addWidget(lineEdit, 0, 0, 1, 1);

        psb_AlterarNome = new QPushButton(frame_Principal);
        psb_AlterarNome->setObjectName(QString::fromUtf8("psb_AlterarNome"));
        psb_AlterarNome->setMinimumSize(QSize(120, 36));
        psb_AlterarNome->setMaximumSize(QSize(16777215, 50));
        psb_AlterarNome->setFont(font);
        psb_AlterarNome->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 0, 127)	\n"
"}"));

        gridLayout->addWidget(psb_AlterarNome, 0, 1, 1, 1);


        verticalLayout_4->addLayout(gridLayout);


        verticalLayout->addWidget(frame_Principal, 0, Qt::AlignHCenter);

        application_pages->addWidget(page_1);
        page_2 = new QWidget();
        page_2->setObjectName(QString::fromUtf8("page_2"));
        verticalLayout_2 = new QVBoxLayout(page_2);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label_2 = new QLabel(page_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(label_2);

        application_pages->addWidget(page_2);
        page_3 = new QWidget();
        page_3->setObjectName(QString::fromUtf8("page_3"));
        verticalLayout_3 = new QVBoxLayout(page_3);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        label_3 = new QLabel(page_3);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        verticalLayout_3->addWidget(label_3);

        application_pages->addWidget(page_3);

        retranslateUi(application_pages);

        QMetaObject::connectSlotsByName(application_pages);
    } // setupUi

    void retranslateUi(QStackedWidget *application_pages)
    {
        application_pages->setWindowTitle(QCoreApplication::translate("application_pages", "StackedWidget", nullptr));
        label_ola->setText(QCoreApplication::translate("application_pages", "Ol\303\241", nullptr));
        lineEdit->setPlaceholderText(QCoreApplication::translate("application_pages", "Escreva o seu nome", nullptr));
        psb_AlterarNome->setText(QCoreApplication::translate("application_pages", "Alterar Texto", nullptr));
        label_2->setText(QCoreApplication::translate("application_pages", "Pagina 2", nullptr));
        label_3->setText(QCoreApplication::translate("application_pages", "Pagina 3", nullptr));
    } // retranslateUi

};

namespace Ui {
    class application_pages: public Ui_application_pages {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PAGESTMGFNU_H
