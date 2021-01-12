from datetime import *
from tkinter import *
from tkinter import ttk


class Table:
    def __init__(self, root):
        self.__root = root

    def update_rows(self, data_rows, frame):
        row = data_rows[0]
        self.insert_entry(0, 1, row.Judul, frame)
        self.insert_entry(0, 1, row.Pengarang, frame)
        self.insert_entry(0, 1, row.Penerbit, frame)
        self.insert_entry(0, 1, row.No_Klasifikasi, frame)
        self.insert_entry(0, 1, row.No_Barcode, frame)
        self.insert_entry(0, 1, row.Jumlah_Eksemplar, frame)

    def insert_entry(self, row, column, data, frame):
        data_entry = Label(frame, text=data, padx=2, pady=2, bg='Ghost White')
        data_entry.grid(row=row, column=column, sticky=W)


class NbibliothekUI:
    def __init__(self, nbibliothek_service):
        self.__root = Tk()
        self.__service = nbibliothek_service
        self.__tabs = self.tab()
        self.title()



    def title(self):
        title_label = Label(self.__root, text="Neugierig bibliothek", borderwidth=1, bg="white", font=("Arial", 10))
        title_label.grid(row=0, column=0, columnspan=4, sticky=W)
        address_label = Label(self.__root, text="Ilse. Str No.21 Berlin - 12053", borderwidth=1, bg="white",
                              font=("Arial", 10))
        address_label.grid(row=1, column=0, columnspan=4, sticky=W)
        date_label = Label(self.__root, text=date.today(), borderwidth=1, bg="white", font=("Arial", 10))
        date_label.grid(row=0, column=6, columnspan=2, sticky=E)

    def tab(self):
        tab_control = ttk.Notebook(self.__root)
        find_tab = ttk.Frame(tab_control)
        report_tab = ttk.Frame(tab_control)
        tab_control.add(find_tab, text="Cari")
        tab_control.add(report_tab, text="Laporan")
        tab_control.grid(row=3, column=0, columnspan=7, sticky=W)
        return find_tab, report_tab

    def find_books(self):
        find_label = Label(self.__tabs[0], text="Cari", borderwidth=1, font=("Arial", 10))
        find_label.grid(row=5, column=0)
        find_label_1 = Label(self.__tabs[0], text=":", borderwidth=1, font=("Arial", 10))
        find_label_1.grid(row=5, column=1)
        find_entry = Entry(self.__tabs[0], fg="black", bg="yellow", borderwidth=1, text="enter book title")
        find_entry.grid(row=5, column=2, columnspan=2)
        find_button = Button(self.__tabs[0], text="Cari", command=lambda: self.cari_buku_clicked(find_entry.get()))
        find_button.grid(row=5, column=6)

    def book(self):
        frame_book = LabelFrame(self.__tabs[0], bd=5, bg='Ghost White', font=('Arial', 10, 'bold'), text='Buku')
        frame_book.grid(row=12, column=1, padx=15, pady=15)

        booktitle_label = Label(frame_book, text='Judul :', padx=2, pady=2, bg='Ghost White')
        booktitle_label.grid(row=0, column=0, sticky=W)
        author_label = Label(frame_book, text='Pengarang :', padx=2, pady=2, bg='Ghost White')
        author_label.grid(row=1, column=0, sticky=W)
        publisher_label = Label(frame_book, text='Penerbit :', padx=2, pady=2, bg='Ghost White')
        publisher_label.grid(row=2, column=0, sticky=W)
        classification_label = Label(frame_book, text='No. Klasifikasi :', padx=2, pady=2, bg='Ghost White')
        classification_label.grid(row=3, column=0, sticky=W)
        barcode_label = Label(frame_book, text='No. Barcode :', padx=2, pady=2, bg='Ghost White')
        barcode_label.grid(row=4, column=0, sticky=W)
        exemplar_total_label = Label(frame_book, text='Jumlah Exemplar :', padx=2, pady=2, bg='Ghost White')
        exemplar_total_label.grid(row=5, column=0, sticky=W)

    def find_nim(self):
        nim_label = Label(self.__tabs[0], text="Nomor Induk Mahasiswa", borderwidth=1, font=("Arial", 10))
        nim_label.grid(row=17, column=0)
        nim_label_1 = Label(self.__tabs[0], text=":", borderwidth=1, font=("Arial", 10))
        nim_label_1.grid(row=17, column=1)
        nim_entry = Entry(self.__tabs[0], fg="black", bg="yellow", borderwidth=1, text="enter NIM")
        nim_entry.grid(row=17, column=2, columnspan=2)
        nim_button = Button(self.__tabs[0], text="Cari", command=lambda: self.cari_mahasiswa_clicked(nim_entry.get()))
        nim_button.grid(row=17, column=6)
        nim_button = Button(self.__tabs[0], text="Pinjam", command=lambda: self.cari_mahasiswa_clicked(nim_entry.get()))
        nim_button.grid(row=18, column=6)

    def member(self):
        frame_member = LabelFrame(self.__tabs[0], bd=5, bg='Ghost White', font=('Arial', 10, 'bold'), text='Anggota')
        frame_member.grid(row=25, column=0, columnspan=4, padx=15, pady=15)
        member_label = Label(frame_member, text='Nama :', padx=2, pady=2, bg='Ghost White')
        member_label.grid(row=0, column=0, sticky=W)
        nim_label = Label(frame_member, text='NIM :', padx=2, pady=2, bg='Ghost White')
        nim_label.grid(row=1, column=0, sticky=W)
        return_date_label = Label(frame_member, text='Tanggal Kembali :', padx=2, pady=2, bg='Ghost White')
        return_date_label.grid(row=2, column=0, sticky=W)
        borrowed_book_label = Label(frame_member, text='Peminjaman :', padx=2, pady=2, bg='Ghost White')
        borrowed_book_label.grid(row=3, column=0, sticky=W)

    def result_message(self):
        find_book_message = Label(self.__tabs[0], text="Judul BUKU Tidak Ditemukan !!!", bg='red', borderwidth=1,
                                  relief='groove')
        find_book_message.grid(row=7, column=1)
        find_book_message = Label(self.__tabs[0], text="NIM tidak ditemukan !!!", bg='red', borderwidth=1,
                                  relief='groove')
        find_book_message.grid(row=22, column=1)
        find_book_message = Label(self.__tabs[0], text="Telah melebihi Quota Peminjaman !!!", bg='red', borderwidth=1,
                                  relief='groove')
        find_book_message.grid(row=23, column=1)

    def cari_buku_clicked(self, judul):
        book_dto =

    def cari_mahasiswa_clicked(self, nim):
        pass

    def mainloop(self):
        self.__root.mainloop()


if __name__ == '__main__':
    tes = NbibliothekUI()
    tes.find_nim()
    tes.find_books()
    tes.book()
    tes.member()
    tes.result_message()
    tes.mainloop()
