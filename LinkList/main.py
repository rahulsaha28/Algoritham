
from Project4.LinkList import Linklist;

ls = Linklist();

ls.insert(20);
ls.insert(30);
ls.insert(40);
ls.insert('Rahul');
ls.insert('SUST');

ls.delete(2);

print(ls.length());

print(ls.search(40));