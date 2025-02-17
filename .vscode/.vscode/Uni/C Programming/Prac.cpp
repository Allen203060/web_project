#include <iostream>
#include <string>
using namespace std;

class Book{
    public:
    int b_id;
    string title;
    string status;

    Book(int id, string title, string status="Not Issued"){
        b_id=id;
        title=title;
        status=status;
    }
    void issue_book(){
        if (status=="Not Issued"){
            status="Issued";
            cout<<"Book"<<title<<"has been issued!"<<endl;
        }
        else{
            cout<<"Book"<<title<<"is already issued!"<<endl;
        }
    }
    void return_book(){
        if (status=="Issued"){
            status="Not Issued";
            cout<<"Book"<<title<<"has been returned!"<<endl;
        }
        else{
            cout<<"Book"<<title<<"was not issued!"<<endl;
        }
    void print_details(){
        cout<<"Book ID:"<<b_id<<"Title:"<<title<<"Status"<<status<<endl;
    }
}
class Lib{
    private:
        Book*books[10];
        int size;
    public:
    Lib(){
        size=0;
    }
    void add_book(Book*book){
        if (size<10){
            books[size]=book;
            size++;
        }
        else{
            cout<<"Library is full!Can't add more books!"<<endl;
        }}

    void issue_book_by_ID(){
        for (int i=0;i<size;i++){
            if (books[i]->b_id==id){
                books[i]->issue_book();
                return;
                }
            cout<<"Book with ID"<<b_id<<"was not found"<<endl;
        }
        void return_book_by_id(int id) {
        for (int i = 0; i < size; ++i) {
            if (books[i]->book_id == id) {
                books[i]->return_book();
                return;
            }
        }
        cout << "Book with ID " << id << " not found." << endl;
    }
        void print_not_issued_books() {
        for (int i = 0; i < size; ++i) {
            if (books[i]->status == "Not Issued") {
                books[i]->print_details();
            }
        }
    }
    void print_not_issued_books() {
        for (int i = 0; i < size; ++i) {
            if (books[i]->status == "Not Issued") {
                books[i]->print_details();
            }
        }
    }
    void print_issued_books() {
        for (int i = 0; i < size; ++i) {
            if (books[i]->status == "Issued") {
                books[i]->print_details();
            }
        }
    }
};
int main() {
    Lib library;
    library.add_book(new Book(1, "The Catcher in the Rye"));
    library.add_book(new Book(2, "To Kill a Mockingbird"));
    library.add_book(new Book(3, "1984"));
    library.add_book(new Book(4, "Pride and Prejudice"));
    library.add_book(new Book(5, "The Great Gatsby"));
    library.add_book(new Book(6, "Moby-Dick"));
    library.add_book(new Book(7, "War and Peace"));
    library.add_book(new Book(8, "The Odyssey"));
    library.add_book(new Book(9, "Crime and Punishment"));
    library.add_book(new Book(10, "The Brothers Karamazov"));
    int book_id;
    cout << "Enter the ID of the book you want to issue: ";
    cin >> book_id;
    library.issue_book_by_id(b_id);
    cout << "\nIssued books:" << endl;
    library.print_issued_books();

    return 0;
}