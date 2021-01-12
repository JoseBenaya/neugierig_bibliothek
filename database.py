import sqlite3

from nbibliothek.model import BooksDTO, AnggotaDTO

class NbibliothekDatabase:
    def __init__(self, db_url):
        self.__db_url = db_url
        self.__conn = self.__create_connection()

    def __create_connection(self):
        return sqlite3.connect(self.__db_url)

    def begin_transaction(self):
        pass

    def update_book(self):
        pass

    def update_member(self):
        pass

    def __toDto_book(self, rows):
        book_dtos = []

        for row in rows:
            book_dtos.append(BooksDTO(row[0], row[1], row[2], row[3], row[4], row[5]))

        return book_dtos

    def __toDto_member(self, rows):
        member_dtos = []

        for row in rows:
            member_dtos.append(AnggotaDTO(row[0], row[1], row[2], row[3]))

        return member_dtos

    def init(self):
        drop_books_table = """
            DROP TABLE IF EXISTS books;
        """
        self.__conn.cursor().execute(drop_books_table)

        create_books_table = """        
            CREATE TABLE books (
                Judul            text    PRIMARY KEY NOT NULL,
                Pengarang        text    NOT NULL,
                Penerbit         text    NOT NULL,
                No_Klasifikasi   integer NOT NULL,
                No_Barcode       integer NOT NULL,
                Jumlah_Eksemplar integer NOT NULL
            );
        """
        self.__conn.cursor().execute(create_books_table)

        insert_books_table = """   
            INSERT INTO books VALUES("Sepuluh Hukum Allah", "Pdt. Dr. Stephen Tong", "Momentum", 200, 200001, 5),
                                    ("Allah Tri Tunggal", "Pdt. Dr. Stephen Tong", "Momentum", 200, 200002, 5),
                                    ("Cosmos", "Carl Sagan", "Random House", 500, 500001, 5),
                                    ("The Biology of Belief", " Bruce H. Lipton", "Hay House Inc", 500, 500002, 5),
                                    ("The Most Powerful Idea in the World", "William Rosen", "University Of Chicago Press", 600, 600001, 5),
                                    ("Homo Deus", "Yuval Noah Harari", "Harvill Secker", 600, 600002, 5),
                                    ("AIR KATA KATA", "Sindhunata", "Gramedia Pustaka Utama", 800, 800001, 5),
                                    ("Lelaki Tua dan Laut", "Ernest Hemingway", "Pustaka Jaya", 800, 800002, 5),
                                    ("A History of the Twentieth Century", "Martin Gilbert", "William Morrow Paperbacks", 900, 900001, 5),
                                    ("The Rise and Fall of the Third Reich", "William L. Shirer", "Simon & Schuster", 900, 900002, 5);
        """
        self.__conn.cursor().execute(insert_books_table)

        drop_anggota_table = """
                    DROP TABLE IF EXISTS anggota;
                """
        self.__conn.cursor().execute(drop_anggota_table)

        create_anggota_table = """
            CREATE TABLE anggota (
                Nomor_Induk_Mahasiswa integer PRIMARY KEY NOT NULL,
                Nama                  text    NOT NULL,
                Tanggal_Kembali       date,
                Peminjaman            text
            );
        """
        self.__conn.cursor().execute(create_anggota_table)

        insert_anggota_table = """   
            INSERT INTO anggota VALUES(10101190129, "Charis Hulu", ..., ...),
                                    (10101190602, "Badia Tuahman", ..., ...),
                                    (10101190564, "Michael David", ..., ...),
                                    (10101190694, "Elson P R S", ..., ...),
                                    (10101190476, "Yehezkiel Purnama", ..., ...),
                                    (10101190202, "Arnold Christian", ..., ...),
                                    (10101190203, "Edgar Tigor", ..., ...),
                                    (10101190378, "Jody N Imanuel", ..., ...),
                                    (10101190478, "Yosia Farianto", ..., ...),
                                    (10101190479, "Christopher V", ..., ...),;
        """
        self.__conn.cursor().execute(insert_anggota_table)

    def get_book(self):
        select_from_books = """   
                SELECT *
                  FROM books
                 WHERE Judul=?;
        """

        cursor = self.__conn.cursor().execute(select_from_books)
        rows = cursor.fetchall()

        return self.__toDto_book(rows)

    def get_member(self):
        select_from_anggota = """   
                SELECT *
                  FROM anggota
                 WHERE Nomor_Induk_Mahasiswa=?;
        """

        cursor = self.__conn.cursor().execute(select_from_anggota)
        rows = cursor.fetchall()

        return self.__toDto_member(rows)


