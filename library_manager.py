from book import BookItem

class LibrarySystem:
    def _init_(self):
        self.records = []      # ← FIX: this must exist
        self.load_file()

    def insert_book(self, book):
        self.records.append(book)
        self.write_file()

    def find_code(self, code):
        for b in self.records:
            if b.code == code:
                return b
        return None

    def find_title(self, key):
        key = key.lower()
        return [b for b in self.records if key in b.title.lower()]

    def show_all(self):
        print("\n--- Library Collection ---")
        if not self.records:
            print("No books found.")
            return
        for b in self.records:
            print(f"{b.title} | {b.writer} | {b.code} | {b.state}")

    def write_file(self):
        with open("books.txt", "w") as f:
            for b in self.records:
                f.write(f"{b.title},{b.writer},{b.code},{b.state}\n")

    def load_file(self):
        try:
            with open("books.txt", "r") as f:
                for line in f:
                    t, w, c, s = line.strip().split(",")
                    b = BookItem(t, w, c)
                    b.state = s
                    self.records.append(b)
        except FileNotFoundError:
            pass